# Weekly Schedule

This 12-week schedule interleaves LLM preparation and NVIDIA GPU preparation every week.
It is a high-level outline only; detailed study materials will come later.

<table>
  <thead>
    <tr>
      <th>Week</th>
      <th>LLM Focus</th>
      <th>NVIDIA/GPU Focus</th>
      <th>Systems Bridge Focus</th>
      <th>Behavioral/Leadership Focus</th>
      <th>Assessment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>what LLMs are, tokens, embeddings, transformer purpose</td>
      <td>latest NVIDIA platform landscape and why GPUs dominate LLMs</td>
      <td>LLMs as matrix, memory, and communication workloads</td>
      <td>career narrative and target-company positioning</td>
      <td>baseline diagnostic</td>
    </tr>
    <tr>
      <td>2</td>
      <td>transformer block, attention, MLP, normalization, residuals</td>
      <td>SMs, warps, Tensor Cores, HBM, and GPU execution model</td>
      <td>mapping transformer operations to GPU hardware</td>
      <td>explaining complex architecture decisions</td>
      <td>conceptual quiz and whiteboard explanation</td>
    </tr>
    <tr>
      <td>3</td>
      <td>attention mechanics, causal masking, prefill versus decode</td>
      <td>memory hierarchy, HBM bandwidth, on-chip storage, data movement</td>
      <td>attention, KV cache, and memory pressure</td>
      <td>ambiguity and tradeoff stories</td>
      <td>design drill on inference bottlenecks</td>
    </tr>
    <tr>
      <td>4</td>
      <td>inference basics, decoding, sampling, batching, serving metrics</td>
      <td>inference-oriented GPU performance bottlenecks</td>
      <td>latency, throughput, batch size, utilization, and cost</td>
      <td>leadership under schedule pressure</td>
      <td>Month 1 technical midterm</td>
    </tr>
    <tr>
      <td>5</td>
      <td>training pipeline, forward/backward pass, optimizers, fine-tuning</td>
      <td>training workloads on modern NVIDIA GPUs</td>
      <td>compute, memory, activation, gradient, and optimizer state costs</td>
      <td>cross-functional leadership</td>
      <td>training versus inference comparison</td>
    </tr>
    <tr>
      <td>6</td>
      <td>distributed training concepts and parallelism</td>
      <td>scale-up systems, NVLink, NVSwitch, rack-scale platforms</td>
      <td>data, tensor, pipeline, expert, and sequence parallelism</td>
      <td>influencing without authority</td>
      <td>distributed training design prompt</td>
    </tr>
    <tr>
      <td>7</td>
      <td>production serving architecture, scheduling, routing, model hosting</td>
      <td>scale-out networking, InfiniBand, Ethernet, RDMA, collectives</td>
      <td>multi-node serving and training bottlenecks</td>
      <td>incident, postmortem, and reliability stories</td>
      <td>production systems quiz</td>
    </tr>
    <tr>
      <td>8</td>
      <td>quantization, sparsity, distillation, compression, low precision</td>
      <td>Tensor Cores, FP8, FP4, mixed precision, software support</td>
      <td>accuracy, latency, throughput, memory, and cost tradeoffs</td>
      <td>making hard technical tradeoffs</td>
      <td>Month 2 technical midterm</td>
    </tr>
    <tr>
      <td>9</td>
      <td>RAG, tools, agents, orchestration, memory, guardrails</td>
      <td>CUDA stack, libraries, compilers, kernels, serving frameworks</td>
      <td>systems around the model and where GPU performance matters</td>
      <td>mentoring and technical leadership</td>
      <td>agent/RAG systems interview drill</td>
    </tr>
    <tr>
      <td>10</td>
      <td>VLMs and multimodal production systems</td>
      <td>capacity planning for mixed workloads and large context windows</td>
      <td>vision/text workload differences and serving implications</td>
      <td>communicating with executives and non-experts</td>
      <td>multimodal architecture prompt</td>
    </tr>
    <tr>
      <td>11</td>
      <td>evaluation, benchmarks, hallucination, safety, reliability</td>
      <td>performance modeling, roofline, bottleneck analysis, accelerator comparison</td>
      <td>evaluating GPUs and custom accelerators for LLM workloads</td>
      <td>conflict, disagreement, and decision quality</td>
      <td>accelerator evaluation case study</td>
    </tr>
    <tr>
      <td>12</td>
      <td>full-stack production LLM system synthesis</td>
      <td>latest NVIDIA platform synthesis and cluster-level design</td>
      <td>end-to-end LLM platform design for target companies</td>
      <td>final story bank and company-specific positioning</td>
      <td>final mock interview loop</td>
    </tr>
  </tbody>
</table>

Detailed study materials are pending the deep research phase.
