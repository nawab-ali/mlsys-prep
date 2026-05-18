# Three Month Plan

This three-month plan prepares Nawab Ali for ML systems interviews at NVIDIA, OpenAI,
and Anthropic. It emphasizes LLMs, latest NVIDIA GPU architecture, production inference
and training systems, performance modeling, hardware/software co-design, and behavioral
leadership.

The core principle is interleaving: LLM preparation and GPU preparation appear every week.
Each week also includes a bridge exercise, behavioral practice, and an assessment or
reflection checkpoint.

Expected time commitment: up to 10 hours per week, assuming five core sessions of up to
two hours each. The schedule is flexible because the learner is currently employed.

## Phase 1, Weeks 1-4: Foundations And Workload Intuition

Goals:

- Build a concise mental model of LLM architecture, inference, and workload shape.
- Refresh modern NVIDIA GPU platform concepts without dwelling on older architectures.
- Connect transformer operations to compute, memory, communication, and cost drivers.
- Establish a baseline career narrative and initial target-company positioning.

## Phase 2, Weeks 5-8: Production Systems, Low Precision, And Scaling

Goals:

- Compare training and inference systems from a practical production viewpoint.
- Study scale-up and scale-out GPU systems for modern LLM workloads.
- Organize low-precision, compression, and throughput tradeoffs at a high level.
- Practice leadership stories involving influence, reliability, and hard tradeoffs.

## Phase 3, Weeks 9-12: Advanced Systems Synthesis And Interview Readiness

Goals:

- Synthesize full-stack LLM platform design across models, serving, GPUs, and clusters.
- Prepare for RAG, agents, multimodal systems, evaluation, and reliability discussions.
- Apply performance modeling and accelerator comparison to interview-style cases.
- Finalize behavioral stories and company-specific positioning for the target roles.

Detailed study materials are pending the deep research phase.
## Required deep-dive topics

The plan must include explicit deep dives on two critical modern LLM systems
subjects:

1. Mixture of Experts.
2. Agents.

These topics should not be treated as side notes.

### Mixture of Experts

Mixture of Experts is introduced during the distributed-training phase and
covered deeply in Week 7.

The MoE deep dive should connect model architecture to systems consequences:

- Sparse activation and activated parameters.
- Router and gating behavior.
- Expert parallelism.
- Load balancing and capacity factor.
- Token dispatch, combine, overflow, and dropped-token behavior.
- All-to-all communication.
- Training instability and routing collapse.
- Inference serving, scheduling, batching, and memory implications.
- Hardware/software co-design implications for GPUs and custom accelerators.

### Agents

Agents are covered deeply in Week 9.

The agents deep dive should focus on production systems rather than hype:

- Tool calling and function calling.
- Planning and execution loops.
- RAG versus agents.
- Agent memory.
- Multi-agent systems.
- Guardrails, failure modes, and recovery.
- Latency and cost implications.
- Evaluation of agentic systems.
- Infrastructure impact for OpenAI, Anthropic, and NVIDIA-adjacent roles.

