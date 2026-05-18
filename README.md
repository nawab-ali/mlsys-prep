# mlsys-prep

Deep ML systems interview preparation for roles at NVIDIA, OpenAI, and
Anthropic.

This repository is a structured three-month preparation program focused on:

- LLM fundamentals and production LLM systems.
- Latest NVIDIA GPU platforms and GPU systems.
- The bridge between LLM workloads and hardware architecture.
- Performance modeling and accelerator comparison.
- Behavioral and technical leadership interviews.

## Start here

Begin with the Week 1 materials in this order:

1. [LLM Fundamentals](llms/01_llm_fundamentals.md)
2. [Latest NVIDIA Platforms](nvidia/01_latest_nvidia_platforms.md)
3. [LLM and GPU Bridge](systems/00_llm_gpu_bridge.md)
4. [Behavioral Strategy](behavioral/00_behavioral_strategy.md)
5. [Week 1 Baseline Diagnostic](assessments/weekly_quizzes/week_01_quiz.md)
6. [Progress Tracker](plan/04_progress_tracker.md)

Use the diagnostic after reading the first four files. Then log weak areas in
the progress tracker.

## Current status

Week 1 is the first complete content module. It is intended to become the gold
standard for future weeks.

| Area | Status |
| --- | --- |
| Repository scaffold | Complete |
| 12-week interleaved curriculum outline | Complete |
| Research and source policy | Complete |
| Week 1 study materials | In review |
| Week 2-12 study materials | Not started |

## How to use this repository

Each week is designed to interleave four tracks:

1. LLM concepts.
2. NVIDIA GPU or GPU systems concepts.
3. Systems bridge topics that connect models to hardware.
4. Behavioral and leadership preparation.

Do not study all LLM material first and GPU material later. The curriculum is
designed so that the model concepts and hardware concepts reinforce each other.

## Week 1 study flow

| Step | File | Purpose |
| ---: | --- | --- |
| 1 | [LLM Fundamentals](llms/01_llm_fundamentals.md) | Build the base LLM vocabulary. |
| 2 | [Latest NVIDIA Platforms](nvidia/01_latest_nvidia_platforms.md) | Learn the current NVIDIA platform map. |
| 3 | [LLM and GPU Bridge](systems/00_llm_gpu_bridge.md) | Connect LLM behavior to hardware bottlenecks. |
| 4 | [Behavioral Strategy](behavioral/00_behavioral_strategy.md) | Build your senior-level career narrative. |
| 5 | [Week 1 Baseline Diagnostic](assessments/weekly_quizzes/week_01_quiz.md) | Test the Week 1 concepts. |
| 6 | [Progress Tracker](plan/04_progress_tracker.md) | Record weak areas and next actions. |

## Three-month structure

| Phase | Weeks | Theme |
| --- | ---: | --- |
| Phase 1 | 1-4 | Foundations and workload intuition |
| Phase 2 | 5-8 | Production systems, low precision, and scaling |
| Phase 3 | 9-12 | Advanced systems synthesis and interview readiness |

The detailed schedule lives in:

- [Three-Month Plan](plan/00_three_month_plan.md)
- [Weekly Schedule](plan/01_weekly_schedule.md)
- [Daily Schedule](plan/02_daily_schedule.md)
- [Flex and Catch-Up Policy](plan/03_flex_and_catchup_policy.md)

## Repo map

| Directory | Purpose |
| --- | --- |
| [docs](docs/) | Overview and usage instructions. |
| [plan](plan/) | Three-month plan, schedules, flexibility, and progress tracking. |
| [llms](llms/) | LLM concepts and production LLM systems. |
| [nvidia](nvidia/) | NVIDIA GPU platforms, architecture, and software stack. |
| [systems](systems/) | LLM/GPU bridge, bottleneck analysis, and system design. |
| [behavioral](behavioral/) | Behavioral and leadership interview preparation. |
| [assessments](assessments/) | Weekly quizzes, midterms, and mock interviews. |
| [diagrams](diagrams/) | Mermaid diagrams and visual assets. |
| [references](references/) | Source policy, bibliography, and glossary. |

## Quality bar

Every real study module should include:

- Accurate, current, source-grounded technical content.
- Visual explanations using Mermaid diagrams, tables, or embedded public figures.
- Interview-focused explanations, not just textbook summaries.
- Senior/principal-level answer patterns.
- Clear links between model behavior, hardware bottlenecks, and system tradeoffs.
- Markdown lines under 120 characters.

## Source policy

The research and citation policy lives in:

- [Sources and Research Policy](references/sources.md)

Use that file to understand how future modules should be researched, cited, and
reviewed.

## Development workflow

Main stays stable. New content should be added through reviewed pull requests:

```text
new branch -> validate -> pull request -> review -> merge
```

Do not push directly to `main`.
