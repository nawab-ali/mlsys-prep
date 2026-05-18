# Week 1 Baseline Diagnostic

This diagnostic checks the Week 1 foundation. It is not punitive. Use it to find weak
areas before moving into deeper LLM, GPU, and systems modules.

## Instructions

Answer without notes first. Then review the Week 1 modules, revise your answers, and log
weak areas in [04_progress_tracker.md](../../plan/04_progress_tracker.md).

For explain-it-to-an-interviewer prompts, use two to four sentences. For architecture
reasoning prompts, state assumptions before giving the answer.

## Scoring Table

| Score | Meaning | Evidence |
| ---
| ---
| --- |
| 0 | Not started | Cannot define the concept yet. |
| 1 | Familiar | Recognizes terms but cannot explain clearly. |
| 2 | Can explain | Gives a correct basic explanation. |
| 3 | Can solve interview problems | Applies the concept to a realistic prompt. |
| 4 | Can teach and defend tradeoffs | Explains assumptions, tradeoffs, and failure modes. |

## Part A: LLM Fundamentals

1. Define an LLM in one precise paragraph.
2. What is a token, and why is a token not always a word?
3. What is a token ID?
4. What is an embedding, and why is it useful for accelerator execution?
5. What are logits?
6. What is the difference between logits and probabilities?
7. Explain autoregressive generation as a loop.
8. Why is the "next-token predictor" view useful but incomplete?
9. Why is an LLM not a database?
10. Why did Transformers become attractive for accelerator-based training?
11. What is the Week 1 difference between training and inference?
12. Name two LLM topics intentionally deferred to later weeks.

## Part B: NVIDIA Platform Landscape

1. What does "latest NVIDIA hardware" mean for this curriculum?
2. Explain Blackwell in one sentence.
3. Explain Grace Blackwell in one sentence.
4. What is GB200 NVL72?
5. What is GB300 NVL72, and why is it important for reasoning workloads?
6. What is Vera Rubin NVL72 in the public roadmap context?
7. Why does a 72-GPU NVLink domain matter for LLM workloads?
8. Why is NVIDIA's advantage not only the GPU chip?
9. Name one software layer that matters for production LLM inference.
10. What should you memorize versus reason from in platform interviews?

## Part C: LLM/GPU Bridge

1. Explain LLMs as matrix workloads.
2. Explain LLMs as memory workloads.
3. Explain LLMs as communication workloads.
4. What is the Week 1 preview distinction between prefill and decode?
5. What is the KV-cache preview, without going into Week 3 detail?
6. State the three recurring bottleneck questions.
7. A service is described as "GPU bound." What evidence would you ask for?
8. How does this bridge connect to custom silicon and PPA?

## Part D: Behavioral Positioning

1. Write a one-sentence positioning statement for your target roles.
2. Give one NVIDIA-specific angle from your background.
3. Give one OpenAI-specific angle from your background.
4. Give one Anthropic-specific angle from your background.
5. Name one behavioral red flag you want to avoid.
6. Pick one story-bank theme and list the missing evidence you need.

## Part E: Design Prompt

You are asked to evaluate whether a rack-scale NVIDIA GPU system or a custom accelerator
is a better fit for a new LLM inference service. The product target is low latency, but
the model and traffic shape are not yet specified.

Give a senior/principal-level first response. Include the assumptions you need, the three
bottleneck questions, and how you would avoid premature conclusions.

## Answer Key: Part A

1. Expected answer: token sequence to next-token distributions.
Senior/principal signal: connects definition to systems.
Common red flag: calls it a chatbot.
2. Expected answer: tokens are text fragments, not always words.
Senior/principal signal: mentions model-specific tokenization.
Common red flag: assumes words only.
3. Expected answer: integer vocabulary label.
Senior/principal signal: separates symbols from tensors.
Common red flag: calls it an embedding.
4. Expected answer: learned dense vector from lookup.
Senior/principal signal: connects lookup to tensor compute.
Common red flag: treats it as a fact table.
5. Expected answer: unnormalized vocabulary scores.
Senior/principal signal: separates model score from policy.
Common red flag: calls logits probabilities.
6. Expected answer: probabilities come after conversion.
Senior/principal signal: mentions decoding policy.
Common red flag: ignores sampling.
7. Expected answer: score, select, append, repeat.
Senior/principal signal: connects loop to latency.
Common red flag: describes one pass only.
8. Expected answer: mechanistic but not complete.
Senior/principal signal: avoids dismissive framing.
Common red flag: says "just autocomplete."
9. Expected answer: weights are not queried rows.
Senior/principal signal: explains learned structure.
Common red flag: claims exact lookup.
10. Expected answer: more parallel tensor work.
Senior/principal signal: cites Transformer motivation.
Common red flag: says "because attention is magic."
11. Expected answer: training updates weights; inference serves.
Senior/principal signal: names different bottlenecks.
Common red flag: treats them as identical.
12. Expected answer: attention math, KV cache, RLHF, serving.
Senior/principal signal: knows scope boundaries.
Common red flag: deep-dives too early.

## Answer Key: Part B

1. Expected answer: moving public platform landscape.
Senior/principal signal: distinguishes current and roadmap.
Common red flag: says only GB200.
2. Expected answer: current NVIDIA GPU architecture anchor.
Senior/principal signal: links to AI workloads.
Common red flag: recites no system role.
3. Expected answer: Grace CPU plus Blackwell GPU systems.
Senior/principal signal: mentions CPU-GPU integration.
Common red flag: treats it as one chip only.
4. Expected answer: Grace Blackwell rack-scale NVLink system.
Senior/principal signal: links to scale-up fabric.
Common red flag: misses rack-scale context.
5. Expected answer: Blackwell Ultra reasoning platform.
Senior/principal signal: mentions test-time scaling pressure.
Common red flag: claims unsourced details.
6. Expected answer: forward-looking Vera CPU and Rubin GPU platform.
Senior/principal signal: marks roadmap status.
Common red flag: treats roadmap as fixed design.
7. Expected answer: reduces scale-up communication pain.
Senior/principal signal: connects fabric to utilization.
Common red flag: says "more GPUs" only.
8. Expected answer: full stack with GPU, memory, fabric, CUDA, and software.
Senior/principal signal: explains platform lock-in.
Common red flag: only mentions FLOPS.
9. Expected answer: TensorRT-LLM or CUDA stack.
Senior/principal signal: knows software matters.
Common red flag: ignores software.
10. Expected answer: memorize anchors; reason from bottlenecks.
Senior/principal signal: avoids SKU trivia.
Common red flag: memorizes numbers only.

## Answer Key: Part C

1. Expected answer: dense tensor operations.
Senior/principal signal: mentions shapes and utilization.
Common red flag: says "AI math" only.
2. Expected answer: weights, activations, KV state.
Senior/principal signal: mentions capacity and bandwidth.
Common red flag: ignores memory.
3. Expected answer: multi-GPU or multi-node movement.
Senior/principal signal: separates scale-up and scale-out.
Common red flag: ignores synchronization.
4. Expected answer: prefill handles prompt; decode emits tokens.
Senior/principal signal: links to different bottlenecks.
Common red flag: treats all tokens alike.
5. Expected answer: stored attention state preview.
Senior/principal signal: avoids deep math too early.
Common red flag: overclaims implementation.
6. Expected answer: compute, memory, communication.
Senior/principal signal: applies them consistently.
Common red flag: lists random metrics.
7. Expected answer: utilization, bandwidth, queueing, batch, latency.
Senior/principal signal: asks for evidence.
Common red flag: accepts label blindly.
8. Expected answer: compare PPA under workload assumptions.
Senior/principal signal: includes software and risk.
Common red flag: compares peak FLOPS only.

## Answer Key: Part D

1. Expected answer: links ML hardware to LLM systems.
Senior/principal signal: clear, specific positioning.
Common red flag: generic AI enthusiasm.
2. Expected answer: PPA, modeling, platforms, co-design.
Senior/principal signal: maps to NVIDIA value.
Common red flag: chip-only framing.
3. Expected answer: infrastructure rigor for frontier systems.
Senior/principal signal: connects to reliability and cost.
Common red flag: claims model research depth.
4. Expected answer: reliable systems and careful deployment.
Senior/principal signal: connects to safety and trust.
Common red flag: ignores mission context.
5. Expected answer: names a concrete habit to avoid.
Senior/principal signal: shows self-awareness.
Common red flag: says "none."
6. Expected answer: lists scope, metric, tradeoff, outcome.
Senior/principal signal: evidence-driven story prep.
Common red flag: invents details.

## Answer Key: Part E

Expected answer:
- Refuse to choose before fixing model, context, batch, traffic, SLA, reliability, and cost.

Senior/principal signal:
- Uses compute, memory, communication, software maturity, and platform risk.

Common red flags:
- Chooses on peak FLOPS.
- Ignores software maturity.
- Skips workload assumptions.

## Visual Progress Summary

| Area | Score | Weak area to log | Next study action |
| ---
| ---
| ---
| --- |
| LLM fundamentals |  |  |  |
| NVIDIA platform landscape |  |  |  |
| LLM/GPU bridge |  |  |  |
| Behavioral positioning |  |  |  |
| Design reasoning |  |  |  |

## Progress Reflection

After scoring, update [04_progress_tracker.md](../../plan/04_progress_tracker.md):
- Mark each Week 1 completion checkbox that is done.
- Record the lowest scoring area as a weak area.
- Write one next study action for the next session.
- Add one story-bank gap if behavioral evidence is incomplete.
