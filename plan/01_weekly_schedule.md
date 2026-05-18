# Weekly Schedule

This file defines the high-level 12-week curriculum map.

The curriculum deliberately interleaves LLMs, NVIDIA GPU systems, systems bridge
topics, behavioral leadership, and assessments every week.

## 12-week interleaved outline

### Week 1: Foundations

- LLM focus: LLM basics, tokens, embeddings, and Transformer purpose.
- NVIDIA/GPU focus: latest NVIDIA platform landscape.
- Systems bridge: LLMs as matrix, memory, and communication workloads.
- Behavioral focus: career narrative and company positioning.
- Assessment: baseline diagnostic.

### Week 2: Transformer block and GPU execution

- LLM focus: Transformer block, attention, MLP, normalization, and residuals.
- NVIDIA/GPU focus: SMs, warps, Tensor Cores, HBM, and execution model.
- Systems bridge: mapping Transformer operations to GPU hardware.
- Behavioral focus: explaining complex architecture decisions.
- Assessment: conceptual quiz and whiteboard explanation.

### Week 3: Attention and memory pressure

- LLM focus: attention mechanics, causal masking, prefill, and decode.
- NVIDIA/GPU focus: memory hierarchy, HBM bandwidth, and on-chip storage.
- Systems bridge: attention, KV cache, and memory pressure.
- Behavioral focus: ambiguity and tradeoff stories.
- Assessment: inference bottleneck design drill.

### Week 4: Inference systems

- LLM focus: inference, decoding, sampling, batching, and serving metrics.
- NVIDIA/GPU focus: inference-oriented GPU performance bottlenecks.
- Systems bridge: latency, throughput, batch size, utilization, and cost.
- Behavioral focus: leadership under schedule pressure.
- Assessment: Month 1 technical midterm.

### Week 5: Training systems

- LLM focus: training pipeline, forward/backward pass, optimizers, and fine-tuning.
- NVIDIA/GPU focus: training workloads on modern NVIDIA GPUs.
- Systems bridge: compute, activation, gradient, and optimizer-state costs.
- Behavioral focus: cross-functional leadership.
- Assessment: training versus inference comparison.

### Week 6: Distributed training and MoE preview

- LLM focus: distributed training and parallelism, including MoE preview.
- NVIDIA/GPU focus: scale-up systems, NVLink, NVSwitch, and rack-scale platforms.
- Systems bridge: data, tensor, pipeline, sequence, and expert parallelism.
- Behavioral focus: influencing without authority.
- Assessment: distributed training design prompt.

### Week 7: Mixture of Experts deep dive

- LLM focus: MoE routing, experts, sparse activation, and load balance.
- NVIDIA/GPU focus: scale-out networking, RDMA, InfiniBand, Ethernet, and collectives.
- Systems bridge: MoE all-to-all, token dispatch, serving, and training bottlenecks.
- Behavioral focus: incident, postmortem, and reliability stories.
- Assessment: MoE systems design drill.

### Week 8: Quantization and low precision

- LLM focus: quantization, sparsity, distillation, compression, and low precision.
- NVIDIA/GPU focus: Tensor Cores, FP8, FP4, mixed precision, and software support.
- Systems bridge: accuracy, latency, throughput, memory, and cost tradeoffs.
- Behavioral focus: making hard technical tradeoffs.
- Assessment: Month 2 technical midterm.

### Week 9: Agents deep dive

- LLM focus: agents, tools, RAG, orchestration, memory, and guardrails.
- NVIDIA/GPU focus: CUDA stack, libraries, compilers, kernels, and serving frameworks.
- Systems bridge: agent systems, latency, cost, reliability, and GPU utilization.
- Behavioral focus: mentoring and technical leadership.
- Assessment: agent/RAG systems interview drill.

### Week 10: VLMs and multimodal systems

- LLM focus: VLMs and multimodal production systems.
- NVIDIA/GPU focus: capacity planning for mixed workloads and long contexts.
- Systems bridge: vision/text workload differences and serving implications.
- Behavioral focus: executive and non-expert communication.
- Assessment: multimodal architecture prompt.

### Week 11: Evaluation and accelerator comparison

- LLM focus: evaluation, benchmarks, hallucination, safety, and reliability.
- NVIDIA/GPU focus: roofline, bottleneck analysis, and accelerator comparison.
- Systems bridge: evaluating GPUs and custom accelerators for LLM workloads.
- Behavioral focus: conflict, disagreement, and decision quality.
- Assessment: accelerator evaluation case study.

### Week 12: Full-system synthesis

- LLM focus: full-stack production LLM system synthesis.
- NVIDIA/GPU focus: latest NVIDIA platform synthesis and cluster-level design.
- Systems bridge: end-to-end LLM platform design for target companies.
- Behavioral focus: final story bank and company positioning.
- Assessment: final mock interview loop.

## Explicit deep-dive guarantees

Two topics are now explicit deep dives rather than incidental mentions:

1. Mixture of Experts.
2. Agents.

## Mixture of Experts coverage

MoE is introduced in Week 6 and becomes a deep dive in Week 7.

The MoE material should cover:

- Dense versus sparse models.
- Experts, routers, and gating networks.
- Top-k expert selection.
- Activated parameters versus total parameters.
- Load balancing and capacity factor.
- Token dispatch and combine.
- Dropped tokens and overflow behavior.
- Expert parallelism.
- All-to-all communication.
- MoE training stability.
- MoE inference serving challenges.
- Memory, bandwidth, interconnect, and scheduling implications.
- Hardware/software co-design implications for GPUs and custom accelerators.

## Agents coverage

Agents become a deep dive in Week 9.

The agents material should cover:

- What an agent is and is not.
- Tool calling and function calling.
- Planning and execution loops.
- Short-term and long-term memory.
- RAG versus agents.
- Multi-agent systems.
- Guardrails and safety boundaries.
- Failure modes and recovery.
- Latency, cost, and serving implications.
- Agent evaluation.
- Production orchestration.
- Why agents matter for OpenAI and Anthropic interviews.
- How agentic systems change infrastructure requirements.
