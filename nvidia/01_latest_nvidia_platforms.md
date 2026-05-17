# Week 1: Latest NVIDIA Platform Landscape

This module gives the Week 1 platform map for modern NVIDIA systems used in LLM training
and inference. It stays high level; later modules cover the microarchitecture and software
stack in depth.

## Learning Goals

- Explain what "latest NVIDIA hardware" means for this curriculum.
- Describe Blackwell and Grace Blackwell at a high level.
- Place B200, GB200, and GB200 NVL72 in the platform landscape.
- Explain why NVIDIA's LLM advantage is broader than one GPU chip.
- Separate facts to memorize from tradeoffs to reason through in interviews.

## Why This Matters For Interviews

NVIDIA interviews may test whether you can reason across GPU architecture, rack-scale
systems, software, and customer workloads. OpenAI and Anthropic interviews may care less
about product names, but they will care about your ability to connect model scale to
accelerator supply, serving cost, reliability, and cluster design.

For senior/principal roles, avoid sounding like a spec sheet. Use platform facts as entry
points into bottleneck analysis and hardware/software co-design.

## What "Latest NVIDIA Hardware" Means For This Curriculum

For Week 1, "latest" means the current public Blackwell and Grace Blackwell generation as
the anchor. The focus is on public platform concepts that matter for LLMs: Tensor Cores,
HBM, NVLink, NVSwitch, Grace CPU integration, CUDA, libraries, and serving/training
software.

Older generations are not the focus. They may appear only as brief context when comparing
why a newer platform changes a system bottleneck.

## Blackwell And Grace Blackwell At A High Level

Blackwell is NVIDIA's GPU architecture generation positioned for AI factories and large
AI workloads (Source 1). Grace Blackwell combines Blackwell GPUs with Grace CPUs into a
system architecture, including coherent CPU-GPU connectivity through NVLink-C2C in the
GB200 Grace Blackwell Superchip context (Sources 3 and 4).

At this level, remember the system shape:

- Blackwell GPU: accelerator for dense AI math and memory-intensive model execution.
- Grace CPU: host-side compute and memory participant in Grace Blackwell systems.
- NVLink-C2C: CPU-GPU connection in the Grace Blackwell Superchip context.
- NVLink and NVLink Switch: scale-up communication fabric for large GPU domains.
- CUDA and libraries: the programming and software ecosystem around the hardware.

## B200, GB200, GB200 NVL72, And Rack-Scale Systems

B200 is the Blackwell GPU product name you should recognize as a current data-center GPU
building block. GB200 refers to Grace Blackwell systems that pair Grace CPU capability with
Blackwell GPUs.

GB200 NVL72 is the key Week 1 rack-scale reference point. NVIDIA describes it as a
rack-scale design connecting 36 Grace CPUs and 72 Blackwell GPUs in a 72-GPU NVLink domain
(Source 3). NVIDIA also positions GB200 NVL72 for scalable LLM inference and training
workloads (Sources 2, 3, and 4).

| Platform/component | What it is | Why it matters for LLMs | Depth |
| --- | --- | --- | --- |
| Blackwell | Current NVIDIA GPU architecture anchor. | Tensor math and memory for AI workloads. | Weeks 2, 8, 12 |
| B200 | Blackwell data-center GPU product. | Building block for server platforms. | Weeks 2, 10 |
| GB200 | Grace Blackwell system building block. | CPU-GPU integration for large systems. | Weeks 5, 6 |
| GB200 NVL72 | Rack-scale 72-GPU NVLink system. | Large-model scale-up domain. | Weeks 6, 12 |
| NVLink/NVSwitch | High-bandwidth GPU communication. | Reduces scale-up communication pain. | Week 6 |
| CUDA/libraries | Programming and software ecosystem. | Turns hardware into usable platforms. | Week 9 |
| TensorRT-LLM | Production inference software preview. | Optimizes LLM serving on NVIDIA GPUs. | Week 7 |

## Why NVIDIA Platforms Are Strong For LLMs

NVIDIA's advantage is not only the GPU chip. It is the combination of GPU architecture,
HBM, Tensor Cores, NVLink/NVSwitch, networking, CUDA, libraries, and serving/training
software.

That combination matters because LLM systems stress multiple layers at once:

- Compute: matrix operations and low-precision tensor execution.
- Memory: model weights, activations, KV cache, and serving state.
- Communication: multi-GPU and multi-node parallelism.
- Software: kernels, libraries, compilers, schedulers, and serving frameworks.

The CUDA C++ Programming Guide frames CUDA as NVIDIA's general-purpose parallel computing
platform and programming model (Source 5). TensorRT-LLM is a preview of the production
inference software layer that later modules will study in more detail (Source 6).

## Compute, Memory, Communication, And Software Ecosystem

In Week 1, use this stack as a map:

```text
Model demand
  -> tensor compute
  -> HBM capacity and bandwidth
  -> GPU-to-GPU communication
  -> cluster networking
  -> CUDA, libraries, compilers, and serving software
```

The GB200 NVL72 sources emphasize scale-up communication, including a 72-GPU NVLink domain
and high per-GPU NVLink bandwidth in Grace Blackwell systems (Sources 3 and 4). Treat those
facts as system clues: large models need both local tensor throughput and fast movement of
state across devices.

## What To Memorize Versus What To Reason From

Memorize:

- Blackwell and Grace Blackwell are the Week 1 current platform anchors.
- GB200 NVL72 is a rack-scale system with 36 Grace CPUs and 72 Blackwell GPUs.
- NVIDIA's platform story includes hardware, interconnect, networking, CUDA, and software.

Reason from:

- Whether the workload is compute-bound, memory-bound, or communication-bound.
- Whether scale-up fabric or scale-out networking is the first bottleneck.
- Whether software maturity changes the practical performance of the hardware.
- Whether a product claim maps to your specific batch size, context length, and SLA.

## What This File Intentionally Does Not Cover Yet

This file does not cover SMs, warps, Tensor Cores, HBM details, NVLink topology, CUDA
kernels, collectives, quantization formats, or serving frameworks in depth. Those topics
belong to later weeks.

## Interviewer Questions You Should Be Ready For

- What is the current NVIDIA platform anchor for this curriculum?
- Why is GB200 NVL72 important for large-model systems?
- Why is NVIDIA's advantage broader than a single GPU?
- What parts of the platform attack compute, memory, communication, and software risk?
- What should you memorize, and what should you derive from workload assumptions?

## Senior/Principal-Level Answer Patterns

- Begin with the workload, then map it to the platform.
- Say "GPU architecture plus system fabric plus software ecosystem," not just "faster GPU."
- Treat official performance claims as context, then ask about assumptions.
- Use rack-scale facts to reason about communication and utilization, not to recite specs.
- Avoid older architecture history unless it explains a current bottleneck.

## Week 1 Self-Check

- Can you explain GB200 NVL72 in two sentences?
- Can you name the four platform layers that matter for LLMs?
- Can you explain why NVLink/NVSwitch matters before studying topology details?
- Can you give one software reason NVIDIA platforms are hard to displace?
- Can you avoid overfitting to product names and instead reason from bottlenecks?

## Sources

Source 1: NVIDIA, "Blackwell Architecture."
https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/

Source 2: NVIDIA, "GB200 NVL72."
https://www.nvidia.com/en-us/data-center/gb200-nvl72/

Source 3: NVIDIA, "GB200 NVL Multi-Node Tuning Guide."
https://docs.nvidia.com/multi-node-nvlink-systems/multi-node-tuning-guide/overview.html

Source 4: NVIDIA developer blog, "GB200 NVL72 Delivers Trillion-Parameter LLM Training."
https://developer.nvidia.com/blog/nvidia-gb200-nvl72-delivers-trillion-parameter-llm-training-and-real-time-inference/

Source 5: CUDA C++ Programming Guide.
https://docs.nvidia.com/cuda/cuda-c-programming-guide/

Source 6: NVIDIA TensorRT-LLM documentation.
https://docs.nvidia.com/tensorrt-llm/
