# Pipelining, Branch Prediction, and Out-of-Order Execution

## Instruction Pipelining

Pipelining overlaps different phases of multiple instructions. It primarily improves **throughput**, not the latency
of a single instruction.

![Five-stage pipeline](assets/five_stage_pipeline.svg)

*Figure: Five-stage instruction overlap without stalls. The highlighted column is clock cycle 4.*
Source: [5 Stage Pipeline.svg][figure-pipeline] by Inductiveload, public domain.
White background and display sizing; original drawing retained.

### Basic Idea

Partition instruction processing into stages and place registers between stages. In the ideal steady state, every
stage works on a different instruction each cycle.

Ideal speedup approaches the number of balanced stages only when hazards, stalls, and register overhead are small.

### Instruction Processing Cycle

Classic stages:

- `IF`: fetch instruction;
- `ID/RF`: decode and read registers;
- `EX`: execute or generate an address;
- `MEM`: access data memory;
- `WB`: write result.

Real designs frequently separate fetch, decode, rename, dispatch, schedule, execute, writeback, and retirement.

## Data Dependences and Hazards

A **dependence** is a program relationship. A **hazard** is a pipeline situation in which that relationship could
cause incorrect execution if the machine did not stall, forward, rename, or otherwise enforce it.

### Read After Write - RAW

```text
I1: R2 = R1 + R3
I2: R4 = R2 + R5
```

`I2` needs the value produced by `I1`. RAW is a **true data dependence**.

### Write After Read - WAR

```text
I1: R4 = R1 + R5
I2: R5 = R2 + R3
```

`I2` must not overwrite the old `R5` before `I1` reads it. WAR is an **anti-dependence** caused by register-name
reuse, not by a true value flow.

### Write After Write - WAW

```text
I1: R2 = R4 + R7
I2: R2 = R1 + R3
```

The final architectural value must be from `I2`. WAW is an **output dependence**, also caused by name reuse.

**Important:** a simple in-order five-stage pipeline normally encounters RAW hazards but not WAR/WAW hazards.
WAR and WAW become relevant when instructions can read/write or complete out of program order.

### Handling Data Dependences

Main techniques:

1. stall until the value is available;
2. forward/bypass a produced value directly to a consumer;
3. dynamically schedule independent instructions around the delay;
4. rename registers to eliminate WAR/WAW name dependences;
5. use compiler scheduling where the ISA/compiler contract permits it;
6. overlap latency with another hardware thread.

**Value prediction** goes further: guess an unavailable operand and speculatively execute its consumers.
When the producer finishes, compare the actual value with the prediction. A mismatch requires replay or squash
of affected work; speculative results must not become architectural state before validation. Unlike forwarding,
this predicts a value that has not yet been produced. It is a design option, not a feature to assume in every CPU.

### Scoreboarding

The source slide reduces scoreboarding to register valid bits. That is useful as a basic readiness model but is not
classical scoreboarding.

The toy model assumes in-order admission, source operands captured at admission, and at most one pending writer
per register. Initially every architectural register has `ready=1`:

```text
if any source has ready=0, or a written destination already has ready=0:
    stall this instruction
else:
    capture the source values
    if the instruction writes a register: clear its destination ready bit
    start execution when its functional unit is available
on completion:
    write the result, then set the destination ready bit
```

For `R2 = R1 + R3` followed by `R4 = R2 + R5`, the first instruction clears `ready[R2]`; the second waits until
the result is written and that bit is set again. Checking a pending destination also conservatively prevents WAW.
WAR is avoided here by the in-order operand-capture assumption, not by readiness bits alone. Supporting delayed
operand reads or out-of-order admission needs additional bookkeeping, as in a real scoreboard or renamed scheduler.

A **scoreboard** centrally tracks:

- functional-unit availability;
- source-operand readiness;
- destination conflicts;
- RAW, WAR, and WAW hazards.

The CDC 6600 scoreboard allowed out-of-order execution while preserving correctness without register renaming.

### Data Forwarding

A consumer does not always need to wait for a producer to write the register file.

Example in a five-stage pipeline:

```text
I1: ADD R2, R1, R3   # result produced near end of EX
I2: SUB R4, R2, R5   # can receive R2 through EX-to-EX forwarding
```

Forwarding reduces stalls but adds bypass networks, muxes, timing pressure, and dependency-check logic.

A load-use dependence can still require a bubble if load data arrives too late for the next instruction's EX stage.

## Control Dependences

### Control Dependence

The frontend must choose a next fetch PC before many branches are resolved. Waiting for every branch would destroy
pipeline utilization, so processors predict control flow and execute speculatively.

### Branch Types

| Type | Direction | Target source |
| --- | --- | --- |
| Conditional branch | taken or not taken | usually PC-relative immediate |
| Direct jump | taken | encoded target / PC-relative offset |
| Direct call | taken | encoded target / PC-relative offset |
| Return | taken | predicted with return-address stack |
| Indirect jump/call | taken | register or memory-derived target |

A frontend must predict both **direction** and **target** early enough to keep instruction fetch supplied.

In the chapter's simple pipeline, without prediction:

| Branch form | Possible next PCs | Direction known | Actual target/next PC resolved |
| --- | --- | --- | --- |
| Conditional direct | Two: fall-through or target | EX, after operand comparison | Target in ID; choice in EX |
| Direct jump/call | One encoded target | Always taken once decoded | ID: compute PC + offset |
| Return / indirect | Many across dynamic executions | Always taken once decoded | EX, when target operand is ready |

These stages are illustrative. Early branch units may resolve sooner; an unready register or memory-derived
target may resolve later. A BTB or return-address stack supplies a prediction, not proof of the actual target.

### Handling Control Dependences

From simplest to most aggressive:

- stall until resolution;
- static prediction;
- compiler-filled delay slots;
- dynamic branch prediction;
- predication for short control-flow regions;
- multipath execution, rarely used broadly because of cost.

### Branch Delay Slots

A delay-slot ISA defines one or more instructions after a branch that execute regardless of branch direction.
This exposed pipeline timing to software.

A useful delay-slot instruction must preserve data dependences and be safe on **both** branch outcomes.
Do not move the instruction that computes the branch condition into its slot: the branch needs that value first.
Likewise, a load or store taken from only one path must not introduce a fault or side effect on the other path.
Prefer an independent instruction from before the branch; use a NOP when no safe candidate exists.

Delay slots replace branch-wait bubbles with useful work only if there are enough slots to cover branch resolution
and the compiler can fill them with safe, useful instructions. Unfilled slots waste work as NOPs; insufficient
coverage still leaves a control-flow penalty.

- **Deeper pipelines:** more work may be needed between branch fetch and resolution.
- **Wider issue:** several instructions per cycle are needed to keep all execution lanes busy during that interval.
- **Variable latency:** operand stalls change the interval, so a fixed slot count cannot hide every case.

The ISA's slot count is fixed; increasing hardware depth or width does not automatically increase that count.
This makes the software-visible mechanism difficult to match to different implementations.

Historical examples include classic MIPS and SPARC. Modern high-performance ISAs generally avoid architectural
branch delay slots because pipeline depth and implementation vary across generations.

### Fine-Grained Multithreading

Fine-grained multithreading switches the issuing thread frequently, often every cycle, so one thread's latency can
be hidden by useful work from others.

The special **barrel-pipeline** case spaces a thread's instructions far enough apart that only one is in the
pipeline at a time. In a fixed five-stage pipeline, five runnable threads can issue round-robin as
`T0, T1, T2, T3, T4, T0, ...`; assume the first T0 instruction completes before its next instruction enters.
This avoids overlapping same-thread data/control hazards without bypass or branch prediction for that case.
Variable-latency operations still require readiness checks or skipping stalled threads. General fine-grained
multithreading does not guarantee this spacing, nor eliminate inter-thread memory ordering requirements.

Benefits:

- tolerates branch and memory latency;
- reduces the need for aggressive single-thread speculation.

Costs:

- each thread needs architectural context;
- single-thread latency may worsen;
- there must be enough runnable threads.

GPUs use a related idea at warp granularity: the scheduler selects among many ready warps.

## Branch Prediction

### What Must Be Predicted?

![Branch front end](assets/branch_frontend.svg)

*Figure: Simplified BTB lookup and next-PC selection. Direction prediction, the RAS, and updates are not drawn.*
Source: [Branch target buffer lookup tr.svg][figure-btb] by Oguz Ergin, [CC BY-SA 4.0][figure-license-4].
Adapted with English labels, a generic PC increment, a direction-prediction caveat, a white background, and sizing.

At fetch time, the machine wants to know:

1. whether the fetched bytes contain control flow;
2. the direction of a conditional branch;
3. the target of a taken branch;
4. the target of a return.

Common structures:

- **BTB:** caches branch PCs and target addresses;
- **direction predictor:** predicts conditional taken/not-taken;
- **RAS/RSB:** predicts return targets using call/return nesting;
- **indirect-target predictor:** predicts one of multiple possible indirect targets.

A misprediction flushes wrong-path work and redirects fetch. The performance penalty grows with the time from
prediction to resolution and with frontend/backend width.

Branch identification can also be predecoded when an instruction-cache line is filled. Cached metadata marks
instruction boundaries and control-flow locations, so fetch need not perform a full decode merely to find a branch.
This is an alternative/complement to BTB-based identification, not a direction predictor: a conditional branch
still needs a taken/not-taken prediction and a target source. Invalidating modified code must also discard stale
metadata. Exact predecode bits depend on the ISA and frontend design.

### Branch Prediction Schemes

**Static:**

- always taken / always not taken;
- backward taken, forward not taken;
- compiler or profile-guided hints.

**Dynamic:**

- last-outcome predictor;
- two-bit saturating counters;
- local-history predictors;
- global-history predictors;
- gshare-like predictors;
- hybrid/tournament predictors;
- TAGE-family predictors;
- neural/perceptron-style predictors.

### Two-Bit Counter Predictor

![Two-bit branch predictor](assets/two_bit_branch_predictor.svg)

*Figure: Standard two-bit saturating-counter transitions; the outer states saturate on repeated outcomes.*
Source: [Two-bit saturating counter][figure-two-bit] by Afog / ENORMATOR, [CC BY-SA 3.0][figure-license-3].
White background and display sizing; original drawing retained.

A two-bit counter uses states `0` (SNT), `1` (WNT), `2` (WT), and `3` (ST). Increment on taken outcomes and
decrement on not-taken outcomes, saturating at `3` and `0`. Predict taken for states `2` and `3`.

The source diagram instead sends WNT directly to ST on taken, and WT directly to SNT on not-taken.
The standard counter shown here moves WNT to WT and WT to WNT, respectively.

A two-bit saturating counter provides hysteresis. From a strong state, two consecutive opposite outcomes change
the predicted direction; from a weak state, one opposite outcome suffices.

**Correction from the source:** "changes prediction after two consecutive mistakes" is only an intuition. The
exact state transition depends on the starting state.

For a general `b`-bit counter, states range from `0` to `2^b - 1`; predict taken in the upper half,
`counter >= 2^(b-1)`. Taken updates to `min(counter + 1, 2^b - 1)`; not-taken updates to
`max(counter - 1, 0)`. For `b=3`, the threshold is 4: state 7 remains 7 on taken and falls to 6 on not-taken.

### Correlated Branch Prediction

![gshare predictor](assets/gshare_predictor.svg)

*Figure: Gshare XOR indexing compared with gselect concatenation. Only part of the counter table is shown.*
Source: [Gshare branch predictor tr.svg][figure-gshare] by Oguz Ergin, [CC BY-SA 4.0][figure-license-4].
Adapted with English labels, separate XOR inputs, a table-size clarification, a white background, and sizing.

A two-level predictor uses branch history to select a prediction counter.

- **Local history:** history of one branch.
- **Global history:** outcomes of recent branches across the program.
- **gshare:** indexes a pattern table with `PC XOR global_history` to reduce destructive aliasing.

The source slides combine correlated prediction and gshare. They are related but distinct concepts.

#### Worked example: one branch helps predict another

Consider the source's two consecutive conditions:

```text
if (d == 0): d = 1
if (d == 1): execute the second if-body
```

The compiled branches **skip** their respective if-bodies: `b1` branches when `d != 0`; `b2` branches when
`d != 1`. Taken/not-taken therefore refers to the machine branch, not the truth of the source-level condition.

| Initial `d` | `b1` | `d` before `b2` | `b2` |
| --- | --- | --- | --- |
| 0 | Not taken | 1 | Not taken |
| 1 | Taken | 1 | Not taken |
| 2 | Taken | 2 | Taken |

If `b1` is not taken, `b2` is always not taken: the first if-body has just set `d = 1`. If `b1` is taken, either
outcome is possible for `b2`. Global history exposes this correlation; it does not make every prediction certain.

An **`(m, n)` correlating predictor** uses the last `m` branch outcomes to select among `2^m` banks of `n`-bit
counters, with branch-address bits selecting an entry within a bank. A `(2, 2)` predictor has four history banks
(`00`, `01`, `10`, `11`), each holding two-bit counters. The selected counter is trained on the actual outcome,
which is also shifted into history. This banked design is distinct from gshare's XOR indexing.

For a history register of width `h`, keep only its most recent `h` outcomes:

```text
history = ((history << 1) | taken_bit) & ((1 << h) - 1)
```

For `h=4`, history `0110` followed by taken becomes `1101`; another taken becomes `1011`, discarding the oldest bit.
In a toy gshare table, branch PC index `1011` XOR prediction-time history `0110` selects counter `1101`.
Save that selected index with the branch, then train **that counter** when its actual outcome is known; recomputing
with a subsequently changed history could train the wrong entry. A speculative predictor may shift predicted
outcomes early and restore a checkpoint on misprediction; this simple update describes resolved history.

#### Modern interview note: TAGE

TAGE uses multiple tagged predictor tables indexed with different geometric history lengths. It chooses the
longest-history matching entry and falls back to shorter-history/base predictors when needed.

Why it matters:

- captures both short- and long-range correlations;
- controls aliasing with tags;
- is a useful mental model for modern high-accuracy conditional prediction.

Do not assume a commercial CPU implements the academic TAGE design exactly unless the vendor documents it.

### Branch target prediction

Direction accuracy alone is insufficient. Frontends also need low-latency target prediction for:

- direct taken branches;
- indirect jumps and calls;
- returns.

Modern indirect predictors may use branch history. Returns are commonly handled by a hardware return stack.

## Multi-Cycle Execution

Different operations have different latencies:

- integer ALU: often short;
- multiply/divide: longer;
- floating-point/vector: multi-cycle and frequently pipelined;
- loads: variable because of the memory hierarchy.

Multiple independent functional units let unrelated instructions execute while a long-latency operation remains
in flight.

Multi-cycle units may themselves be **pipelined or non-pipelined**:

- **Pipelined:** can accept a new independent operation before the previous one finishes. Latency is the time
  to produce a result; the **initiation interval** is the minimum spacing between new operations.
- **Non-pipelined:** cannot start another operation on that unit until the current one finishes.

For a teaching example, a three-cycle unit with initiation interval one can start operations in cycles 1, 2, and 3.
A non-pipelined three-cycle unit starts them in cycles 1, 4, and 7. Both have three-cycle latency, but different
throughput. Sharing a unit or waiting for dependent operands can still prevent overlap.

## Exceptions, Precise State, and Retirement

### Exceptions vs. Interrupts

**Exception:** synchronous with an instruction, such as page fault, illegal instruction, divide fault, or breakpoint.

**Interrupt:** asynchronous external or timer/device event delivered between architectural instructions.

Some architectures use broader terminology, but synchronous vs. asynchronous is the useful interview distinction.

Detection and delivery are different:

- **Precise instruction fault:** record it when detected, but enter the handler only when the instruction is
  non-speculative and reaches the architectural exception boundary. In an ROB design, this is at the head;
  faults from discarded wrong-path instructions are not delivered.
- **Ordinary maskable interrupt:** may remain pending until a permitted instruction boundary, subject to
  interrupt-enable, masking, and priority rules. It need not be serviced at the instant the device requests it.
- **Urgent hardware event:** nonmaskable interrupts and critical hardware-error or power-fail notifications
  follow their own ISA/platform delivery rules. On x86, a machine check is an exception, not an ordinary interrupt.

### Precise Exceptions

At the architectural exception boundary:

1. all older instructions appear completed;
2. the faulting instruction is identified precisely;
3. no younger instruction has modified architectural state.

Precise state enables restart, debugging, virtual memory, and robust OS exception handling.

### Reorder Buffer - ROB

![Out-of-order core](assets/ooo_core.svg)

*Figure: Modern PRF-based teaching core. Result data and ROB completion/retirement are separate paths.*

The ROB tracks instructions in program order while execution may complete out of order.

Typical ROB metadata:

- destination mapping or completion information;
- exception status;
- branch/speculation state;
- age/order information.

Instructions **retire/commit in order** when the oldest instruction has completed without an unresolved exception.

### Register Renaming

Architectural registers are names. False dependences occur when unrelated values reuse the same name.

Rename maps architectural names to a larger pool of physical destinations:

```text
Architectural R5 -> Physical P37
later write R5   -> Physical P82
```

Effects:

- removes WAR anti-dependences;
- removes WAW output dependences;
- preserves RAW true dependences by linking consumers to the producer's physical register or tag.

The source describes renaming directly to ROB entries, which is historically valid. Many modern OoO cores instead
use a separate physical register file while the ROB primarily provides ordering and retirement.

### In-Order Pipeline with ROB

An ROB does **not** by itself imply out-of-order issue. In this teaching design, instructions start execution in
program order, but different functional-unit latencies allow them to **finish out of order**.

```text
fetch -> decode / dispatch -> execution units -> completion / ROB -> retire
         in program order     variable latency   may be unordered   in order
```

| Phase | What happens |
| --- | --- |
| Decode / dispatch | Allocate an ROB entry; wait for operands and an available execution unit. |
| Execute | Start instructions in order; operations of different latencies may overlap. |
| Complete | Write the result and exception status to the instruction's ROB entry. |
| Retire | At the ROB head, commit a completed, non-faulting instruction; handle faults precisely. |

In this **result-in-ROB** model, decode uses the current producer mapping to obtain each source operand:

- No pending producer: read the committed value from the architectural register file.
- Producer has completed: read its ready result from the ROB, even if it has not retired.
- Producer has not completed: wait for its result; this in-order design stalls dispatch rather than bypassing it.

For example, an add has produced `R2 = 6` in its ROB entry but is waiting behind an older multiply to retire.
The next instruction, `R4 = R2 + 1`, can read that `6` from the ROB and produce `7`; it need not use the stale
register-file value or wait for the add to retire. A modern PRF-based core gets speculative values from physical
registers or bypass paths instead; the diagram above depicts that different organization.

An independent short add can finish before an older long multiply, but must wait behind it in the ROB to retire.
If the next instruction cannot start, younger instructions cannot bypass it at dispatch in this design.
The dynamically scheduled design below removes that issue-order restriction. Stores become architecturally
committed at retirement; their data may drain from a store buffer later under the memory-ordering rules.

### Dynamic Instruction Scheduling - Tomasulo

Tomasulo-style scheduling tracks operand readiness with producer tags and wakes consumers when values become
available.

Core concepts:

- reservation stations or issue queues buffer waiting operations;
- rename tags identify producers;
- completed results wake dependent consumers;
- independent operations may bypass stalled older operations;
- a load/store queue handles memory dependences and ordering.

A classic common-data bus broadcasts results. Modern designs use more distributed wakeup/select and bypass
networks because a single global broadcast does not scale well.

A modern ROB-based organization is:

```text
fetch -> decode -> rename -> dispatch -> issue -> execute -> writeback -> retire
                 program order          out of order            program order
```

The frontend establishes program order and renames dependencies. The scheduler chooses ready instructions based on
operand and resource availability. Retirement restores the appearance of sequential architectural execution.
Classic Tomasulo did not include an ROB; adding one supports speculation and precise in-order retirement.

#### Reservation-station walkthrough

The source's six-instruction example uses producer tags `x`, `a`, `b`, `c`, `y`, and `d`:

```text
x: R3  = R1 * R2
a: R5  = R3 + R4
b: R7  = R2 + R6
c: R10 = R8 + R9
y: R11 = R7 * R10
d: R5  = R5 + R11
```

Initially, `R1=1`, `R2=2`, `R4=4`, `R6=6`, `R8=8`, and `R9=9`. Each source operand is stored as either
a ready value or a tag naming its producer. Capture source mappings **before** changing the destination mapping.

Logical snapshot after all six instructions have been renamed, before any result broadcasts:

| Tag | Destination | First operand | Second operand | Ready to execute? |
| --- | --- | --- | --- | --- |
| `x` | `R3` | 1 | 2 | Yes |
| `a` | `R5` | Wait for `x` | 4 | No |
| `b` | `R7` | 2 | 6 | Yes |
| `c` | `R10` | 8 | 9 | Yes |
| `y` | `R11` | Wait for `b` | Wait for `c` | No |
| `d` | `R5` | Wait for `a` | Wait for `y` | No |

This is a dependency snapshot, not a cycle-accurate timing claim. It assumes enough reservation stations;
actual execution also depends on functional-unit and result-bus availability.

```text
x (1 * 2) -> a (x + 4) -----------------> d (a + y) -> final R5
b (2 + 6) ----+
              +-> y (b * c) ------------+
c (8 + 9) ----+
```

1. Allocate a free reservation station and record values/tags; stall allocation if none is free.
2. Operations `x`, `b`, and `c` are ready; `b` and `c` may bypass the older blocked operation `a`.
3. Broadcast `(x, 2)`: `a` captures `2`, becomes ready, and can produce `6`.
4. Broadcasts `(b, 8)` and `(c, 17)` supply both operands of `y`, which can produce `136`.
5. Broadcasts `(a, 6)` and `(y, 136)` wake `d`, which produces the final `R5 = 142`.

Steps 3 and 4 may interleave; dependencies, not this list's order, determine readiness. Each result must win
result-bus arbitration before it broadcasts, and a tag must not be reused while consumers still need its result.

**Why renaming matters:** after allocating `d`, the latest producer for `R5` is `d`, but `d`'s first source still
refers to `a`. In classic Tomasulo, broadcasting `(a, 6)` updates waiting consumers but not architectural `R5`,
whose current tag no longer matches `a`. Broadcasting `(d, 142)` finally updates `R5`. Thus the two writes do not
create a WAW hazard, and the true RAW dependence from `a` to `d` remains intact.

With an ROB, results instead update their assigned speculative destinations and retire in program order.

#### Load/store buffering and memory dataflow

In the classic teaching datapath, the instruction unit allocates reservation stations and load/store buffers;
register values or producer tags supply their operands. Memory operations join the same producer-consumer flow:

- **Load buffer:** holds a load until its address is ready and memory-dependence checks allow the read.
  The returned value and its producer tag enter the result-broadcast path, supplying waiting reservation stations,
  matching register entries, and store-data buffers.
- **Store buffer:** retains the address and either a ready data value or a tag for its pending producer.
  A matching broadcast supplies the missing data. With an ROB, address/data readiness is not permission to write:
  the store must commit before its data can drain to memory under the memory-ordering rules.

For `R6 = MEM[R1]` followed by `MEM[R2] = R6`, the store saves the load's tag while waiting for its data.
A broadcast `(load_tag, 42)` lets the store buffer capture `42` directly; it need not reread the register file.
The store still needs its address and, in the speculative ROB-based design, commitment before becoming visible.

Multiple buffer entries support **memory-level parallelism (MLP)**: independent loads with ready addresses can
have overlapping memory requests instead of waiting for each previous load to finish. This requires support for
multiple outstanding requests in the memory system; buffer capacity, dependencies, and cache/memory resources
limit the overlap. Register renaming alone does not resolve memory-address dependencies.

## Interview checklist

Be able to explain, without notes:

- why pipelining increases throughput but introduces hazards;
- why RAW is real while WAR/WAW are name dependences;
- forwarding vs. stalling;
- BTB vs. direction predictor vs. return stack;
- two-bit counter and gshare;
- why deeper pipelines make branch prediction more important;
- ROB vs. rename map vs. PRF vs. reservation stations;
- how OoO execution still delivers precise exceptions;
- why loads/stores need an LSQ even after register renaming.

## References

- Intel optimization manuals:
<https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html>
- Intel architecture manuals: <https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html>
- A. Seznec, *A New Case for the TAGE Branch Predictor*:
  <https://www.cs.cmu.edu/~18742/papers/Seznec2011.pdf>
- D. Jimenez and C. Lin, *Dynamic Branch Prediction with Perceptrons*:
  <https://www.cs.utexas.edu/~lin/papers/hpca01.pdf>
- Bruce Jacob, *An Out-of-Order RiSC-16*: [historical ROB operand sourcing][rob-operands].
- University of Edinburgh, HASE Tomasulo model: [tagged results and store-data buffering][tomasulo-memory].

[rob-operands]: https://user.eng.umd.edu/~blj/risc/RiSC-oo.1.pdf
[tomasulo-memory]: https://www.icsa.inf.ed.ac.uk/research/groups/hase/models/tomasulo/tomasulo.html
[figure-pipeline]: https://commons.wikimedia.org/wiki/File:5_Stage_Pipeline.svg
[figure-btb]: https://commons.wikimedia.org/wiki/File:Branch_target_buffer_lookup_tr.svg
[figure-two-bit]: https://commons.wikimedia.org/wiki/File:Branch_prediction_2bit_saturating_counter-dia.svg
[figure-gshare]: https://commons.wikimedia.org/wiki/File:Gshare_branch_predictor_tr.svg
[figure-license-3]: https://creativecommons.org/licenses/by-sa/3.0/
[figure-license-4]: https://creativecommons.org/licenses/by-sa/4.0/
