# Computer Architecture Interview Notes

Concise, research-validated notes reconstructed from Chapter 3 of *Notes for Technical Interviews*, v2.2.

The source chapter spans PDF pages 74-217 and sections 3.1 through 3.18.20. The material was condensed,
corrected, and selectively modernized for senior computer-architecture and ML-hardware interviews.

## Study order

| File | Coverage |
| --- | --- |
| [Foundations](00_foundations.md) | Amdahl, Von Neumann, dataflow, ISA vs. microarchitecture |
| [ISA and microarchitecture](01_isa_microarchitecture.md) | ISA, addressing, RISC/CISC, datapaths, performance |
| [Pipelining and OoO](02_pipelining_ooo.md) | Pipelining, hazards, branch prediction, ROB, renaming, OoO |
| [Data parallelism and GPUs](03_data_parallelism_gpu.md) | Dataflow, SIMD, vectors, SIMT/GPU, VLIW, loop unrolling |
| [Caches and virtual memory](04_caches_virtual_memory.md) | Caches, coherence, virtual memory, page tables, TLBs |
| [DRAM and HBM](05_dram_hbm_memory_systems.md) | DRAM, HBM, STREAM, controllers, prefetching |
| [Multiprocessors](06_multiprocessors_interconnects.md) | Consistency, synchronization, networks, NoCs, chiplets |

## Recommended two-day skim

**Day 1:** `00` -> `01` -> `02` -> `04`

**Day 2:** `03` -> `05` -> `06`, then revisit diagrams and interview traps.

## Diagram policy

Important screenshots from the source were not copied blindly. They were converted using one of three methods:

1. Recreated as deterministic SVG diagrams in `assets/`.
2. Converted into Markdown tables, equations, or code where an image added no value.
3. Replaced by a concise modern explanation when the original figure was obsolete or misleading.

The SVGs are editable, GitHub-friendly, and were rendered during validation to check legibility and layout.

A final clean-room audit independently rebuilt the source inventory, re-rendered and visually inspected all 20
SVGs, corrected residual issues, and passed a zero-finding post-fix regression. See `AUDIT_REPORT.md`.

## Scope policy

The notes preserve the original Chapter 3 topic coverage. New material was added only when it is high-value for
modern architecture interviews. Examples include TAGE-style branch prediction, physical-register renaming,
false sharing, HBM4, acquire/release ordering, UCIe, and CXL.

## Conventions

- `IPC`: instructions per cycle.
- `CPI`: cycles per instruction.
- `MLP`: memory-level parallelism.
- `ILP`: instruction-level parallelism.
- `TLP`: thread-level parallelism.
- `DLP`: data-level parallelism.
- `ROB`: reorder buffer.
- `RS`: reservation station.
- `PRF`: physical register file.
- `LSQ`: load/store queue.
- `BTB`: branch target buffer.
- `RAS`: return-address stack.
- `TLB`: translation lookaside buffer.
- `NoC`: network on chip.

## Provenance and validation

See [Change and Validation Summary](CHANGELOG_VALIDATION.md) for corrections, sources, and diagram validation notes.
[Audit Report](AUDIT_REPORT.md) records the source package's verification claims.

The archive's conversion-only `PROGRESS.md` was not imported. Study progress remains in the existing
[Progress Tracker](../plan/04_progress_tracker.md).
