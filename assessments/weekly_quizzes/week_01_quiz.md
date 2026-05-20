# Week 1 Quiz

This assessment checks whether Week 1 material is usable in interview settings.

It covers:

- LLM fundamentals.
- Latest NVIDIA platforms.
- The LLM/GPU systems bridge.
- Behavioral strategy.
- Senior-level synthesis.

This quiz is not a memory test. It is a diagnostic for interview readiness.

## How to use this quiz

Use this sequence:

1. Answer without notes.
2. Score yourself with the rubric.
3. Review the answer key.
4. Mark weak areas in the progress tracker.
5. Repeat missed questions out loud.

Recommended time:

| Section | Time |
| --- | ---: |
| LLM fundamentals | 20 minutes |
| NVIDIA platforms | 25 minutes |
| LLM/GPU bridge | 30 minutes |
| Behavioral strategy | 25 minutes |
| Senior synthesis | 30 minutes |

Total time: about two hours.

## Scoring rubric

Use this 0 to 4 scale.

| Score | Meaning |
| ---: | --- |
| 0 | Cannot answer or answer is mostly wrong |
| 1 | Knows vocabulary but cannot explain clearly |
| 2 | Gives a mostly correct basic answer |
| 3 | Gives a clear interview-ready answer with tradeoffs |
| 4 | Gives a senior-level answer with assumptions and caveats |

Week 1 target:

```text
Average score >= 3.0
No critical topic below 2.0
At least two synthesis answers at 3.0 or higher
```

If a topic scores below 2.0, review the corresponding study file before moving
to Week 2.

## Section 1: LLM fundamentals

### Question 1

Explain the flow from user text to next-token generation.

Your answer should include:

- tokens,
- token IDs,
- embeddings,
- Transformer layers,
- logits,
- decoding,
- autoregressive repetition.

### Question 2

What is a token?

Explain why tokens are not always the same as words.

### Question 3

What are logits?

Explain where they appear in the LLM generation pipeline.

### Question 4

What does autoregressive generation mean?

Explain why this matters for latency and serving.

### Question 5

What is the purpose of a Transformer block?

Do not go deep into attention math yet. Give the Week 1 mental model.

### Question 6

Explain the difference between training and inference.

Your answer should mention:

- forward pass,
- backward pass,
- gradients,
- optimizer state,
- serving latency,
- token generation.

### Question 7

What is a common misconception about LLMs that a senior interviewer might test?

Give the misconception and the corrected explanation.

### Question 8

Give a 60-second answer to:

```text
What is an LLM?
```

## Section 2: Latest NVIDIA platforms

### Question 9

Why is NVIDIA's advantage platform-level rather than only GPU-level?

Your answer should include hardware and software.

### Question 10

What is GB200 NVL72?

Give a Week 1-level explanation.

### Question 11

What is GB300 NVL72?

Explain why it is relevant for reasoning and long-context inference.

### Question 12

What is Blackwell Ultra?

How should it be framed relative to Blackwell?

### Question 13

Why does HBM matter for LLM workloads?

Mention at least three memory consumers.

### Question 14

Explain scale-up versus scale-out in NVIDIA AI systems.

Give examples of technologies associated with each.

### Question 15

What does NCCL contribute?

Explain why communication libraries matter for multi-GPU workloads.

### Question 16

What does TensorRT-LLM contribute?

Explain why inference software is part of the platform story.

### Question 17

Why is peak FLOPS insufficient for evaluating an NVIDIA platform?

Give at least four other factors.

### Question 18

Give a senior-level answer to:

```text
Why does NVLink matter for LLM systems?
```

## Section 3: LLM/GPU bridge

### Question 19

Translate these model terms into systems terms:

| Model term | Systems interpretation |
| --- | --- |
| token | |
| weight | |
| activation | |
| KV cache | |
| batch | |
| context length | |

### Question 20

Explain the compute, memory, and communication triangle.

Why is it useful for LLM systems interviews?

### Question 21

Why are prefill and decode different?

Your answer should mention parallelism, sequential dependency, and KV cache.

### Question 22

A serving system has good prefill throughput but poor decode throughput.

List five questions you would ask before proposing a fix.

### Question 23

A model spans multiple GPUs. Single-GPU kernels are fast, but end-to-end latency
does not scale well.

What are the likely causes?

### Question 24

What is KV cache?

Explain both why it helps and why it creates pressure.

### Question 25

Explain why a GPU can have high peak FLOPS but poor tokens per second for a
specific serving workload.

### Question 26

A vendor claims their accelerator has much higher TOPS than an NVIDIA GPU.

What information do you need before believing the claim?

### Question 27

Explain scale-up communication pressure in one paragraph.

### Question 28

Explain scale-out communication pressure in one paragraph.

## Section 4: Behavioral strategy

### Question 29

Give your 30-second career narrative.

It should follow:

```text
past depth -> current focus -> target fit
```

### Question 30

Give your two-minute career narrative.

It should connect hardware architecture to LLM systems.

### Question 31

Give a Week 1 answer to:

```text
Why NVIDIA?
```

### Question 32

Give a Week 1 answer to:

```text
Why OpenAI?
```

### Question 33

Give a Week 1 answer to:

```text
Why Anthropic?
```

### Question 34

Name eight candidate stories for your behavioral story bank.

For each story, state what signal it proves.

### Question 35

Explain STAR plus tradeoff.

Why is plain STAR not enough for senior interviews?

### Question 36

Pick one architecture tradeoff story.

List:

- situation,
- task,
- action,
- result,
- tradeoff,
- reflection,
- missing metrics.

### Question 37

Pick one failure or mistake story.

What did you learn and what changed afterward?

### Question 38

What are three behavioral red flags you must avoid?

## Section 5: Senior synthesis

### Question 39

You are asked to evaluate a new GPU platform for LLM inference.

Give a structured answer.

Your answer should cover:

- workload phase,
- model size,
- context length,
- batch size,
- precision,
- HBM capacity,
- HBM bandwidth,
- KV cache,
- interconnect,
- software stack,
- latency,
- cost per token.

### Question 40

You are asked why a reasoning model costs more to serve.

Give a systems answer.

### Question 41

You are asked whether a model should be split across GPUs.

What questions do you ask before answering?

### Question 42

You are asked to explain LLM serving to an executive.

Give a concise non-jargon answer.

### Question 43

You are asked to compare NVIDIA and a custom accelerator.

Give a balanced answer without sounding like marketing.

### Question 44

You are asked why your hardware background is relevant to OpenAI or Anthropic.

Give a senior-level answer.

### Question 45

You are debugging a production LLM latency regression.

Give your first five steps.

## Answer key

Use the answer key to score quality, not word-for-word similarity.

## Section 1 answer key

### Answer 1

A strong answer:

> User text is split into tokens. Tokens are mapped to token IDs. Token IDs are
> converted into embeddings. Embeddings pass through Transformer layers. The
> model outputs logits over the vocabulary. A decoding policy selects the next
> token. The new token is appended to the context, and the process repeats.

Senior signal:

- Mentions tensors, not just text.
- Mentions autoregressive repetition.
- Separates logits from decoded tokens.

### Answer 2

A token is a unit used by the model's tokenizer.

Tokens can be:

- whole words,
- parts of words,
- punctuation,
- whitespace-related pieces,
- special symbols.

Words and tokens differ because tokenizers optimize for vocabulary coverage and
statistical reuse, not human word boundaries.

### Answer 3

Logits are raw output scores before probability normalization or sampling.

They appear after the model processes the current context and before decoding
selects the next token.

A good answer distinguishes:

```text
logits -> probabilities or scores -> decoding choice -> next token
```

### Answer 4

Autoregressive generation means the model generates one token at a time, using
previous tokens as context for the next token.

This matters because decode has a sequential dependency. It can make serving
latency-sensitive even when prefill is highly parallel.

### Answer 5

A Transformer block repeatedly transforms token representations.

At Week 1 level, it combines:

- attention-like mixing across sequence positions,
- MLP computation,
- residual paths,
- normalization,
- learned weights.

The purpose is to update token representations using context.

### Answer 6

Training learns weights. Inference uses learned weights.

Training includes forward pass, backward pass, gradients, optimizer state, and
large memory pressure. Inference focuses on serving prompts, generating tokens,
latency, throughput, batching, and cost.

### Answer 7

Example misconception:

> LLMs understand text the way humans do.

Correction:

> LLMs operate on tokens and tensors. They learn statistical patterns in data and
> generate next-token predictions. Their behavior can look like reasoning, but
> systems design must treat them as tensor programs with memory, compute, and
> communication costs.

### Answer 8

A strong 60-second answer:

> An LLM is a neural network trained to map token sequences to predictions over
> the next token. In modern systems, it is usually a Transformer-based model.
> Text is tokenized, token IDs become embeddings, and Transformer layers produce
> logits over possible next tokens. Generation is autoregressive, so each output
> token is fed back into the context. From a systems view, an LLM is a workload
> involving dense matrix math, memory movement, KV-cache behavior, batching, and
> sometimes multi-GPU communication.

## Section 2 answer key

### Answer 9

NVIDIA's advantage is platform-level because performance depends on more than
the GPU chip.

A complete answer mentions:

- Tensor Cores,
- HBM,
- NVLink and NVSwitch,
- InfiniBand or Ethernet,
- CUDA,
- NCCL,
- TensorRT-LLM,
- libraries,
- tools,
- ecosystem maturity.

### Answer 10

GB200 NVL72 is a Grace Blackwell rack-scale system.

Week 1 answer:

> It combines Grace CPUs and Blackwell GPUs into a rack-scale NVLink domain. It
> is important because it shows NVIDIA treating the rack as a tightly coupled
> AI compute platform rather than a pile of independent GPUs.

### Answer 11

GB300 NVL72 is the Blackwell Ultra rack-scale system.

A strong answer:

> GB300 NVL72 integrates Blackwell Ultra GPUs and Grace CPUs for reasoning,
> long-context, and test-time scaling workloads. It matters because these
> workloads can increase memory pressure, attention pressure, and serving cost.

### Answer 12

Blackwell Ultra should be framed as a platform refresh aimed at reasoning,
long-context inference, post-training, and test-time compute.

Do not describe it merely as "a faster Blackwell."

### Answer 13

HBM matters because LLMs need memory for:

- weights,
- activations,
- KV cache,
- temporary buffers,
- gradients during training,
- optimizer state during training.

For inference, KV cache and concurrent users can make memory capacity and
bandwidth central.

### Answer 14

Scale-up connects GPUs into a tightly coupled domain.

Examples:

- NVLink,
- NVSwitch,
- NVLink Switch.

Scale-out connects nodes or racks.

Examples:

- InfiniBand,
- Ethernet,
- RDMA,
- ConnectX,
- NCCL across nodes.

### Answer 15

NCCL provides optimized collective communication across GPUs and nodes.

It matters because distributed LLM training and multi-GPU inference rely on
patterns such as all-reduce, all-gather, reduce-scatter, and broadcast.

### Answer 16

TensorRT-LLM contributes optimized inference execution for LLMs.

It matters because inference performance depends on kernels, graph execution,
batching support, precision support, and integration with serving systems.

### Answer 17

Peak FLOPS is insufficient because real performance can be limited by:

- memory capacity,
- memory bandwidth,
- KV-cache traffic,
- interconnect bandwidth,
- collective overhead,
- batch size,
- latency target,
- kernel maturity,
- software stack,
- precision support,
- scheduling.

### Answer 18

A strong answer:

> NVLink matters when a model or serving workload spans multiple GPUs. Tensor
> parallelism, expert parallelism, and large-model inference can require
> frequent GPU-to-GPU communication. NVLink and NVSwitch create a high-bandwidth
> scale-up domain that reduces the penalty of splitting work across GPUs.

## Section 3 answer key

### Answer 19

Expected mapping:

| Model term | Systems interpretation |
| --- | --- |
| token | sequence unit processed by the model |
| weight | learned tensor stored in memory |
| activation | intermediate tensor produced during execution |
| KV cache | stored attention state used during decode |
| batch | multiple sequences or requests grouped together |
| context length | sequence length driving attention and KV-cache footprint |

### Answer 20

The compute, memory, and communication triangle is a bottleneck framework.

It prevents weak answers that focus only on FLOPS. It asks whether the workload
is limited by math throughput, data movement, or device-to-device communication.

### Answer 21

Prefill processes prompt tokens and has more parallel work across the input
sequence. Decode generates one token at a time and has a sequential dependency.

Decode often stresses KV-cache reads and writes, latency, and scheduling.

### Answer 22

Good questions:

- What is the decode batch size?
- What is the context length?
- How large is the KV cache?
- Is HBM bandwidth saturated?
- Are decode kernels optimized?
- Can requests be batched without violating latency?
- Are prefill and decode scheduled separately?
- Is the bottleneck memory, compute, or scheduler overhead?

### Answer 23

Likely causes:

- tensor-parallel collectives,
- pipeline bubbles,
- poor compute and communication overlap,
- NVLink or network saturation,
- small tensor shapes,
- NCCL overhead,
- load imbalance,
- synchronization on the critical path.

### Answer 24

KV cache stores prior keys and values so decode does not recompute attention
state for all earlier tokens.

It helps efficiency, but it consumes memory and can stress memory bandwidth,
especially for long context and many concurrent users.

### Answer 25

High peak FLOPS may not translate to high tokens per second because decode can
be sequential, small-batch, memory-sensitive, and latency-constrained.

The math units may not be fully fed.

### Answer 26

Ask for:

- model,
- phase,
- batch size,
- context length,
- precision,
- memory capacity,
- memory bandwidth,
- interconnect,
- software stack,
- latency,
- throughput,
- cost per token,
- benchmark methodology.

### Answer 27

Scale-up communication pressure happens when GPUs in a tightly coupled domain
must frequently exchange tensors, partial results, or activations. Tensor
parallelism and expert parallelism can create collectives or dispatch paths
where NVLink, NVSwitch, and NCCL become critical.

### Answer 28

Scale-out communication pressure happens when nodes or racks coordinate work.
Multi-node training may need gradient synchronization, checkpointing, and
collectives across InfiniBand or Ethernet. Network bandwidth, latency,
congestion, and reliability can affect scaling efficiency.

## Section 4 answer key

### Answer 29

A strong 30-second narrative includes:

- senior ML hardware architecture,
- custom AI silicon,
- performance modeling,
- hardware/software co-design,
- current focus on LLM systems,
- fit for model, GPU, and infrastructure tradeoffs.

### Answer 30

A strong two-minute narrative connects:

- architecture background,
- workload analysis,
- performance modeling,
- co-design,
- current LLM systems focus,
- target company fit,
- desire to work across accelerators and production systems.

### Answer 31

A strong NVIDIA answer emphasizes:

- platform thinking,
- GPU systems,
- performance,
- CUDA ecosystem,
- LLM workloads,
- architecture fit,
- customer impact.

It should not say only "NVIDIA has fast GPUs."

### Answer 32

A strong OpenAI answer emphasizes:

- production LLM systems,
- training and inference infrastructure,
- hardware/software boundary,
- cost,
- latency,
- reliability,
- full-stack systems impact.

### Answer 33

A strong Anthropic answer emphasizes:

- careful systems engineering,
- reliability,
- principled tradeoffs,
- evaluation,
- infrastructure for useful AI systems,
- humility under uncertainty.

### Answer 34

Good story-bank categories:

- architecture tradeoff,
- performance modeling,
- hardware/software co-design,
- ambiguous roadmap decision,
- cross-functional conflict,
- failure or mistake,
- execution under pressure,
- mentoring,
- debugging,
- product or customer impact.

### Answer 35

STAR plus tradeoff adds tradeoff and reflection to situation, task, action, and
result.

Plain STAR can describe what happened. Senior interviews need to know why the
decision was hard, what was sacrificed, what evidence was used, and what the
candidate learned.

### Answer 36

A strong answer should identify:

- the project,
- the decision,
- alternatives,
- your role,
- evidence,
- result,
- tradeoff,
- what metric is missing.

### Answer 37

A strong failure story should avoid blame.

It should show:

- initial assumption,
- evidence that disproved it,
- corrective action,
- communication,
- changed future behavior.

### Answer 38

Red flags include:

- vague impact,
- no metrics,
- blaming others,
- overclaiming,
- too much jargon,
- no reflection,
- ignoring software,
- ignoring product impact.

## Section 5 answer key

### Answer 39

A strong answer starts by clarifying the workload.

Then it covers:

- training versus inference,
- prefill versus decode,
- model size,
- context length,
- batch size,
- precision,
- HBM capacity,
- HBM bandwidth,
- KV cache,
- NVLink and scale-up,
- InfiniBand or Ethernet and scale-out,
- TensorRT-LLM or serving software,
- latency,
- throughput,
- cost per token.

Senior signal:

> I would not evaluate the platform on peak FLOPS alone.

### Answer 40

Reasoning models may cost more to serve because they can use more test-time
compute, generate more tokens, perform more intermediate steps, use longer
contexts, call tools, or run multiple model passes.

This increases latency, GPU time, memory pressure, and scheduling complexity.

### Answer 41

Ask:

- Does the model fit on one GPU?
- What is the latency target?
- Which phase dominates?
- What parallelism strategy is proposed?
- What communication happens per layer?
- Is the interconnect strong enough?
- Can compute and communication overlap?
- How does the serving stack support it?

### Answer 42

Executive answer:

> LLM serving turns user requests into repeated GPU computations. The system
> must process the prompt, generate tokens one at a time, manage memory for
> prior context, batch users efficiently, and keep latency and cost under
> control. The hard part is balancing quality, speed, cost, and reliability.

### Answer 43

Balanced answer:

> I would compare the platforms using actual workload metrics, not marketing
> numbers. I would look at time to first token, tokens per second, tail latency,
> cost per token, memory capacity, bandwidth, interconnect, software maturity,
> operational reliability, and how well the platform supports the target model.

### Answer 44

Strong answer:

> My hardware background is relevant because LLM systems are constrained by
> compute, memory, communication, and software. Hardware architecture training
> helps me reason from workload behavior to bottlenecks, model tradeoffs, and
> platform choices. That is directly useful for large-scale training and
> inference infrastructure.

### Answer 45

Good first steps:

1. Separate prefill and decode metrics.
2. Check recent workload changes.
3. Inspect batch size and context length.
4. Measure GPU utilization, HBM bandwidth, and KV-cache behavior.
5. Check serving scheduler and queueing.
6. Check kernel or software changes.
7. Check interconnect or collective time if multi-GPU.
8. Compare p50, p95, and p99 latency.

## Grading sheet

Use this table after finishing.

| Section | Score 0-4 | Weak topics | Follow-up action |
| --- | ---: | --- | --- |
| LLM fundamentals | | | |
| NVIDIA platforms | | | |
| LLM/GPU bridge | | | |
| Behavioral strategy | | | |
| Senior synthesis | | | |

## Pass criteria

You can move to Week 2 if:

- every section score is at least 2.0,
- average score is at least 3.0,
- you can answer Questions 39, 43, and 44 out loud,
- you have at least five usable behavioral story candidates,
- you know exactly what to review next.

## Remediation map

| Weak area | Review file |
| --- | --- |
| LLM basics | `llms/01_llm_fundamentals.md` |
| NVIDIA platform map | `nvidia/01_latest_nvidia_platforms.md` |
| Bottleneck reasoning | `systems/00_llm_gpu_bridge.md` |
| Behavioral stories | `behavioral/00_behavioral_strategy.md` |

## Final instruction

Do not treat the answer key as a script to memorize.

Use it to learn the shape of strong answers. In interviews, your answers should
sound natural, specific, and grounded in your own experience.
