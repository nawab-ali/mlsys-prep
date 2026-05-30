# LLM Topic Backlog

This file captures important LLM topics that are not yet part of the formal
study plan. Use it as a parking lot for topics to revisit and place into the
curriculum later.

## Topics to add later

- Mixture of Experts (MoE)
- Training
- Backpropagation
- RLHF
- DeepSeek
- Chain of Thought (CoT)
- Agents

## Portfolio project ideas

### Agentic Kernel Optimization Lab

Build an AI agent that takes a baseline kernel implementation and produces an
optimized version through an automated generate-test-benchmark-iterate loop.

The long-term goal is a general kernel optimization agent. Given a PyTorch,
Python, C++, or Triton baseline, the system should:

1. Infer the computation pattern.
2. Generate optimized candidate implementations.
3. Validate correctness.
4. Benchmark performance.
5. Analyze failures or bottlenecks.
6. Iterate until it produces a better implementation with a clear performance
   report.

The MVP should target a realistic subset of kernels:

- Elementwise operations
- Reductions
- Normalization kernels
- Layout transforms
- Simple matmul-like patterns

The system should prioritize correctness before speed. It should never accept
an optimization unless it passes tests.

Suggested implementation stack:

- LangGraph for the agent workflow
- Triton and C++ for generated kernels
- PyTorch for baselines and validation
- A benchmark harness for latency and speedup measurement

Development can happen locally on a MacBook Pro, but real benchmarking should
run on a cloud NVIDIA GPU.

This project is intended to showcase serious AI systems engineering: agentic
workflows, GPU programming, performance optimization, correctness validation,
benchmarking discipline, and clear technical reporting.
