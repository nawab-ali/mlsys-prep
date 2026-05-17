# Sources

This file defines the research standards for all study material in this repository. It
sets the source hierarchy, citation expectations, freshness rules, diagram policy, and
interview synthesis standards for the deep research phase.

The goal is to keep the curriculum deeply researched, current, technical, and useful for
senior and principal ML systems interviews at NVIDIA, OpenAI, and Anthropic.

## Source Hierarchy

Use the strongest available source for each claim. Prefer primary and durable sources
when a topic affects factual accuracy, architecture details, or interview preparation.

Tier 1:

- Official documentation, architecture whitepapers, product briefs, and standards.
- Public technical talks and papers from the primary authors or organizations.
- Primary-source material from NVIDIA, OpenAI, Anthropic, standards bodies, or authors.

Tier 2:

- Peer-reviewed papers, adopted arXiv papers, benchmark papers, and systems papers.
- Widely cited technical reports with clear methodology, limitations, and reproducibility.

Tier 3:

- Reputable engineering blogs, conference talks, vendor blogs, and production case studies.
- Use these for practical implementation context, operational lessons, and tradeoff framing.

Tier 4:

- Secondary explainers, tutorials, podcasts, newsletters, and informal posts.
- Tier 4 may help with intuition, but it should not be the main basis for factual claims.

## Preferred Sources By Topic

### LLM Fundamentals And Transformers

Prioritize foundational transformer papers, primary author explanations, high-quality
survey papers, and official documentation from major model providers when public. Use
modern sources to update terminology, scale assumptions, and production relevance.

### LLM Inference And Serving

Prioritize serving framework documentation, systems papers, production talks, and vendor
guides that explain scheduling, batching, KV cache behavior, latency, throughput, and cost.
Use primary sources for specific product or platform claims.

### LLM Training And Distributed Training

Prioritize distributed training papers, framework documentation, cluster architecture
talks, and credible production case studies. Focus on sources that explain parallelism,
optimizer state, activation memory, communication, failure modes, and scaling tradeoffs.

### Quantization And Low Precision

Prioritize papers, official hardware documentation, compiler documentation, and vendor
guides that describe numeric formats, Tensor Core support, calibration, accuracy, and
serving tradeoffs. Confirm claims about current formats before writing.

### RAG, Agents, VLMs, And Production Platforms

Prioritize primary model or platform documentation, systems papers, product architecture
talks, and production case studies. Treat fast-moving product details as current only after
checking recent public sources.

### Evaluation, Benchmarks, Reliability, And Safety

Prioritize benchmark papers, evaluation framework documentation, safety reports, and
public methodology notes. Distinguish benchmark facts from interpretation, limitations,
and interview-oriented synthesis.

### NVIDIA GPU Architecture And Platforms

Prioritize current NVIDIA architecture whitepapers, official product briefs, developer
documentation, conference talks, and public platform documentation. Avoid centering older
architectures except where they give necessary context.

### CUDA And NVIDIA Software Stack

Prioritize official CUDA documentation, NVIDIA library documentation, compiler materials,
developer guides, and public talks. Use framework documentation when explaining how model
systems map onto CUDA libraries or serving stacks.

### Scale-Up And Scale-Out GPU Systems

Prioritize NVIDIA platform documentation, networking documentation, systems papers, and
cluster design talks. Use sources that explain NVLink, NVSwitch, InfiniBand, Ethernet,
RDMA, collectives, topology, reliability, and operational tradeoffs.

### Performance Modeling And Accelerator Comparison

Prioritize foundational roofline sources, accelerator architecture papers, vendor
whitepapers, benchmark methodology papers, and careful technical reports. Keep comparisons
explicit about workload assumptions, bottlenecks, memory behavior, and software maturity.

### Behavioral And Leadership Preparation

Prioritize public company values, interview guidance from the target companies when
available, leadership frameworks, and the user's own verified experience. Separate public
company facts from synthesized positioning and story preparation.

## Freshness Policy

NVIDIA platform and software material must be checked against current public sources
before writing. Platform names, numeric formats, interconnect details, and software support
can change quickly.

OpenAI, Anthropic, and production LLM platform details must be checked against current
public sources before writing. Treat product behavior, model capabilities, and public API
details as time-sensitive.

Stable concepts such as transformers, attention, residual connections, and roofline
modeling can use foundational sources plus modern context. The modern context should make
clear what has changed in scale, deployment, hardware, or interview expectations.

If a claim may have changed recently, verify it before inclusion. When unsure, either
remove the claim, mark it as uncertain, or replace it with a more durable explanation.

## Citation Policy

Factual claims should cite sources. Derived explanations should cite the sources they are
based on, even when the final wording is original.

Interview guidance should distinguish between sourced facts and synthesis. It is fine to
add original interview framing, but the reader should be able to see where the factual
grounding ends and where interpretation begins.

Markdown files should include a `Sources` section when they contain researched technical
material. Prefer links to stable public pages, papers, official docs, or archived
references.

Do not cite low-quality sources for important claims when better sources exist. Use lower
tier sources only for intuition, context, or operational color that is not central to the
technical argument.

## Diagram Policy

Diagrams may be original explanatory diagrams created for this curriculum. Prefer Mermaid,
ASCII, or original simplified diagrams that render well on GitHub.

If a diagram is derived from a source, cite the source near the diagram. Do not copy
proprietary diagrams unless the license or source explicitly permits reuse.

Diagrams should simplify the concept without changing the factual meaning. If a diagram is
schematic rather than exact, say so in the surrounding text.

## Interview Synthesis Policy

Study material should connect facts to interview usefulness. Technical modules should make
clear why a topic matters for system design, debugging, performance, or leadership.

Each technical module should include `What interviewers may ask` and `How to answer at
senior/principal level` sections when appropriate.

The content should emphasize tradeoffs, bottlenecks, system design, hardware/software
co-design, performance modeling, and decision quality.

## Maintenance Policy

Source lists should be updated when material changes. Stale claims should be marked,
revised, or removed instead of silently carried forward.

Major content PRs should mention the research sources used. Reviews should check whether
the sources are current enough for the claims being added.

Markdown line length must remain below 120 characters in every file.

## Week 1 Sources

These sources support the Week 1 foundations content. They are the starting source set for
the first researched study modules, not the final bibliography for later weeks.

Current NVIDIA platform facts were checked against public NVIDIA sources on May 17, 2026.

No external figures are embedded in Week 1. The modules use original Mermaid diagrams and
Markdown tables derived from the sources listed below.

### LLM Foundations

- Vaswani et al., "Attention Is All You Need."
  https://arxiv.org/abs/1706.03762

- OpenAI Help Center, "What are tokens and how to count them?"
  https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them

- OpenAI API docs, "Key concepts."
  https://developers.openai.com/api/docs/concepts

- OpenAI API reference, "Completions."
  https://developers.openai.com/api/reference/resources/completions

### NVIDIA Platforms

- NVIDIA, "Blackwell Architecture."
  https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/

- NVIDIA, "GB200 NVL72."
  https://www.nvidia.com/en-us/data-center/gb200-nvl72/

- NVIDIA, "GB200 NVL Multi-Node Tuning Guide."
  https://docs.nvidia.com/multi-node-nvlink-systems/multi-node-tuning-guide/overview.html

- NVIDIA developer blog, "GB200 NVL72 Delivers Trillion-Parameter LLM Training."
https://developer.nvidia.com/blog/nvidia-gb200-nvl72-delivers-trillion-parameter-llm-training-and-real-time-inference/

- NVIDIA, "GB300 NVL72."
  https://www.nvidia.com/en-us/data-center/gb300-nvl72/

- NVIDIA developer blog, "Blackwell Ultra for the Era of AI Reasoning."
  https://developer.nvidia.com/blog/nvidia-blackwell-ultra-for-the-era-of-ai-reasoning/

- NVIDIA, "Vera Rubin Platform."
  https://www.nvidia.com/en-us/data-center/technologies/rubin/

- NVIDIA investor news, "NVIDIA Vera Rubin Opens Agentic AI Frontier."
  https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Opens-Agentic-AI-Frontier/default.aspx

### GPU Software Preview

- NVIDIA, "CUDA C++ Programming Guide."
  https://docs.nvidia.com/cuda/cuda-c-programming-guide/

- NVIDIA, "TensorRT-LLM Documentation."
  https://docs.nvidia.com/tensorrt-llm/

### LLM Serving Preview

- Kwon et al., "Efficient Memory Management for Large Language Model Serving."
  https://arxiv.org/abs/2309.06180

### Behavioral Positioning

- NVIDIA, "About Us."
  https://www.nvidia.com/en-us/about-nvidia/

- OpenAI, "OpenAI Charter."
  https://openai.com/charter/

- Anthropic, "Company."
  https://www.anthropic.com/company
