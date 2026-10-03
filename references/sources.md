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

## Week 2: GEMM Tiling Hierarchy

The seven-panel explanation in [NVIDIA GPU Execution Model](../nvidia/02_gpu_execution_model.md)
uses these primary NVIDIA sources:

- [CUTLASS Efficient GEMM in CUDA][gemm-efficient]: hierarchy diagram, mainloop, pipelining, and epilogue exchange.
- [CUTLASS GEMM API][gemm-api]: CTA/warp/thread operators, register fragments, and boundary predication.
- [CUTLASS: Fast Linear Algebra in CUDA C++][gemm-blog]: thread outer products and fused epilogue examples.
- [Matrix Multiplication Background User's Guide][gemm-background]: dimensions, output tiling, and reuse tradeoffs.
- [CUDA C++ Best Practices Guide][gemm-practices]: shared-memory reuse, synchronization, and coalesced accesses.
- [CUTLASS 3.0 Design][gemm-design] and [PTX ISA][gemm-ptx]: instruction scope and modern-architecture limitations.

Numerical tile sizes are an illustrative mapping, not a hardware specification or benchmark.
The original diagram's classic register hierarchy is not a universal Hopper or Blackwell operand path.

[gemm-efficient]: https://docs.nvidia.com/cutlass/4.2.1/media/docs/cpp/efficient_gemm.html
[gemm-api]: https://docs.nvidia.com/cutlass/4.2.1/media/docs/cpp/gemm_api.html
[gemm-blog]: https://developer.nvidia.com/blog/cutlass-linear-algebra-cuda/
[gemm-background]: https://docs.nvidia.com/deeplearning/performance/dl-performance-matrix-multiplication/index.html
[gemm-practices]: https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html
[gemm-design]: https://docs.nvidia.com/cutlass/4.2.1/media/docs/cpp/cutlass_3x_design.html
[gemm-ptx]: https://docs.nvidia.com/cuda/parallel-thread-execution/index.html

## Week 2: Decode Performance Case Study

[Applied Decode-Performance Case Study](../systems/02_decode_performance_case_study.md) uses
[NVIDIA's inference optimization guidance][decode-inference] for decode, batching, KV memory, and quantization.
The worked calculations and both figures use the exercise's explicit hypothetical assumptions.
They are not measured H100 performance, and a latency lower bound below the SLA does not guarantee compliance.

[decode-inference]: https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/

## Computer Architecture

Content basis: the computer-architecture material in the user-provided *Notes for Technical Interviews*,
PDF pages 74-217 (printed pages 73-216). The PDF is local source material, not a committed repository asset.

Coverage additions in [Computer Architecture](../computer_architecture/README.md) restore these teaching details:

- Dataflow operators and node state: PDF pages 75-76 and 114-115.
- Addressing modes: page 81; pipeline/frontend mechanisms: pages 93 and 97-101.
- Delay-slot limits, execution-unit pipelining, event timing, ROB operand reads, and Tomasulo memory paths:
  pages 98, 106, 109, 111, and 113.
- Cache placement and optimizations: pages 137-142; coherence transactions and filters: pages 146-151.
- DRAM transfer organization and scheduling: pages 158-163 and 168-172.
- Prefetching mechanisms, examples, and metric definitions: pages 178-189.
- Consistency and interconnect examples: pages 197-217.

The notes distinguish teaching assumptions from implementation guarantees. New network diagrams are simplified
reconstructions of the chapter's concepts; numerical illustrations are not hardware benchmark results.

### Figure Attribution

For this topic, prefer accurate, clearly licensed public artwork before creating a new diagram.
Captions in the study modules link to the original artwork and record author attribution, licenses, and adaptations.
The foundations dataflow graph uses [Dive into Deep Learning, Fig. 13.1.1][architecture-dataflow-source],
by Aston Zhang, Zachary C. Lipton, Mu Li, and Alexander J. Smola. Its
[CC BY-SA 4.0 license](../computer_architecture/assets/dataflow_model_license.txt) is retained beside the asset.
The vector labels, nodes, and arrows are unchanged; a white background was added for legibility.
The source depicts data dependencies in an imperative program; the module explains how a dataflow executor
can use the two independent branches concurrently, rather than claiming that the source Python code does so.
The foundations Von Neumann overview uses [Kapooht's Wikimedia Commons vector artwork][architecture-von-neumann],
licensed under [CC BY-SA 3.0][architecture-von-neumann-license]. It is rasterized at 2400 pixels wide on a white
background; the original labels, blocks, and arrows are unchanged. The module retains the detailed register and
fetch/execute explanation that the overview omits.
Public illustrations do not override the curriculum's topic coverage.
Numerical chapter prefixes are not used in headings.

Additional retained artwork restores mechanisms that broader replacement pictures did not show:

- The full ALU instruction path, vector-lane mapping, and conceptual warp
  scheduling reuse existing artwork from the approved local notes; no chapter heading or page furniture is retained.
- The crossbar matrix and H-tree/fat-tree panels reuse [CMU's interconnection-network lecture][architecture-networks].
  The crossbar is cropped; the tree panels are cropped and arranged side by side without changing their connections.

Worked encoding details use [RISC-V instruction listings][architecture-encodings]; cache-miss reference-model
qualifications use [CMU's memory-hierarchy lecture][arch-cache]. Prefetch locality hints are qualified against
[Intel's instruction reference][arch-prefetch-isa] and [intrinsic mapping][architecture-prefetch-hints].
Routing tradeoffs follow [CMU's routing discussion][architecture-routing]. Numerical teaching examples are not
vendor specifications.

The ISA scope and bit/byte/word addressability distinctions retain the approved notes' introductory coverage.
Plain-store versus base-register-writeback behavior is checked against
[Arm's store-instruction guidance][arch-arm-stores].

Historical result-in-ROB operand sourcing is checked against [Maryland's RiSC-oo teaching report][arch-rob-operands].
Tagged load results, store-data capture, and functional-unit overlap follow
[Edinburgh's HASE Tomasulo model][arch-tomasulo]. Event-delivery terminology and masking are qualified against
[Intel's system programming manual][arch-event-delivery]; urgent-event behavior is ISA/platform-specific.

[arch-rob-operands]: https://user.eng.umd.edu/~blj/risc/RiSC-oo.1.pdf
[arch-tomasulo]: https://www.icsa.inf.ed.ac.uk/research/groups/hase/models/tomasulo/tomasulo.html
[arch-event-delivery]: https://cdrdv2-public.intel.com/819714/253668-sdm-vol-3a.pdf
[architecture-dataflow-source]: https://d2l.ai/chapter_computational-performance/hybridize.html#fig-computegraph
[architecture-von-neumann]: https://commons.wikimedia.org/wiki/File:Von_Neumann_Architecture.svg
[architecture-von-neumann-license]: https://creativecommons.org/licenses/by-sa/3.0/
[architecture-networks]: https://www.cs.cmu.edu/afs/cs/academic/class/15418-s12/www/lectures/18_interconnects.pdf
[architecture-encodings]: https://docs.riscv.org/reference/isa/unpriv/rv-32-64g.html
[arch-cache]: https://www.cs.cmu.edu/afs/cs/academic/class/15740-s18/www/lectures/03-04-memory-hierarchy.pdf
[architecture-prefetch-hints]: https://www.intel.com/content/dam/develop/external/us/en/documents/18072-347603.pdf
[arch-prefetch-isa]: https://cdrdv2-public.intel.com/782151/253667-sdm-vol-2b.pdf
[architecture-routing]: https://www.cs.cmu.edu/afs/cs/academic/class/15740-f14/www/lectures/08-interconnect.pdf
[arch-arm-stores]: https://documentation-service.arm.com/static/680122175b1a8c5a27aa1aa7#page=18
