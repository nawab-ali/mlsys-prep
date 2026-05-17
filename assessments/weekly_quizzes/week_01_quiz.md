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
| --- | --- | --- |
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

| Q | Expected answer | Senior/principal signal | Common red flag |
| --- | --- | --- | --- |
| 1 | Token sequence to next-token distributions. | Connects definition to systems. | Calls it a chatbot. |
| 2 | Tokens are text fragments, not always words. | Mentions model-specific tokenization. | Assumes words only. |
| 3 | Integer vocabulary label. | Separates symbols from tensors. | Calls it an embedding. |
| 4 | Learned dense vector from lookup. | Connects lookup to tensor compute. | Treats it as a fact table. |
| 5 | Unnormalized vocabulary scores. | Separates model score from policy. | Calls logits probabilities. |
| 6 | Probabilities come after conversion. | Mentions decoding policy. | Ignores sampling. |
| 7 | Score, select, append, repeat. | Connects loop to latency. | Describes one pass only. |
| 8 | Mechanistic but not complete. | Avoids dismissive framing. | Says "just autocomplete." |
| 9 | Weights are not queried rows. | Explains learned structure. | Claims exact lookup. |
| 10 | More parallel tensor work. | Cites Transformer motivation. | Says "because attention is magic." |
| 11 | Training updates weights; inference serves. | Names different bottlenecks. | Treats them as identical. |
| 12 | Attention math, KV cache, RLHF, serving. | Knows scope boundaries. | Deep-dives too early. |

## Answer Key: Part B

| Q | Expected answer | Senior/principal signal | Common red flag |
| --- | --- | --- | --- |
| 1 | Moving public platform landscape. | Distinguishes current and roadmap. | Says only GB200. |
| 2 | Current NVIDIA GPU architecture anchor. | Links to AI workloads. | Recites no system role. |
| 3 | Grace CPU plus Blackwell GPU systems. | Mentions CPU-GPU integration. | Treats it as one chip only. |
| 4 | Grace Blackwell rack-scale NVLink system. | Links to scale-up fabric. | Misses rack-scale context. |
| 5 | Blackwell Ultra reasoning platform. | Mentions test-time scaling pressure. | Claims unsourced details. |
| 6 | Forward-looking Vera CPU and Rubin GPU platform. | Marks roadmap status. | Treats roadmap as fixed design. |
| 7 | Reduces scale-up communication pain. | Connects fabric to utilization. | Says "more GPUs" only. |
| 8 | Full stack: GPU, memory, fabric, CUDA, software. | Explains platform lock-in. | Only mentions FLOPS. |
| 9 | TensorRT-LLM or CUDA stack. | Knows software matters. | Ignores software. |
| 10 | Memorize anchors; reason from bottlenecks. | Avoids SKU trivia. | Memorizes numbers only. |

## Answer Key: Part C

| Q | Expected answer | Senior/principal signal | Common red flag |
| --- | --- | --- | --- |
| 1 | Dense tensor operations. | Mentions shapes and utilization. | Says "AI math" only. |
| 2 | Weights, activations, KV state. | Mentions capacity and bandwidth. | Ignores memory. |
| 3 | Multi-GPU or multi-node movement. | Separates scale-up and scale-out. | Ignores synchronization. |
| 4 | Prefill handles prompt; decode emits tokens. | Links to different bottlenecks. | Treats all tokens alike. |
| 5 | Stored attention state preview. | Avoids deep math too early. | Overclaims implementation. |
| 6 | Compute, memory, communication. | Applies them consistently. | Lists random metrics. |
| 7 | Utilization, bandwidth, queueing, batch, latency. | Asks for evidence. | Accepts label blindly. |
| 8 | Compare PPA under workload assumptions. | Includes software and risk. | Compares peak FLOPS only. |

## Answer Key: Part D

| Q | Expected answer | Senior/principal signal | Common red flag |
| --- | --- | --- | --- |
| 1 | Links ML hardware to LLM systems. | Clear, specific positioning. | Generic AI enthusiasm. |
| 2 | PPA, modeling, platforms, co-design. | Maps to NVIDIA value. | Chip-only framing. |
| 3 | Infrastructure rigor for frontier systems. | Connects to reliability and cost. | Claims model research depth. |
| 4 | Reliable systems and careful deployment. | Connects to safety and trust. | Ignores mission context. |
| 5 | Names a concrete habit to avoid. | Shows self-awareness. | Says "none." |
| 6 | Lists scope, metric, tradeoff, outcome. | Evidence-driven story prep. | Invents details. |

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
| --- | --- | --- | --- |
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
