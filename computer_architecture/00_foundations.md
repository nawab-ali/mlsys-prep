# 00 - Computer Architecture Foundations

Source mapping: Chapter 3, sections 3.1-3.4.

## 3.1 Amdahl's Law

If fraction `p` of execution time is improved by speedup `s`, total speedup is:

\[
S = \frac{1}{(1-p) + p/s}
\]

Key implications:

- The unimproved fraction `(1-p)` eventually dominates.
- As `s -> infinity`, maximum speedup is `1 / (1-p)`.
- Optimize the common case: a large speedup on a rare path may have little system impact.
- Parallel scaling is bounded by serial work plus synchronization, communication, and imbalance.

**Interview trap:** Amdahl's Law assumes a fixed workload. Gustafson-style reasoning instead asks how much larger
problem can be solved when resources scale.

## 3.2 Von Neumann Model

A stored-program machine keeps instructions and data in memory and executes a logically sequential instruction
stream identified by a program counter.

Core architectural state usually includes:

- program counter;
- integer, floating-point, vector, and control registers;
- architecturally visible memory;
- privilege, exception, and status state.

Modern CPUs are not physically sequential. They use pipelining, speculation, superscalar issue, out-of-order
execution, and caches while preserving the ISA-defined architectural behavior.

**Von Neumann bottleneck:** computation and memory share finite data-movement bandwidth and latency. Modern
systems attack it with caches, prefetching, vectorization, many memory channels, HBM, and near-data techniques.

## 3.3 Dataflow Model

In a dataflow machine, an operation becomes eligible to execute when its input operands are available. Ordering
comes primarily from data dependences rather than a single global program counter.

```text
A ----\
       (+) ---- X ----\
B ----/                (*) ---- Y
C --------------------/
```

Properties:

- Nodes are operations; edges carry values or tokens.
- Independent nodes can execute concurrently.
- Execution is naturally asynchronous.
- Control flow can be represented with predicates, switch/merge nodes, and synchronization tokens.

Pure dataflow machines are uncommon as general-purpose CPUs, but dataflow ideas are everywhere:

- Tomasulo-style out-of-order scheduling;
- GPU dependency tracking;
- tensor and streaming accelerators;
- task-graph runtimes.

## 3.4 ISA vs. Microarchitecture

![ISA versus microarchitecture](assets/isa_vs_microarchitecture.svg)

*Figure: Original reconstruction. ISA concepts checked against current RISC-V and Intel architecture manuals.*

### ISA

The **instruction set architecture** is the software-visible hardware contract. It defines what software can rely
on, including:

- instructions and encodings;
- registers and data types;
- addressing and memory semantics;
- exceptions, interrupts, and privilege;
- atomic and synchronization behavior;
- architecturally visible state.

### Microarchitecture

The **microarchitecture** is a particular hardware implementation of an ISA. It decides how the contract is met:

- pipeline depth and width;
- in-order vs. out-of-order execution;
- branch prediction and speculation;
- cache hierarchy and coherence;
- prefetching;
- execution-unit mix;
- clocking, power, and physical design.

The same ISA can have radically different microarchitectures. Software compatibility does not imply similar
performance.

### Interview-ready distinction

> ISA tells software **what** the machine does. Microarchitecture determines **how** a processor implements it.

## References

- RISC-V Ratified Specifications: <https://docs.riscv.org/>
- Intel architecture manuals: <https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html>
