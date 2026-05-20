# Sources

This file defines the research and source standard for the ML systems interview
preparation repository.

It also records the source map for Week 1.

The goal is to keep the curriculum:

- accurate,
- current,
- interview-relevant,
- source-grounded,
- visually explainable,
- useful for senior and principal ML systems interviews.

## Source hierarchy

Use the strongest available source for each claim.

### Tier 1: primary sources

Use these whenever a claim affects technical correctness.

Examples:

- official NVIDIA documentation,
- official OpenAI documentation or technical reports,
- official Anthropic documentation or technical reports,
- architecture whitepapers,
- product briefs,
- standards documentation,
- primary research papers,
- public talks from primary authors or organizations.

### Tier 2: peer-reviewed or widely cited technical work

Use these for concepts, algorithms, and systems design.

Examples:

- peer-reviewed papers,
- widely cited arXiv papers,
- systems papers,
- benchmark papers,
- performance-modeling papers,
- reproducible technical reports.

### Tier 3: reputable engineering material

Use these for practical context and production lessons.

Examples:

- vendor engineering blogs,
- conference talks,
- production case studies,
- framework documentation,
- mature open-source project documentation.

### Tier 4: secondary explainers

Use these only for intuition.

Examples:

- tutorials,
- newsletters,
- podcasts,
- informal blog posts,
- summaries.

Tier 4 sources should not be the main basis for important factual claims.

## Citation rules

Every technical module should include a `Sources` section.

Use citations for:

- architecture claims,
- product claims,
- platform specifications,
- numeric values,
- benchmark claims,
- algorithm descriptions,
- named systems,
- fast-changing software or product details.

Do not cite a weak source when a stronger source exists.

Do not overstate what a source says.

If a claim is synthesis rather than a direct source fact, make that clear.

## Freshness rules

Some topics are stable. Others change quickly.

Stable topics can rely on foundational sources plus modern context.

Examples:

- Transformer basics,
- attention as a concept,
- autoregressive generation,
- roofline intuition,
- CUDA as a programming model,
- collective communication as a systems concept.

Fast-moving topics require recent public sources.

Examples:

- NVIDIA platform specifications,
- Blackwell and Blackwell Ultra details,
- Vera Rubin roadmap details,
- TensorRT-LLM features,
- OpenAI product behavior,
- Anthropic product behavior,
- model-serving frameworks,
- agent tooling,
- benchmark results.

If a claim may have changed recently, verify it before using it.

## Diagram and visual policy

Study modules should use visual explanations.

Good visuals include:

- Mermaid diagrams,
- ASCII diagrams,
- tables,
- simplified flowcharts,
- workload maps,
- bottleneck diagrams,
- platform stack diagrams.

Original diagrams are preferred when they explain the concept clearly.

If a diagram is derived from a source, cite the source near the diagram.

Do not copy proprietary diagrams unless reuse is clearly permitted.

If a diagram is schematic rather than exact, say so in the text.

## Interview synthesis policy

This repository is not a paper collection.

Each module should convert sources into interview-ready understanding.

A good module should include:

- the concept,
- why it matters,
- how it appears in systems,
- common misconceptions,
- senior-level answer patterns,
- diagrams or tables,
- self-check questions,
- sources.

The reader should be able to answer interview questions out loud after studying
the module.

## Week 1 source map

Week 1 uses the following source categories.

| Module | Source role |
| --- | --- |
| LLM fundamentals | Transformer basics and autoregressive generation |
| NVIDIA platforms | current NVIDIA platform and software documentation |
| LLM/GPU bridge | serving, KV cache, CUDA, NCCL, and roofline concepts |
| Behavioral strategy | original interview-prep synthesis |
| Week 1 quiz | synthesis from all Week 1 modules |

## Week 1: LLM fundamentals

Primary sources:

- Vaswani et al., "Attention Is All You Need."
  https://arxiv.org/abs/1706.03762

Recommended supporting sources:

- Stanford CS224N lecture materials.
  https://web.stanford.edu/class/cs224n/

- The Illustrated Transformer.
  https://jalammar.github.io/illustrated-transformer/

Use these sources for:

- Transformer motivation,
- token-to-logit mental model,
- attention as contextual mixing,
- autoregressive generation,
- common terminology.

## Week 1: Latest NVIDIA platforms

Primary NVIDIA sources:

- NVIDIA, "GB200 NVL72."
  https://www.nvidia.com/en-us/data-center/gb200-nvl72/

- NVIDIA, "GB300 NVL72."
  https://www.nvidia.com/en-us/data-center/gb300-nvl72/

- NVIDIA, "Blackwell Architecture."
  https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/

- NVIDIA Developer Blog, "NVIDIA Blackwell Ultra for the Era of AI Reasoning."
  https://developer.nvidia.com/blog/nvidia-blackwell-ultra-for-the-era-of-ai-reasoning/

- NVIDIA Docs, "NVIDIA GB200 NVL Multi-Node Tuning Guide."
  https://docs.nvidia.com/multi-node-nvlink-systems/multi-node-tuning-guide/overview.html

- NVIDIA Docs, "TensorRT-LLM."
  https://docs.nvidia.com/tensorrt-llm/

- NVIDIA Developer, "NVIDIA Collective Communications Library."
  https://developer.nvidia.com/NCCL

Use these sources for:

- GB200 NVL72,
- GB300 NVL72,
- Blackwell,
- Blackwell Ultra,
- NVLink and NVSwitch platform framing,
- TensorRT-LLM,
- NCCL,
- NVIDIA platform-stack vocabulary.

## Week 1: LLM and GPU bridge

Primary and technical sources:

- Vaswani et al., "Attention Is All You Need."
  https://arxiv.org/abs/1706.03762

- Kwon et al., "Efficient Memory Management for Large Language Model Serving
  with PagedAttention."
  https://arxiv.org/abs/2309.06180

- NVIDIA Docs, "TensorRT-LLM."
  https://docs.nvidia.com/tensorrt-llm/

- NVIDIA Docs, "CUDA C++ Programming Guide."
  https://docs.nvidia.com/cuda/cuda-c-programming-guide/

- NVIDIA Developer, "NVIDIA Collective Communications Library."
  https://developer.nvidia.com/NCCL

- Williams, Waterman, and Patterson, "Roofline: An Insightful Visual
  Performance Model for Multicore Architectures."
  https://crd.lbl.gov/assets/pubs_presos/roofline-sc09.pdf

Use these sources for:

- Transformer workload intuition,
- KV-cache serving pressure,
- CUDA execution context,
- collective communication,
- roofline intuition,
- compute, memory, and communication bottleneck framing.

## Week 1: Behavioral strategy

This module is original interview-prep synthesis.

It should be grounded in:

- the user's real experience,
- target company role expectations,
- senior and principal interview standards,
- demonstrated technical leadership,
- real metrics and outcomes.

Do not invent personal stories or metrics.

When finalizing behavioral answers, use only real experience and safe,
non-confidential descriptions.

## Week 1: Quiz

The Week 1 quiz is synthesis from the Week 1 modules.

It should test:

- LLM vocabulary,
- NVIDIA platform understanding,
- LLM/GPU bottleneck reasoning,
- behavioral positioning,
- senior-level synthesis.

The quiz answer key should not be treated as a script to memorize.

It should teach the shape of strong answers.

## Maintenance rules

When a module changes, update this file if the source basis changes.

When a new source is used, add it to the relevant module source map.

When a source becomes stale, either replace it or mark the claim as historical.

When a claim is uncertain, do not present it as fact.

When a module contains fast-moving platform information, prefer official current
sources.

## Markdown rules

All Markdown files should keep physical lines under 120 characters.

Use blank lines around headings, lists, tables, and code fences.

Prefer readable prose over compressed formatting.

Use tables when they improve comparison.

Use Mermaid diagrams when they improve conceptual understanding.

## Review checklist

Before calling a module gold standard, check:

- Does it teach the concept clearly?
- Does it include diagrams or tables where useful?
- Does it include senior-level answer patterns?
- Does it cite appropriate sources?
- Does it avoid unsupported claims?
- Does it distinguish fact from synthesis?
- Does it stay within the intended week scope?
- Does it help the reader answer interview questions out loud?

## Current Week 1 status

The Week 1 gold-standard content set is:

- `llms/01_llm_fundamentals.md`
- `nvidia/01_latest_nvidia_platforms.md`
- `systems/00_llm_gpu_bridge.md`
- `behavioral/00_behavioral_strategy.md`
- `assessments/weekly_quizzes/week_01_quiz.md`
- `references/sources.md`

Together, these files define the Week 1 baseline for future modules.
