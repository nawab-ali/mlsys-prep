# mlsys-prep

This repository is a structured ML systems interview preparation program.

The immediate focus is Week 1.

Week 1 builds the foundation for senior-level interviews involving LLMs,
NVIDIA GPU platforms, LLM/GPU systems thinking, and behavioral positioning.

## Start here

Begin Week 1 in this order:

1. [LLM Fundamentals](llms/01_llm_fundamentals.md)
2. [Latest NVIDIA Platforms](nvidia/01_latest_nvidia_platforms.md)
3. [LLM and GPU Bridge](systems/00_llm_gpu_bridge.md)
4. [Behavioral Strategy](behavioral/00_behavioral_strategy.md)
5. [Week 1 Quiz](assessments/weekly_quizzes/week_01_quiz.md)
6. [Progress Tracker](plan/04_progress_tracker.md)

Do not browse directories manually. Start with the list above.

## Week 1 goal

The goal of Week 1 is to build a shared mental model for the rest of the
curriculum.

After Week 1, you should be able to explain:

- what an LLM is,
- how tokens become logits,
- why NVIDIA's advantage is platform-level,
- how LLM workloads map to compute, memory, and communication,
- why prefill and decode stress systems differently,
- why peak FLOPS is not enough to evaluate a platform,
- how your hardware architecture background maps to LLM systems roles.

## Week 1 study flow

### Step 1: LLM Fundamentals

Read:

[LLM Fundamentals](llms/01_llm_fundamentals.md)

Purpose:

- build the LLM vocabulary,
- understand tokens, embeddings, logits, and autoregressive generation,
- learn the Week 1 mental model of Transformer-based LLMs.

You should be able to answer:

```text
What is an LLM?
How does text become tokens?
What are logits?
What does autoregressive generation mean?
```

### Step 2: Latest NVIDIA Platforms

Read:

[Latest NVIDIA Platforms](nvidia/01_latest_nvidia_platforms.md)

Purpose:

- understand NVIDIA as a platform company,
- learn the Week 1 map of GB200, GB300, Blackwell Ultra, and Vera Rubin,
- connect GPUs, HBM, NVLink, networking, CUDA, NCCL, and TensorRT-LLM.

You should be able to answer:

```text
Why is NVIDIA's advantage platform-level?
What is GB300 NVL72?
Why does HBM matter for LLMs?
Why is peak FLOPS insufficient?
```

### Step 3: LLM and GPU Bridge

Read:

[LLM and GPU Bridge](systems/00_llm_gpu_bridge.md)

Purpose:

- connect LLM behavior to hardware bottlenecks,
- learn the compute, memory, and communication framework,
- understand prefill, decode, KV cache, and multi-GPU pressure.

You should be able to answer:

```text
Why are LLMs both compute and memory workloads?
Why is decode different from prefill?
Why does KV cache matter?
How would you compare two accelerators for LLM inference?
```

### Step 4: Behavioral Strategy

Read:

[Behavioral Strategy](behavioral/00_behavioral_strategy.md)

Purpose:

- build your interview narrative,
- map your background to NVIDIA, OpenAI, and Anthropic,
- create a story bank for senior/principal interviews.

You should be able to answer:

```text
Tell me about yourself.
Why NVIDIA?
Why OpenAI?
Why Anthropic?
Tell me about a difficult architecture tradeoff.
```

### Step 5: Week 1 Quiz

Complete:

[Week 1 Quiz](assessments/weekly_quizzes/week_01_quiz.md)

Purpose:

- test recall,
- test interview readiness,
- expose weak areas before moving to Week 2.

Do the quiz without notes first.

Then review the answer key.

### Step 6: Progress Tracker

Update:

[Progress Tracker](plan/04_progress_tracker.md)

Record:

- quiz scores,
- weak areas,
- follow-up actions,
- behavioral stories that need work,
- topics to revisit before Week 2.

## Week 1 completion criteria

Week 1 is complete when you can do all of the following without notes:

- explain the LLM token-to-logit pipeline,
- explain NVIDIA's platform stack,
- distinguish training, prefill, decode, and serving,
- explain KV cache and memory pressure,
- explain scale-up versus scale-out,
- give a structured accelerator comparison answer,
- give your 30-second career narrative,
- name at least five behavioral story candidates,
- score at least 3.0 average on the Week 1 quiz.

## Week 1 quality bar

The Week 1 files are intended to be the quality baseline for future weeks.

Each Week 1 module should include:

- clear explanations,
- diagrams or tables,
- senior-level interview framing,
- self-check questions,
- practical answer patterns,
- source grounding where needed.

Future weeks should match or exceed this standard.

## Week 1 files

| File | Purpose |
| --- | --- |
| `llms/01_llm_fundamentals.md` | LLM vocabulary and mental model |
| `nvidia/01_latest_nvidia_platforms.md` | NVIDIA platform landscape |
| `systems/00_llm_gpu_bridge.md` | LLM workload to GPU systems bridge |
| `behavioral/00_behavioral_strategy.md` | Behavioral interview foundation |
| `assessments/weekly_quizzes/week_01_quiz.md` | Week 1 diagnostic |
| `references/sources.md` | Source and research policy |
| `plan/04_progress_tracker.md` | Study tracking and weak-area log |

## What not to do in Week 1

Do not try to master every detail yet.

Do not get stuck on:

- CUDA programming details,
- SM microarchitecture,
- NCCL algorithms,
- MoE routing,
- agent systems,
- advanced attention variants,
- full roofline modeling,
- detailed cluster design.

Those belong in later weeks.

Week 1 is about building the foundation.

## Development workflow

Use pull requests for repository changes.

Do not push directly to `main`.

Each major content update should be reviewed before merge.
