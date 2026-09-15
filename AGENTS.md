# AGENTS.md

## Repo Purpose

This repository contains ML systems interview preparation material, with a
focus on LLM systems, NVIDIA GPU platforms, systems design, and behavioral
interview prep.

## Working Rules

- Preserve the existing directory layout and filenames unless explicitly told
  otherwise.
- Keep Markdown structured, concise, and easy to scan.
- Keep Markdown lines under 120 characters where practical.
- Prefer direct, practical edits over broad rewrites.
- Do not introduce unrelated formatting churn.
- Use ASCII text unless the target file already clearly uses non-ASCII.

## Markdown Style

- Use clear heading hierarchy and avoid skipping heading levels.
- Prefer short paragraphs and parallel bullet lists.
- Keep tables readable in raw Markdown.
- Avoid decorative formatting that does not improve comprehension.
- Preserve existing section order unless the requested change requires moving
  material.

## Content Accuracy

- Treat existing repo files as the source of truth for this curriculum.
- Do not invent citations, benchmarks, product claims, or dates.
- Preserve technical nuance in ML systems, GPU architecture, and LLM serving
  content.
- If a factual claim is uncertain or likely time-sensitive, verify it before
  adding it.
- Keep references and source notes aligned with `references/sources.md`.

## File Organization

- Add new material to the existing topic directory when one fits.
- Do not create new top-level directories without explicit approval.
- Match the existing filename style: lowercase, descriptive, and
  underscore-separated.
- Keep navigation files such as `README.md` and directory `README.md` files in
  sync when adding or moving content.

## Links

- Use relative links for files inside the repo.
- Verify links when renaming, moving, or adding referenced files.
- Do not leave placeholder links unless explicitly requested.
- Prefer linking to canonical repo files instead of duplicating the same
  explanation in multiple places.

## Validation

- After Markdown edits, review changed files for broken headings, malformed
  lists, table damage, and obvious rendering problems.
- Check line length where practical.
- If the repo gains a Markdown linter or link checker, use it for documentation
  changes.

## Source-to-Markdown Audits

- Establish the exact source file, page range, repository commit, and audit
  scope before comparing content. The approved source governs import coverage.
- For an independent audit, reread the source and current files from scratch;
  do not use previous audit conclusions as evidence.
- Build the checklist from the source first, before reading the Markdown.
  Inventory every substantive explanation, equation, example, table, and
  diagram mechanism, with its source page.
- Compare every source page directly with the relevant Markdown. Matching
  headings or mentioning a topic does not establish complete coverage.
- Render and visually inspect every source page and repository diagram.
  Use OCR for image-embedded text, but verify formulas, labels, arrows, and
  worked examples visually rather than trusting extracted text alone.
- Record an exact repository location for each retained item. Classify other
  items as incomplete, missing, intentionally adapted, or incorrect.
  Do not treat shorter wording as missing content if it preserves the meaning.
- Check correctness separately from coverage. Verify calculations, code, and
  diagram semantics; check uncertain technical claims against primary sources.
- Finish the entire comparison before issuing the consolidated findings.
  Report findings with source pages and repository locations, and distinguish
  factual errors from coverage gaps and intentional adaptations.
- Do not declare the audit complete while any source item is unreviewed or
  unclassified. State inaccessible content, uncertainty, and testing limits
  explicitly; do not imply a guarantee that no issue can remain.
- After corrections, recheck the same inventory and affected surrounding
  content. Do not silently expand the scope or introduce new requirements.
- Keep working inventories outside the repository unless requested. An audit
  does not authorize collateral edits, commits, or new audit Markdown files.

## Branch And Git Workflow

- Work on the current feature branch unless asked to create or switch branches.
- Confirm the active branch before making multi-file or history-changing edits.
- Keep `main` clean and protected; do not rewrite it unless explicitly asked.
- Before destructive Git actions, verify status and explain what will happen.
- Use short, descriptive commit messages.
- Summarize changed files and intent clearly when creating PRs.

## Commit History Preferences

- The user prefers a clean, readable history.
- For major milestone cleanup, squash related prep work into a single clear
  commit when explicitly requested.
