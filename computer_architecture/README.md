# Computer Architecture Interview Notes

Concise, research-validated notes for senior computer-architecture and ML-hardware interviews.
The material is organized into seven topic modules with descriptive headings, matching the other study directories.

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
