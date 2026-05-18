# Week 1 Baseline Diagnostic

This diagnostic checks whether the Week 1 concepts are usable in interviews.

It is not a punitive exam. Its purpose is to identify weak areas early.

## Instructions

Use this diagnostic after completing the Week 1 modules.

For each question:

- Answer without notes first.
- Then check the answer key.
- Score yourself using the rubric.
- Log weak areas in `plan/04_progress_tracker.md`.
- Re-answer missed questions out loud.

## Scoring rubric

| Score | Meaning |
| ---: | --- |
| 0 | Not started |
| 1 | Familiar |
| 2 | Can explain |
| 3 | Can solve interview problems |
| 4 | Can teach and defend tradeoffs |

Use score 3 as the practical interview-readiness target for Week 1.

## Part A: LLM fundamentals

1. What is an LLM?
2. What is the difference between a token and a word?
3. What is a token ID?
4. What is an embedding?
5. What are logits?
6. How does autoregressive generation work?
7. Why is "next-token predictor" useful but incomplete?
8. Why did Transformers become dominant?
9. Why is an LLM not a database?
10. What is the difference between training and inference?

## Part B: NVIDIA platform landscape

1. Why is NVIDIA's advantage more than the GPU chip?
2. What role does HBM play in LLM systems?
3. Why does NVLink matter?
4. What is GB200 NVL72 at a high level?
5. What is GB300 NVL72 at a high level?
6. How should Vera Rubin be discussed in interviews?
7. Why does CUDA matter to the platform?
8. What should you memorize versus reason from?

## Part C: LLM and GPU bridge

1. What are the three recurring bottleneck questions?
2. Why are LLMs matrix workloads?
3. Why are LLMs memory workloads?
4. Why are LLMs communication workloads?
5. What is prefill?
6. What is decode?
7. Why does KV cache matter?
8. Why is peak FLOPS insufficient for accelerator comparison?

## Part D: Behavioral positioning

1. Give your 30-second career narrative.
2. Give your two-minute career narrative.
3. Explain why NVIDIA is a fit.
4. Explain why OpenAI or Anthropic could be a fit.
5. Describe one architecture tradeoff story.
6. Describe one cross-functional leadership story.

## Part E: Design prompt

You are asked to evaluate a new accelerator for LLM inference. The team claims
it has very high peak TOPS but provides little information about memory bandwidth
or interconnect.

Explain what questions you would ask before trusting the performance claim.

## Answer key: Part A

### A1: What is an LLM?

Expected answer:

> An LLM is a neural network trained on tokenized data to model sequences. In
> the autoregressive case, it maps previous tokens to logits over the next token.

Senior/principal signal:

- Mentions tokens, logits, decoding, and system workload implications.

Red flags:

- Says only "chatbot."
- Says "predicts words" without clarifying tokens.
- Treats the model as a database.

### A2: Token versus word

Expected answer:

> A token is a tokenizer-produced symbol. It may be a word, part of a word,
> punctuation, whitespace, or special symbol.

Senior/principal signal:

- Connects token count to context length, memory, and compute.

Red flags:

- Assumes one token always equals one word.

### A3: Token ID

Expected answer:

> A token ID is an integer vocabulary index used to look up an embedding.

Senior/principal signal:

- Explains that the numeric value is not semantically meaningful as a scalar.

Red flags:

- Treats token IDs as continuous model inputs.

### A4: Embedding

Expected answer:

> An embedding is a learned dense vector associated with a token ID.

Senior/principal signal:

- Connects embeddings to hidden size and activation footprint.

Red flags:

- Confuses embeddings with one-hot vectors.

### A5: Logits

Expected answer:

> Logits are unnormalized scores over candidate next tokens.

Senior/principal signal:

- Mentions decoding policy and probability conversion.

Red flags:

- Calls logits probabilities directly.

### A6: Autoregressive generation

Expected answer:

> The model predicts a next token, appends it to the context, and repeats.

Senior/principal signal:

- Mentions prefill and decode as later system-level phases.

Red flags:

- Describes generation as retrieving a stored answer.

### A7: Next-token predictor is incomplete

Expected answer:

> It describes the base mechanism but not alignment, tool use, RAG,
> multimodality, evaluation, or emergent behavior.

Senior/principal signal:

- Uses the simple model while identifying its limits.

Red flags:

- Treats next-token prediction as either everything or nothing.

### A8: Transformer dominance

Expected answer:

> Transformers combine strong sequence modeling with dense operations that scale
> well on accelerator hardware.

Senior/principal signal:

- Mentions attention, MLPs, parallelism, and dense linear algebra.

Red flags:

- Says only "attention is powerful."

### A9: LLM is not a database

Expected answer:

> A database stores explicit records. An LLM generates from learned parameters
> and context and can hallucinate.

Senior/principal signal:

- Mentions RAG as an external retrieval path.

Red flags:

- Says the model looks up facts in weights like rows.

### A10: Training versus inference

Expected answer:

> Training updates weights using forward, backward, and optimizer steps.
> Inference uses fixed weights to generate outputs.

Senior/principal signal:

- Connects training to activations, gradients, optimizer state, and
> synchronization; connects inference to latency, throughput, and KV cache.

Red flags:

- Treats them as the same workload.

## Answer key: Part B

Expected themes:

- NVIDIA's platform includes GPUs, HBM, Tensor Cores, NVLink, NVSwitch,
  networking, CUDA, libraries, and serving software.
- GB200 is an important Grace Blackwell anchor.
- GB300 is the current Blackwell Ultra anchor in this curriculum.
- Vera Rubin is forward-looking public roadmap context.
- HBM affects model fit, bandwidth, and KV-cache behavior.
- NVLink matters for scale-up communication.
- CUDA and libraries make hardware capability usable.

Senior/principal signal:

- Explains compute, memory, communication, and software as a balanced system.

Common red flags:

- Says only "faster GPUs."
- Ignores software.
- Overstates roadmap systems as current deployed baselines.
- Memorizes SKU names without bottleneck reasoning.

## Answer key: Part C

Expected themes:

- The three bottleneck questions are compute, memory, and communication.
- Matrix workloads come from projections, MLPs, and GEMM-like operations.
- Memory pressure comes from weights, activations, and KV cache.
- Communication appears in tensor parallelism, pipeline parallelism, data
  parallelism, and multi-node execution.
- Prefill processes prompt tokens.
- Decode generates output tokens step by step.
- KV cache stores attention state and can limit serving throughput.
- Peak FLOPS is insufficient without memory, interconnect, software, and
  workload shape.

Senior/principal signal:

- Separates prefill, decode, training, and serving bottlenecks.

Common red flags:

- Uses a single bottleneck for every scenario.
- Ignores latency and utilization.
- Ignores communication.

## Answer key: Part D

Strong behavioral answers should include:

- Scope.
- Constraint.
- Action.
- Tradeoff.
- Outcome.
- Reflection.
- Relevance to the target company.

Common red flags:

- Vague impact.
- No metrics.
- No tradeoff.
- Blaming others.
- Overclaiming LLM research expertise.

## Answer key: Part E

A strong design answer should ask about:

- Target model sizes.
- Batch sizes.
- Context lengths.
- Prefill versus decode split.
- Weight precision.
- Activation precision.
- KV-cache capacity.
- HBM capacity and bandwidth.
- Interconnect bandwidth and latency.
- Kernel availability.
- Software stack maturity.
- Latency and throughput targets.
- Power and cost constraints.
- Comparison baseline.
- Real workload traces.

Senior/principal signal:

- Refuses to evaluate peak TOPS in isolation.
- Defines workload assumptions first.
- Separates compute-bound and memory-bound regimes.
- Asks for measurement methodology.

Red flags:

- Accepts peak TOPS as enough.
- Ignores memory bandwidth.
- Ignores interconnect.
- Ignores software and batching.

## Progress reflection

After the diagnostic, fill this table.

| Area | Score | Weak point | Next action |
| --- | ---: | --- | --- |
| LLM fundamentals |  |  |  |
| NVIDIA platforms |  |  |  |
| LLM/GPU bridge |  |  |  |
| Behavioral positioning |  |  |  |
| Design reasoning |  |  |  |

Then update `plan/04_progress_tracker.md`.
