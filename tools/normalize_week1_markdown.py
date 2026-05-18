#!/usr/bin/env python3
"""
Normalize Week 1 Markdown files that were accidentally compressed into very long
physical lines.

Run from the root of the mlsys-prep repository on branch week-01-foundations:

    python3 tools/normalize_week1_markdown.py

The script:
- creates .bak files before editing;
- inserts real physical line breaks before headings, bullets, tables, and fences;
- expands compressed Mermaid/code fences;
- wraps prose to < 100 characters where safe;
- validates that all Markdown lines are < 120 characters;
- validates that key Week 1 files have plausible physical line counts.

It is intentionally mechanical. It does not add or remove technical content.
"""

from __future__ import annotations

from pathlib import Path
import re
import shutil
import sys
import textwrap

TARGETS = [
    "llms/01_llm_fundamentals.md",
    "nvidia/01_latest_nvidia_platforms.md",
    "systems/00_llm_gpu_bridge.md",
    "behavioral/00_behavioral_strategy.md",
    "assessments/weekly_quizzes/week_01_quiz.md",
    "references/sources.md",
]

WRAP_WIDTH = 96
MAX_LINE = 119

HEADING_RE = re.compile(r"(?<!^)\s+(#{1,6}\s+)")
BULLET_RE = re.compile(r"\s+([-*]\s+)(?=\S)")
NUMBER_RE = re.compile(r"\s+(\d+\.\s+)(?=\S)")
MERMAID_OPEN_RE = re.compile(r"\s*```mermaid\s*")
TEXT_OPEN_RE = re.compile(r"\s*```text\s*")
FENCE_CLOSE_RE = re.compile(r"\s*```\s*")
TABLE_SPLIT_RE = re.compile(r"\s+(?=\|[^|\n]+?\|)")
URL_RE = re.compile(r"^https?://|<https?://")


def protect_code_fences(text: str) -> str:
    """Put code fence markers on their own lines before other splitting."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Opening fences. This catches inline forms like "text ```mermaid flowchart".
    text = re.sub(r"\s*```mermaid\s*", "\n```mermaid\n", text)
    text = re.sub(r"\s*```text\s*", "\n```text\n", text)

    # Closing fences. Be conservative: only split exact triple-backtick markers.
    text = re.sub(r"\s*```\s*", "\n```\n", text)

    # Repair accidental "``` mermaid" style split, just in case.
    text = text.replace("```\nmermaid", "```mermaid")
    text = text.replace("```\ntext", "```text")
    return text


def split_structural_markers(text: str) -> str:
    """Insert newlines before Markdown structural tokens."""
    text = HEADING_RE.sub(r"\n\n\1", text)
    text = BULLET_RE.sub(r"\n\1", text)
    text = NUMBER_RE.sub(r"\n\1", text)

    # If tables were compressed as "| A | B | | --- | --- | | x | y |",
    # split before each row-like pipe group.
    text = re.sub(r"\s+(\|\s*---)", r"\n\1", text)
    text = re.sub(r"\s+(\|[^|\n]+?\|(?:\s*[^|\n]+?\|)+)", r"\n\1", text)

    # Put blockquote prompts on their own lines when compressed.
    text = re.sub(r"\s+(>\s+)", r"\n\n\1", text)

    return text


def normalize_blank_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    prev_blank = False

    for raw in lines:
        line = raw.rstrip()
        blank = not line.strip()

        if blank:
            if not prev_blank:
                out.append("")
            prev_blank = True
            continue

        stripped = line.strip()

        # Add a blank line before headings unless at file start.
        if stripped.startswith("#") and out and out[-1] != "":
            out.append("")

        out.append(stripped)
        prev_blank = False

        # Add blank line after headings and fences.
        if stripped.startswith("#") or stripped in {"```", "```mermaid", "```text"}:
            out.append("")
            prev_blank = True

    # Remove leading/trailing blank lines and collapse triples.
    while out and out[0] == "":
        out.pop(0)
    while out and out[-1] == "":
        out.pop()

    collapsed: list[str] = []
    blank_count = 0
    for line in out:
        if line == "":
            blank_count += 1
            if blank_count <= 1:
                collapsed.append(line)
        else:
            blank_count = 0
            collapsed.append(line)

    return collapsed


def is_wrappable(line: str, in_code: bool) -> bool:
    stripped = line.strip()

    if in_code:
        return False
    if not stripped:
        return False
    if stripped.startswith("#"):
        return False
    if stripped.startswith(("- ", "* ", "> ")):
        return len(stripped) > MAX_LINE
    if re.match(r"^\d+\.\s+", stripped):
        return len(stripped) > MAX_LINE
    if stripped.startswith("|"):
        return False
    if stripped in {"```", "```mermaid", "```text"}:
        return False
    if URL_RE.search(stripped):
        return False

    return True


def wrap_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    in_code = False

    for line in lines:
        stripped = line.strip()

        if stripped in {"```", "```mermaid", "```text"}:
            out.append(stripped)
            in_code = not in_code
            continue

        if is_wrappable(stripped, in_code):
            wrapped = textwrap.wrap(
                stripped,
                width=WRAP_WIDTH,
                break_long_words=False,
                break_on_hyphens=False,
            )
            out.extend(wrapped or [""])
        elif (stripped.startswith(("- ", "* ")) or re.match(r"^\d+\.\s+", stripped)) and len(stripped) > MAX_LINE:
            if stripped.startswith(("- ", "* ")):
                prefix = stripped[:2]
                body = stripped[2:]
            else:
                m = re.match(r"^(\d+\.\s+)(.*)$", stripped)
                assert m
                prefix = m.group(1)
                body = m.group(2)

            wrapped = textwrap.wrap(
                body,
                width=WRAP_WIDTH - len(prefix),
                initial_indent=prefix,
                subsequent_indent=" " * len(prefix),
                break_long_words=False,
                break_on_hyphens=False,
            )
            out.extend(wrapped)
        else:
            out.append(stripped)

    return out


def normalize_file(path: Path) -> None:
    original = path.read_text(encoding="utf-8")
    backup = path.with_suffix(path.suffix + ".bak")

    if not backup.exists():
        shutil.copy2(path, backup)

    text = protect_code_fences(original)
    text = split_structural_markers(text)

    lines = text.splitlines()
    lines = normalize_blank_lines(lines)
    lines = wrap_lines(lines)
    lines = normalize_blank_lines(lines)

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate(root: Path) -> int:
    errors: list[str] = []

    for rel in TARGETS:
        path = root / rel
        lines = path.read_text(encoding="utf-8").splitlines()

        if len(lines) < 80 and rel != "references/sources.md":
            errors.append(f"{rel}: only {len(lines)} physical lines")

        for i, line in enumerate(lines, start=1):
            if len(line) >= 120:
                errors.append(f"{rel}:{i}: {len(line)} chars")

            stripped = line.strip()
            if "```mermaid" in line and stripped != "```mermaid":
                errors.append(f"{rel}:{i}: Mermaid fence shares line with content")
            if " ## " in line:
                errors.append(f"{rel}:{i}: inline heading marker")
            if stripped.startswith("#") and (" - " in line or " | " in line):
                errors.append(f"{rel}:{i}: heading line contains list/table content")

    if errors:
        print("Validation failed:")
        for err in errors:
            print(f"  {err}")
        return 1

    print("OK: normalized Week 1 Markdown files passed validation.")
    for rel in TARGETS:
        count = len((root / rel).read_text(encoding="utf-8").splitlines())
        print(f"  {rel}: {count} physical lines")

    return 0


def main() -> int:
    root = Path.cwd()

    missing = [rel for rel in TARGETS if not (root / rel).exists()]
    if missing:
        print("Run this from the mlsys-prep repository root.")
        print("Missing files:")
        for rel in missing:
            print(f"  {rel}")
        return 1

    for rel in TARGETS:
        normalize_file(root / rel)

    return validate(root)


if __name__ == "__main__":
    raise SystemExit(main())
