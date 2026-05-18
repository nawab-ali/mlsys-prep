# Sources and Research Policy

This file defines the research standards for study material in this repository.

The goal is to keep interview preparation accurate, current, and grounded in
high-quality public sources.

## Source hierarchy

Use this hierarchy when writing technical material.

### Tier 1: primary and official sources

Examples:

- Official documentation.
- Architecture whitepapers.
- Product briefs.
- Standards.
- Public technical talks from primary organizations.
- Papers from primary authors or organizations.

Tier 1 sources should be preferred for factual claims about current platforms,
software, APIs, hardware, or product positioning.

### Tier 2: strong research sources

Examples:

- Peer-reviewed papers.
- arXiv papers with strong adoption.
- Benchmark papers.
- Systems papers.
- Widely cited technical reports.

Tier 2 sources are appropriate for algorithms, systems techniques, and
historical research context.

### Tier 3: reputable engineering sources

Examples:

- Engineering blogs.
- Conference talks.
- Vendor technical blogs.
- Production case studies.

Tier 3 sources can help connect concepts to production practice.

### Tier 4: secondary explainers

Examples:

- Tutorials.
- Informal posts.
- Podcasts.
- General explainers.

Tier 4 may help with intuition, but should not be the main basis for important
factual claims.

## Preferred sources by topic

### LLM fundamentals and Transformers

Prioritize foundational papers, high-quality lecture material, and primary
model architecture sources.

### LLM inference and serving

Prioritize systems papers, serving framework documentation, and production case
studies.

### LLM training and distributed training

Prioritize papers, official framework documentation, and public engineering
writeups from organizations operating large training systems.

### Quantization and low precision

Prioritize hardware vendor documentation, model optimization papers, and
framework documentation.

### RAG, agents, VLMs, and production platforms

Prioritize official platform documentation, systems papers, and reputable
engineering sources.

### Evaluation, benchmarks, reliability, and safety

Prioritize benchmark papers, official benchmark documentation, and high-quality
technical reports.

### NVIDIA GPU architecture and platforms

Prioritize NVIDIA official documentation, architecture pages, tuning guides,
developer blogs, and public technical presentations.

### CUDA and NVIDIA software stack

Prioritize NVIDIA documentation for CUDA, NCCL, TensorRT-LLM, cuBLAS, CUTLASS,
Triton-related integration notes, and official tuning guides.

### Scale-up and scale-out GPU systems

Prioritize NVIDIA platform documentation, networking documentation, systems
papers, and public cluster architecture material.

### Performance modeling and accelerator comparison

Prioritize roofline sources, architecture papers, vendor specifications, and
careful measurement methodology sources.

### Behavioral and leadership preparation

Use interview-prep synthesis grounded in the user's actual background. Do not
invent personal stories or metrics.

## Freshness policy

NVIDIA platform and software material must be checked against current public
sources before writing.

OpenAI, Anthropic, and production LLM platform details must be checked against
current public sources before writing.

Stable concepts such as Transformers, attention, and roofline modeling can use
foundational sources plus modern context.

If a claim may have changed recently, verify it before inclusion.

## Citation policy

Factual claims should cite sources.

Derived explanations should cite the sources they are based on.

Interview guidance should distinguish between sourced facts and synthesis.

Markdown files should include a Sources section when they contain researched
technical material.

Prefer stable public pages, official docs, papers, or archived references.

Do not cite low-quality sources for important claims when better sources exist.

## Diagram policy

Diagrams may be original explanatory diagrams.

If a diagram is derived from a source, cite the source near the diagram.

Do not copy proprietary diagrams unless reuse is clearly permitted.

Prefer Mermaid, ASCII, or original simplified diagrams that render well on
GitHub.

Embedded public figures are acceptable when the image is publicly available,
stable, and properly attributed. Do not merely link to a page when the visual is
central to the explanation.

## Interview synthesis policy

Study material should connect facts to interview usefulness.

Technical modules should include "What interviewers may ask" and "How to answer
at senior/principal level" sections when appropriate.

The content should emphasize tradeoffs, bottlenecks, system design, and
hardware/software co-design.

## Maintenance policy

Source lists should be updated when material changes.

Stale claims should be marked or revised.

Major content PRs should mention the research sources used.

Markdown line length must remain below 120 characters.

## Week 1 seed sources

### LLM foundations

- Vaswani et al., "Attention Is All You Need."
  <https://arxiv.org/abs/1706.03762>

### NVIDIA platforms

- NVIDIA, GB300 NVL72.
  <https://www.nvidia.com/en-us/data-center/gb300-nvl72/>

- NVIDIA, Blackwell Architecture.
  <https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/>

- NVIDIA, GB200 NVL72.
  <https://www.nvidia.com/en-us/data-center/gb200-nvl72/>

- NVIDIA, Grace Blackwell Multi-Node Tuning Guide.
  <https://docs.nvidia.com/multi-node-nvlink-systems/multi-node-tuning-guide/overview.html>

- NVIDIA, Blackwell Ultra technical blog.
  <https://developer.nvidia.com/blog/nvidia-blackwell-ultra-for-the-era-of-ai-reasoning/>

- NVIDIA, Vera Rubin Platform.
  <https://www.nvidia.com/en-us/data-center/technologies/rubin/>

- NVIDIA, Vera Rubin investor news.
<https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Opens-Agentic-AI-Frontier/default.aspx>

### GPU software preview

- NVIDIA, CUDA C++ Programming Guide.
  <https://docs.nvidia.com/cuda/cuda-c-programming-guide/>

- NVIDIA, TensorRT-LLM documentation.
  <https://docs.nvidia.com/tensorrt-llm/>

### LLM serving preview

- Kwon et al., "Efficient Memory Management for Large Language Model Serving
  with PagedAttention."
  <https://arxiv.org/abs/2309.06180>
