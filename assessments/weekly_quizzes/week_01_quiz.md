# Week 1 Baseline Diagnostic

This diagnostic checks the Week 1 foundation. It is not a punitive exam. Use it to find
where the next review session should focus.

## Instructions

Answer without notes first. Then review the Week 1 modules, revise your answers, and mark
weak areas in the progress tracker.

For explain-it-to-an-interviewer prompts, use two to four sentences. For architecture
reasoning prompts, state assumptions before giving the answer.

## Scoring Rubric

- 0: not started.
- 1: familiar.
- 2: can explain.
- 3: can solve interview problems.
- 4: can teach and defend tradeoffs.

## Part A: LLM Fundamentals

1. Define an LLM in one precise paragraph.
2. What is a token, and why is a token not always a word?
3. What is a token ID?
4. What is an embedding, and why is it useful for accelerator execution?
5. What are logits?
6. Explain autoregressive generation as a loop.
7. Why is an LLM not a database?
8. Why did Transformers become attractive for accelerator-based training?
9. What is the Week 1 difference between training and inference?
10. Name two LLM topics intentionally deferred to later weeks.

## Part B: NVIDIA Platform Landscape

1. What does "latest NVIDIA hardware" mean for this curriculum?
2. Explain Blackwell in one sentence.
3. Explain Grace Blackwell in one sentence.
4. What is GB200 NVL72?
5. Why does a 72-GPU NVLink domain matter for LLM workloads?
6. Why is NVIDIA's advantage not only the GPU chip?
7. Name one software layer that matters for production LLM inference.
8. What should you memorize versus reason from in platform interviews?

## Part C: LLM/GPU Bridge

1. Explain LLMs as matrix workloads.
2. Explain LLMs as memory workloads.
3. Explain LLMs as communication workloads.
4. What is the Week 1 preview distinction between prefill and decode?
5. State the three recurring bottleneck questions.
6. A service is described as "GPU bound." What evidence would you ask for?

## Part D: Behavioral Positioning

1. Write a one-sentence positioning statement for your target roles.
2. Give one NVIDIA-specific angle from your background.
3. Give one OpenAI-specific or Anthropic-specific angle from your background.
4. Name one behavioral red flag you want to avoid.

## Part E: Design Prompt

You are asked to evaluate whether a rack-scale NVIDIA GPU system or a custom accelerator
is a better fit for a new LLM inference service. The product target is low latency, but
the model and traffic shape are not yet specified.

Give a senior/principal-level first response. Include the assumptions you need, the three
bottleneck questions, and how you would avoid premature conclusions.

## Answer Key

Use this key to calibrate, not to memorize wording.

### Part A

1. A strong answer says an LLM maps token sequences to next-token probability
   distributions and is learned from data.
2. A token is a discrete symbol or text fragment; tokenization depends on vocabulary and
   context.
3. A token ID is the integer representation of a token in the model vocabulary.
4. An embedding is a learned dense vector that turns discrete IDs into tensor data.
5. Logits are unnormalized vocabulary scores before probability conversion.
6. Generation repeats: run model, score next token, select token, append it, repeat.
7. Weights encode learned statistical structure; they are not queried like database rows.
8. Transformers exposed more parallel tensor work than recurrent sequence processing.
9. Training changes weights; inference uses fixed weights to serve outputs.
10. Valid deferred topics include attention math, KV cache, serving, fine-tuning, and RLHF.

### Part B

1. The Week 1 anchor is the public Blackwell and Grace Blackwell platform generation.
2. Blackwell is NVIDIA's current GPU architecture anchor for large AI workloads.
3. Grace Blackwell combines Grace CPU capability with Blackwell GPUs in system designs.
4. GB200 NVL72 is a rack-scale Grace Blackwell platform with 72 Blackwell GPUs.
5. It gives a large scale-up communication domain, reducing some multi-GPU bottlenecks.
6. The platform includes GPU, HBM, Tensor Cores, NVLink, networking, CUDA, and software.
7. TensorRT-LLM, CUDA libraries, compilers, or serving frameworks are valid answers.
8. Memorize anchor facts; reason from workload shape, bottlenecks, and assumptions.

### Part C

1. Matrix workload answers should mention tensor operations and accelerator utilization.
2. Memory answers should mention weights, activations, KV cache preview, bandwidth, or
   capacity.
3. Communication answers should mention multi-GPU or multi-node data movement.
4. Prefill processes prompt tokens; decode generates output tokens step by step.
5. Compute, memory capacity and bandwidth, communication.
6. Ask for utilization, memory bandwidth, batch shape, latency breakdown, and queueing.

### Part D

1. Strong positioning links ML hardware architecture to LLM systems and co-design.
2. A strong NVIDIA angle links accelerator architecture, PPA, modeling, and platforms.
3. A strong OpenAI or Anthropic angle links systems rigor to frontier model deployment.
4. Valid red flags include overclaiming LLM depth or ignoring product/system impact.

### Part E

A strong answer refuses to choose before fixing model size, context length, batch shape,
traffic distribution, latency target, reliability needs, software maturity, and cost
constraints. It uses the three bottleneck questions and compares total platform risk, not
only peak TOPS or FLOPS.

## Progress Reflection

- Lowest scoring section:
- Most important weak area:
- One concept to explain aloud tomorrow:
- One company-specific story to improve:
- Next study action:
