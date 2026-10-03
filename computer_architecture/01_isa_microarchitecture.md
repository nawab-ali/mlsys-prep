# 01 - ISA and Microarchitecture

Source mapping: Chapter 3, sections 3.5-3.6.6.

## 3.5 Instruction Set Architecture

An ISA is the programmer/compiler-visible interface between software and hardware.

### 3.5.1 Instruction

An instruction typically contains:

- **opcode:** operation to perform;
- **source operands:** register, immediate, or memory inputs;
- **destination:** where the result is written;
- **control fields:** size, addressing mode, predicate, rounding mode, and similar metadata.

Instruction encoding trades code density against decode simplicity and extensibility.

### Instruction processing style

| Style | Typical meaning | Example |
| --- | --- | --- |
| 0-address | Operands implicit on a stack | stack machines |
| 1-address | One explicit operand, accumulator implicit | historical accumulators |
| 2-address | One operand is both source and destination | many x86 forms |
| 3-address | Two sources plus independent destination | RISC ALU instructions |

### 3.5.2 Memory Organization

Important ISA properties:

- **address space:** number of distinct addresses;
- **addressability:** bytes per addressable location;
- **alignment:** legal or preferred placement of multi-byte objects;
- **endianness:** byte ordering within multi-byte values.

Most current general-purpose ISAs are byte-addressed. The architectural register width does not by itself determine
physical memory size.

### 3.5.3 Registers

Registers exploit temporal locality: recently produced values are likely to be reused. Key design choices include:

- number and width of architectural registers;
- general-purpose vs. special-purpose registers;
- scalar, vector, predicate, and control-register classes.

More architectural registers reduce spills but increase instruction-encoding pressure.

### 3.5.4 Programmer-Visible State

Typical visible state:

- PC / instruction pointer;
- architectural registers;
- memory address space;
- flags or condition state where the ISA exposes them;
- privilege and control state.

Microarchitectural structures such as the ROB, physical registers, predictor tables, and cache replacement state
are not part of normal ISA-visible state.

### 3.5.5 Instruction Classes

- **Compute:** integer, floating-point, logical, vector, tensor, crypto.
- **Data movement:** load, store, move, gather, scatter.
- **Control flow:** conditional branch, jump, call, return, indirect branch.
- **System:** fences, atomics, privilege, TLB/cache maintenance, exception return.

### 3.5.6 Load-Store vs. Register-Memory vs. Memory-Memory

**Load-store architecture:** arithmetic operates on registers; memory is accessed with explicit loads/stores.
RISC-V and classic RISC designs follow this model.

**Register-memory architecture:** an ALU instruction may use one memory operand. x86 is best described this way
for most ordinary integer and floating-point instructions.

**Memory-memory architecture:** an operation can directly use multiple memory operands. VAX is a classic example;
x86 string instructions provide limited memory-to-memory behavior but do not make x86 a pure memory-memory ISA.

**Correction from the source:** treating x86 simply as a memory-memory architecture is too coarse.

### 3.5.7 Addressing Modes

Common modes:

- immediate: constant encoded in the instruction;
- register: operand held in a register;
- base + displacement: `addr = base + offset`;
- indexed: `addr = base + index * scale + offset`;
- PC-relative: target relative to the current instruction address;
- auto-increment/decrement: address use also updates the pointer.

More addressing modes can improve code density but increase decode and address-generation complexity.

### 3.5.8 I/O Interface

Two common architectural mechanisms:

1. **Memory-mapped I/O:** device registers occupy addresses in the memory map. Normal load/store instructions
   access them, subject to device-memory ordering rules.
2. **Port-mapped I/O:** special I/O instructions access a separate I/O space. x86 retains `IN` and `OUT`.

MMIO dominates modern SoCs because it integrates naturally with load/store datapaths and interconnects.

### 3.5.9 Simple vs. Complex Instructions

The old RISC/CISC split is useful historically but less useful as a modern binary classification.

Complex instructions may improve code density and reduce frontend bandwidth, but they can require more elaborate
decode and sequencing. Modern x86 CPUs commonly decode complex instructions into simpler internal micro-ops.

Modern RISC ISAs also contain sophisticated vector, matrix, crypto, and compressed-instruction extensions.

### 3.5.10 Instruction Length

**Fixed-length encoding:**

- simpler fetch alignment and parallel decode;
- predictable instruction boundaries;
- potentially lower code density.

**Variable-length encoding:**

- better code density;
- more complicated boundary detection and decode.

x86 instructions are variable length from 1 to 15 bytes. RISC-V combines fixed 32-bit base instructions with
optional compressed 16-bit instructions, demonstrating that modern ISAs mix design points.

### 3.5.11 Uniform Decode

Uniform field positions simplify parallel decode and early register-file access. Non-uniform encodings trade that
simplicity for denser or more flexible instruction formats.

### 3.5.12 RISC vs. CISC

| Traditional RISC tendency | Traditional CISC tendency |
| --- | --- |
| load-store execution | register-memory operations |
| simpler, regular encodings | variable and richer encodings |
| many general registers | historically fewer registers |
| simpler addressing modes | many addressing modes |

**Modern reality:** performance is determined far more by implementation than by the historical label. High-end
RISC and x86 cores both use deep speculation, wide decode/issue, OoO execution, and large memory hierarchies.

### 3.5.13 Big Endian vs. Little Endian

For a multi-byte value:

- **little endian:** least-significant byte is stored at the lowest address;
- **big endian:** most-significant byte is stored at the lowest address.

Example: `0x12345678` at address `A`:

```text
Little endian: A:78  A+1:56  A+2:34  A+3:12
Big endian:    A:12  A+1:34  A+2:56  A+3:78
```

Endianness changes byte layout, not the numeric value held in a register.

## 3.6 Microarchitecture

Microarchitecture implements the ISA under performance, power, area, reliability, and verification constraints.

Major choices include:

- pipeline organization;
- issue width and execution units;
- register renaming and scheduling;
- speculation and branch prediction;
- cache hierarchy and prefetchers;
- memory-controller policy;
- voltage/frequency and power management.

### 3.6.1 Single-Cycle vs. Multi-Cycle Machines

**Single-cycle:** every instruction completes in one long clock cycle. The slowest instruction sets the clock
period, wasting time for short instructions.

**Multi-cycle:** an instruction uses several shorter cycles and can reuse hardware across phases. Different
instructions can take different numbers of cycles.

Pipelining goes further by overlapping stages from different instructions.

### 3.6.2 Datapath and Control

- **Datapath:** registers, ALUs, muxes, shifters, address generators, buses, and memories that transform data.
- **Control:** signals that steer the datapath for the current instruction and machine state.

Hardwired control is fast; microcoded control can simplify implementation of complex instruction sequences.

### 3.6.3 Performance Analysis

CPU execution time:

\[
T = \text{Instruction Count} \times \text{CPI} \times \text{Cycle Time}
\]

Equivalent forms:

\[
T = \frac{\text{Instruction Count}}{\text{IPC} \times \text{Clock Frequency}}
\]

Performance optimizations trade among all three terms. A deeper pipeline may improve frequency while increasing
branch-mispredict cost. Wider issue may improve IPC while increasing power and critical-path complexity.

### 3.6.4 Instruction Processing

A canonical teaching pipeline uses five stages:

1. `IF`: instruction fetch;
2. `ID/RF`: decode and register read;
3. `EX`: ALU work or effective-address generation;
4. `MEM`: data-memory access;
5. `WB`: writeback.

Real cores have more stages and often split frontend, rename, scheduling, execution, memory, and retirement.

### 3.6.5 ALU Datapath

![Simple ALU datapath](assets/alu_datapath.svg)

*Figure: Faithful teaching reconstruction of the source ALU datapath, simplified for interview review.*

A simple ALU instruction follows the core path:

```text
PC -> instruction fetch -> decode/register read -> ALU -> destination register
```

The next sequential PC is normally `PC + instruction_length`, unless control flow chooses another target.

### 3.6.6 Load-Store Datapath

![Simple load/store datapath](assets/load_store_datapath.svg)

*Figure: Faithful teaching reconstruction of the source load/store datapath.*

A load/store adds address generation and a memory access:

```text
base register + displacement -> effective address -> cache/TLB -> load or store data
```

A load produces a destination value. A store writes data and therefore has no architectural destination register.
Modern OoO cores place memory operations in an LSQ to enforce ordering and support store-to-load forwarding.

## Interview traps

- ISA width, address width, register width, and physical memory capacity are different concepts.
- x86 is primarily register-memory, not a clean memory-memory architecture.
- RISC vs. CISC is not a useful proxy for modern microarchitectural complexity.
- Fixed-length instructions simplify decode, but compressed extensions can coexist with a RISC ISA.
- CPU time depends on instruction count, CPI/IPC, and clock period; optimizing one can hurt another.

## References

- RISC-V ISA: <https://docs.riscv.org/>
- Intel architecture manuals: <https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html>
- Intel optimization manuals:
<https://www.intel.com/content/www/us/en/developer/articles/technical/intel64-and-ia32-architectures-optimization.html>
