# Dataflow, SIMD, Vector Processing, and GPUs

## Data Flow

A dataflow representation makes dependencies explicit: operations are nodes and values are edges. A node may fire
when all required inputs are ready.

Compared with a control-flow machine:

- no single sequential instruction stream is required conceptually;
- execution order is constrained mainly by dependencies;
- independent nodes can execute asynchronously;
- synchronization is represented explicitly.

Advantages:

- exposes irregular parallelism;
- naturally expresses producer/consumer relationships.

Disadvantages of a pure dataflow machine:

- precise state and debugging are difficult;
- tag matching and token storage add overhead;
- dynamic data structures and side effects complicate execution;
- locality can be poor unless the implementation actively manages it;
- uncontrolled graph expansion can create more runnable nodes/tokens than storage or execution resources support;
- operand/tag matching adds delay on a dependent chain even when arithmetic is fast.

Throttling spawning, bounding live contexts, and applying backpressure control excessive parallelism. For a chain
`A -> B -> C`, each consumer still waits for token delivery, context matching, and wakeup; graph parallelism does
not remove that serial dependence or its scheduling overhead.

Modern OoO cores use a **local dataflow engine** inside a conventional ISA: the scheduler wakes instructions when
operands become ready while the ROB preserves architectural order.

### Dataflow operators and node state

A conceptual node record contains an opcode, operand values with readiness bits, and result destinations:

```text
node N: [MUL | ready=1, arg1=6 | ready=0, arg2=? | destination=(P, input 0)]
receive token 7 for input 1 -> both inputs ready -> emit 42 to P's input 0
```

After firing, the consumed inputs are no longer ready for another firing. Dynamic graphs also need context tags
or equivalent matching rules so tokens from different loop iterations are not accidentally combined.

| Operator | Required inputs | Tokens consumed and produced |
| --- | --- | --- |
| Primitive, e.g., ADD | All operand tokens | Consume operands; emit the result |
| Fork | One value token | Consume it; emit one copy on each output |
| Switch | Value and Boolean selector | Consume both; emit the value on only the selected output |
| Controlled merge | Selector and selected input | Consume those two; emit selected value; leave other input alone |

For a merge with selector `true`, a token on the true input can proceed without waiting for the false input.
This is a **controlled merge**, not an arbitrary join that waits for every input. If an unselected token is present,
it is not consumed by that firing, matching the source's operator diagram.

Example: a fork sends `x=6` to two arithmetic nodes that compute `x+1=7` and `2*x=12` independently. A controlled
merge with selector `true` and these values on its true/false inputs emits `7`. For mutually exclusive branch
execution, use a switch before the branch computations so only the selected branch receives work.

## Data Parallelism

Data parallelism applies the same operation to many independent elements.

![Data-parallel execution models](assets/data_parallelism_models.svg)

*Figure: Illustrative SIMD versus vector-chaining schedules under the resource counts shown, not a benchmark.*
*These are example organizations, not universal timing rules. SIMT is discussed separately below.*
Source: [Comparison SIMD vs Vector.png][figure-simd] by Luke Kenneth Casson Leighton,
[CC BY-SA 4.0][figure-license-4]. Unmodified 1024-pixel-wide PNG embedded in SVG on white.

### Flynn taxonomy

| Class | Meaning | Typical example |
| --- | --- | --- |
| SISD | single instruction, single data | scalar sequential core |
| SIMD | single instruction, multiple data | vector/SIMD engine |
| MISD | multiple instruction, single data | rare as a general model |
| MIMD | multiple instruction, multiple data | multicore CPU |

SIMT is not a separate Flynn category. It is a programming/execution abstraction implemented with SIMD-like
hardware scheduling across groups of threads.

## SIMD Processing

A SIMD instruction performs one operation over multiple data elements.

Examples:

```text
scalar:  C0 = A0 + B0
SIMD:    [C0 C1 C2 C3] = [A0 A1 A2 A3] + [B0 B1 B2 B3]
```

SIMD benefits workloads with regular, independent element operations. Efficiency drops when masks leave lanes
inactive or when memory access is irregular.

### Array vs. vector interpretation

The original notes distinguish time-space duals:

- **array processor:** multiple processing elements operate in parallel in space;
- **vector processor:** pipelined functional units process vector elements over time.

Modern implementations often combine both ideas.

## Vector Processor

A vector processor exposes vector instructions and vector state directly to software.

Typical architectural state:

- vector registers;
- vector length (`VL`);
- vector masks/predicates;
- vector element width and grouping state;
- optional restart state such as `VSTART`.

Classic designs can also expose a vector-stride register (`VSTR`), controlling the spacing of memory elements.
For base address `b` and stride `s` bytes, element `i` is at `b + i*s`. Other ISAs encode stride through operands
rather than a dedicated named register; the control concept is the same.

A vector add conceptually does:

```text
for i in active_elements:
    V3[i] = V1[i] + V2[i]
```

Why vectors are efficient:

- one instruction represents many operations;
- fewer instruction fetch/decode operations;
- regular memory access supports banking and prefetching;
- element pipelines can sustain high throughput;
- masks replace many short branches.

For an elementwise operation, element 1 need not wait for element 0's arithmetic result. A pipelined unit can
accept a new element each cycle even if one element takes several cycles to finish. Dependencies **between**
vector instructions or reductions still need handling; "independent elements" is not a blanket promise for all code.

## Vector Processing Deep Dive

### Vector length and strip mining

#### One lane versus four lanes

In the teaching model, a vector register holds `N` elements of `M` bits each, or `N*M` bits in total;
the active length chooses how many participate. In a six-stage multiply pipeline, element 0 enters stage 1,
then advances to stage 2 while element 1 enters stage 1. After startup, completed `V1[i]*V2[i]` values write
successive `V3[i]` entries each cycle. Different stages hold different elements, not one whole vector per stage.

![One and four pipelined vector lanes](assets/vector_lanes.png)

*Figure: One vector-add pipeline versus four parallel pipelines; indices show the element distribution.*

For `C[i] = A[i] + B[i]`, one lane handles indices `0, 1, 2, ...`; four lanes can distribute them as
lane 0: `0, 4, 8, ...`, lane 1: `1, 5, 9, ...`, lane 2: `2, 6, 10, ...`, lane 3: `3, 7, 11, ...`.
This is spatial width combined with pipelining over time, not four independent vector instructions.

With eight elements, an illustrative three-cycle adder latency, and one new element per lane per cycle:

| Issue cycle, counting from 0 | One lane | Four lanes | Results become available at |
| --- | --- | --- | --- |
| 0 | Element 0 | Elements 0-3 | Cycle 3 |
| 1 | Element 1 | Elements 4-7 | Cycle 4 |
| 2-7 | Elements 2-7, one per cycle | No remaining elements | Cycles 5-10 for the one-lane case |

The final result arrives at cycle 10 with one lane and cycle 4 with four, assuming operands and write ports keep up.
At an intermediate snapshot, newer A/B pairs are waiting to enter while earlier results occupy successive pipeline
stages. After the latency, the destination vector fills one or four elements per cycle; not all elements appear
at once. Startup latency remains even when lane count grows.

#### Choosing the active length

If the dataset is longer than the hardware vector capacity, process it in chunks:

```text
while remaining > 0:
    VL = min(remaining, max_vector_length)
    operate on VL elements
    advance pointers by VL elements
    remaining -= VL
```

This is **strip mining**. With 527 elements and a maximum vector length of 64, process eight chunks of 64,
then one chunk of 15. The remaining count reaches zero. The maximum vector length must be positive.

Vector-length-agnostic ISAs such as RISC-V V and Arm SVE encourage code that does not assume one fixed physical
vector width.

### Masked execution

A predicate/mask register controls which elements participate:

```text
mask[i] = (V0[i] != 0)
V1[i] = mask[i] ? V0[i] * V2[i] : V1[i]
```

Masking is a form of predicated execution and avoids some control-flow branches.

### Stride, gather, and scatter

- **unit stride:** consecutive elements;
- **constant stride:** fixed distance between elements;
- **gather:** load vector elements from indexed addresses;
- **scatter:** store vector elements to indexed addresses.

Gather/scatter support irregular structures but is usually less efficient than unit-stride access.

### Memory banking

Vector processors need enough memory bandwidth to feed many element operations. Interleaved banks let successive
addresses map to independent banks so several accesses can overlap.

Bank conflicts occur when multiple accesses in the same cycle target the same bank.

Bank access latency is not the same as its **initiation interval**, the spacing between accepted requests.
Suppose four non-pipelined banks each need four cycles before accepting another request, and a shared bus carries
one element per cycle. With `bank = element_index % 4`, requests at cycles `0,1,2,3,4,...` go to banks
`0,1,2,3,0,...`; each bank has recovered when reused, allowing one element per cycle after startup.
With only two such banks, each is revisited after two cycles and cannot keep up. A stride of four in the four-bank
example always selects bank 0, reducing throughput to one element per four cycles. More banks do not exceed the
one-element-per-cycle shared-bus limit; four-lane compute needs wider/multiple transfers or sufficient buffered data.

Each bank has local address/data handling, represented by MAR/MDR boxes in the teaching bank diagram.
That local state permits overlapping bank work; the shared address/data buses still serialize their transfers.

### Chaining

A producer vector pipeline can forward element results directly to a dependent consumer pipeline before the full
vector completes. This is analogous to scalar forwarding at vector-element granularity.

## Graphics Processing Unit

The original statement "a GPU is a SIMD (SIMT) machine" is directionally useful but too compressed.

CUDA exposes a **single-program, multiple-data (SPMD) programming model**: threads run the same kernel on
their own data. NVIDIA GPUs use **SIMT execution** to issue instructions for active threads over SIMD-like datapaths.

For NVIDIA CUDA:

- thread = programmer-visible scalar execution context;
- block = cooperating group of threads;
- grid = collection of blocks for a kernel launch;
- warp = hardware execution group of 32 threads.

![GPU thread hierarchy](assets/gpu_simt_hierarchy.svg)

*Figure: NVIDIA's CUDA grid, blocks, and threads. This logical hierarchy does not show warps or SM placement.*
Source: [Block-thread.svg][figure-cuda] by NVIDIA, [CC BY 3.0][figure-license-3].
White background and display sizing; original drawing retained.

### SIMT vs. SIMD

SIMD exposes a vector operation explicitly to software. SIMT executes programmer-visible scalar threads in groups.
In CUDA, consecutive linear thread IDs within a block form fixed warps of up to 32 threads. Warp membership does
not change when threads diverge or are scheduled independently; hardware selects active threads from the same warp.

Each SIMT thread has its own logical registers and control flow, but threads in a warp share execution resources.

### Branch divergence

If threads in one warp take different control-flow paths, the hardware must execute the required paths while
masking threads that are inactive on each path.

Divergence is a performance concern, not normally a correctness problem.

### Independent Thread Scheduling

Since NVIDIA Volta, threads in a warp have more independent scheduling state than older lockstep models exposed.
Code must not assume implicit warp-wide synchronization where explicit synchronization is required.

### Latency hiding

GPUs tolerate long memory and execution latency by maintaining many resident warps and switching issue to ready
warps.

This differs from a CPU's emphasis on minimizing latency for a smaller number of threads with speculation and OoO
execution.

![Ready and waiting warps with resident register state](assets/warp_scheduling.png)

*Figure: Historical conceptual ready/waiting warp flow, not a modern SM pipeline specification.*

An SM allocates register-file storage to resident thread contexts. If warp 1's load misses, its dependent
instruction waits, but its registers remain allocated; the scheduler can issue a ready instruction from warp 3.
When the data returns and dependencies clear, warp 1 becomes eligible again. This ready -> issue -> wait -> ready
cycle is latency hiding, not saving registers to memory on every scheduling change. A modern warp can have several
instructions in flight; the teaching fetch/decode/ALU/cache boxes do not imply one-instruction-at-a-time execution.
The figure's lanes are schematic; actual CUDA warps contain 32 threads with fixed membership.

### Memory coalescing

A warp's memory references are most efficient when thread addresses can be combined into a small number of memory
transactions.

Good data layout therefore matters as much as arithmetic parallelism.

### Worked example: CPU vs. CUDA matrix addition

For two row-major `n x n` matrices, compute `C[row, col] = A[row, col] + B[row, col]`.
The CPU loops over elements; CUDA assigns one element to each thread. These teaching snippets assume positive
dimensions, index arithmetic that fits in `int`, and separate, sufficiently sized input/output arrays.

CPU baseline:

```cpp
void matrix_add_cpu(const float* a, const float* b, float* c, int n) {
    for (int row = 0; row < n; ++row) {
        for (int col = 0; col < n; ++col) {
            int index = row * n + col;
            c[index] = a[index] + b[index];
        }
    }
}
```

CUDA kernel:

```cpp
__global__ void matrix_add(const float* a, const float* b, float* c, int n) {
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    if (row < n && col < n) {
        int index = row * n + col;
        c[index] = a[index] + b[index];
    }
}
```

Host launch, with `a`, `b`, and `c` pointing to allocated device-accessible arrays and inputs already initialized:

```cpp
dim3 block(16, 16);
dim3 grid((n + 15) / 16, (n + 15) / 16);
matrix_add<<<grid, block>>>(a, b, c, n);
cudaDeviceSynchronize();
```

Each block covers a `16 x 16` tile. For `n = 17`, the grid is `2 x 2`; bounds checks discard excess threads.
For block `(1, 0)`, thread `(0, 3)` writes row `3`, column `16`, at offset `3 * 17 + 16 = 67`.
Adjacent x-lanes access adjacent columns. No inter-thread synchronization is needed because outputs are disjoint.

### Worked example: SAXPY with a grid-stride loop

SAXPY means **single-precision `a * x + y`**: update every `y[i] = a * x[i] + y[i]`.
Unlike the matrix example, each thread can process several elements, separated by the grid's total thread count.

```cpp
__global__ void saxpy(int n, float a, const float* x, float* y) {
    int index = blockIdx.x * blockDim.x + threadIdx.x;
    int stride = blockDim.x * gridDim.x;
    for (int i = index; i < n; i += stride) {
        y[i] = a * x[i] + y[i];
    }
}
```

With eight total threads and `n = 20`, thread `0` handles indices `0, 8, 16`; thread `3` handles `3, 11, 19`.
Different threads never update the same element, and neighboring threads access neighboring elements each iteration.

Host-side lifecycle using managed memory:

```cpp
constexpr int n = 1000;
constexpr int threads = 256;
float* x = nullptr;
float* y = nullptr;
cudaMallocManaged(&x, n * sizeof(float));
cudaMallocManaged(&y, n * sizeof(float));
for (int i = 0; i < n; ++i) {
    x[i] = 1.0f;
    y[i] = 2.0f;
}
int blocks = (n + threads - 1) / threads;
saxpy<<<blocks, threads>>>(n, 2.0f, x, y);
cudaDeviceSynchronize();
// Each y[i] is now 4.0f; inspect it on the CPU before freeing the arrays.
cudaFree(y);
cudaFree(x);
```

These are CUDA C++ fragments, not standalone programs; host fragments belong inside a function and require
`<cuda_runtime.h>`. They assume successful CUDA calls to keep the execution model visible. Real code must check
allocation results before dereferencing pointers, `cudaGetLastError()` after each launch, and synchronization/free
return values. Synchronize successfully before the CPU reads managed-memory results or releases the arrays.
No CPU-side loop over GPU threads is needed: the CUDA runtime launches them.

## From GTX 285 to Modern GPU Architecture

The GTX 285 material in the source is historically useful but obsolete for current interview preparation. Its main
lessons remain valid:

- threads are grouped into warps;
- many warps reside on an SM to hide latency;
- register capacity limits resident thread contexts;
- execution resources are shared by threads in a warp.

For modern NVIDIA architecture, use the **Streaming Multiprocessor (SM)** as the unit of reasoning:

```text
GPU
  -> many SMs
       -> warp schedulers / issue logic
       -> scalar and vector ALUs
       -> Tensor Cores
       -> load/store units
       -> large register file
       -> shared memory + L1/texture cache
  -> shared L2
  -> HBM
```

The exact SM resource counts vary by compute capability. Do not memorize one generation's counts as universal.

### Current NVIDIA interview note - Rubin era

As of 2026, NVIDIA Vera Rubin is in production. The CUDA programming model still uses 32-thread warps and the
same core SIMT concepts above. Current platform changes worth knowing are:

- Rubin uses HBM4 and sixth-generation NVLink;
- Blackwell remains highly relevant as the previous deployed generation, using HBM3E and NVLink 5;
- thread-block clusters, shared memory, Tensor Cores, and asynchronous data movement remain important concepts;
- exact SM counts, cache sizes, and throughput numbers are product-specific and should not be treated as invariants.

For interviews, know the execution model first; memorize product numbers only when the role specifically demands it.

## Very Long Instruction Word - VLIW

VLIW moves scheduling responsibility toward the compiler. One wide instruction encodes several independent
operations intended for different functional units.

For example, a four-slot word might encode `[integer ADD | FP MUL | LOAD | branch/NOP]`. Slot positions select
particular functional-unit paths, avoiding the dynamic alignment/steering needed to place arbitrary operations
on available units. The compiler must honor dependencies and the machine's latency/slot rules.
In a simple lockstep, interlocked implementation, an unexpected load delay can stall bundle progress and leave
other units idle. VLIW does **not** universally require all operations to finish before the next word issues:
pipelined and explicitly scheduled designs can overlap words when their documented rules permit it.

Advantages:

- simpler dynamic scheduling hardware;
- predictable issue structure;
- attractive when parallelism is statically visible.

Disadvantages:

- compiler must find enough independent work;
- code can be tied to a particular machine width/latency model;
- NOPs waste instruction bandwidth when slots cannot be filled;
- variable-latency operations and cache misses are difficult to schedule statically.

VLIW ideas remain important in DSPs and accelerator architectures, even though high-end CPUs usually prefer
dynamic scheduling.

## Loop Unrolling

Loop unrolling replicates a loop body several times per iteration.

Benefits:

- fewer branch and loop-control instructions;
- more independent operations visible to the scheduler/compiler;
- better software pipelining and vectorization opportunities.

Costs:

- larger code footprint and instruction-cache pressure;
- cleanup code for iteration counts not divisible by the unroll factor;
- excessive unrolling can increase register pressure.

Example, assuming `n >= 0` and arrays with at least `n` elements:

```c
int i = 0;
for (; n - i >= 4; i += 4) {
    c[i + 0] = a[i + 0] + b[i + 0];
    c[i + 1] = a[i + 1] + b[i + 1];
    c[i + 2] = a[i + 2] + b[i + 2];
    c[i + 3] = a[i + 3] + b[i + 3];
}
for (; i < n; ++i) {
    c[i] = a[i] + b[i];
}
```

The first loop handles complete groups of four; the scalar tail handles the remaining zero to three elements.

Unrolling does not remove loop-carried dependences. The source's coupled a/b example, with `n >= 1`,
nonzero `m`, and initialized arrays covering indices `0..n`, can be written as:

```text
# Original loop
for i = 1 .. n-1:
    a[i] = b[i+1] + (i+1)/m
    b[i] = a[i-1] - i/m

# Two bodies per iteration, retaining statement order
i = 1
while i+1 < n:
    a[i]   = b[i+1] + (i+1)/m
    b[i]   = a[i-1] - i/m
    a[i+1] = b[i+2] + (i+2)/m
    b[i+1] = a[i]   - (i+1)/m
    i += 2
if i < n:
    a[i] = b[i+1] + (i+1)/m
    b[i] = a[i-1] - i/m
```

The second body's `b[i+1]` still needs the first body's `a[i]`; reads of future b elements must also remain
before their later overwrites. The tail prevents executing an extra body when the iteration count is odd.
Unrolling reduces loop control and exposes a larger basic block, but does not make these bodies independent
like the array-add example above. This is mathematical pseudocode; numeric types determine division semantics.

## Interview checklist

Be able to explain:

- control-flow execution vs. dataflow scheduling;
- SIMD vs. vectors vs. SIMT;
- strip mining, masks, gather/scatter, and banking;
- why GPUs use many resident warps;
- divergence and memory coalescing;
- programming model vs. execution model;
- why VLIW shifts complexity from hardware to the compiler;
- how loop unrolling exposes ILP but can hurt code size and register pressure.

## References

- CUDA Programming Guide: <https://docs.nvidia.com/cuda/cuda-programming-guide/>
- Blackwell Tuning Guide: <https://docs.nvidia.com/cuda/blackwell-tuning-guide/>
- NVIDIA Rubin architecture:
  <https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/>
- NVIDIA Vera Rubin production announcement:
  <https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory>
- RISC-V Ratified Specifications: <https://docs.riscv.org/>

[figure-simd]: https://commons.wikimedia.org/wiki/File:Comparison_SIMD_vs_Vector.png
[figure-cuda]: https://commons.wikimedia.org/wiki/File:Block-thread.svg
[figure-license-4]: https://creativecommons.org/licenses/by-sa/4.0/
[figure-license-3]: https://creativecommons.org/licenses/by/3.0/
