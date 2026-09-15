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
