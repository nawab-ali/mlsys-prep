# Change and Validation Summary

Initial research/validation: 2026-09-28.
Independent pre-Git audit: 2026-09-29 Pacific Time.
Final clean-room audit: 2026-10-02 Pacific Time.

This collateral is a researched reconstruction of Chapter 3 rather than a literal PDF transcription. The original
coverage and interview-oriented structure were preserved, while incorrect, ambiguous, or obsolete material was
corrected or compressed.

## High-value corrections

| Area | Correction / modernization |
| --- | --- |
| ISA | Treat x86 primarily as register-memory, not simply memory-memory. |
| RISC vs. CISC | Keep the historical distinction, but emphasize modern implementation convergence. |
| Hazards | Clarify that a simple in-order five-stage pipeline normally sees RAW, not WAR/WAW hazards. |
| Scoreboarding | Replace the source valid-bit simplification with the classical centralized hazard model. |
| Branch prediction | Correct two-bit wording; separate correlation from gshare; add a short TAGE note. |
| Exceptions | Use synchronous exception vs. asynchronous interrupt as the interview-level distinction. |
| Renaming | Keep historical ROB-tag renaming, but add the modern PRF + ROB organization. |
| GPUs | Replace GTX 285 emphasis with SIMT, SM, warp, divergence, coalescing, and modern CUDA. |
| Caches | Add VIPT constraints, non-inclusive caches, coherence misses, and false sharing. |
| Coherence | Correct MOESI Owned semantics: dirty sharing is allowed, but a writer needs exclusivity. |
| Virtual memory | Explicitly distinguish a TLB miss from a page fault. |
| HBM | Replace HBM2 emphasis with HBM3E/HBM4 context; HBM4 uses a 2048-bit stack interface. |
| STREAM | Correct the official kernel name from `Sum` to `Add`. |
| DRAM | Emphasize banks, timing, DDR5, controllers, QoS, and prefetching. |
| Consistency | Add acquire/release, fences, RVWMO, and a compact modern ISA comparison. |
| Interconnects | Preserve topology/routing fundamentals; add concise UCIe 3.0 and CXL 4.0 context. |

## Independent pre-Git audit corrections

The second pass found real defects in the first delivered ZIP. They were corrected rather than waived:

- `gpu_simt_hierarchy.svg`: fixed a hierarchy error that visually implied one warp was nested under another.
- `mesi_protocol.svg`: added the missing `I -> M` write-miss/RFO path and redrew the state machine for clarity.
- `branch_frontend.svg`: corrected misleading feedback-flow presentation between resolution and prediction.
- `alu_datapath.svg`: added the promised ALU datapath figure that was absent from the first package.
- `load_store_datapath.svg`: added the promised load/store datapath figure that was absent from the first package.
- `gshare_predictor.svg`: added the promised correlated/global-history predictor figure.
- `interconnect_topologies.svg`: made fat-tree link widening explicit instead of drawing a plain tree.
- GPU current-generation note: moved from Blackwell-era wording to Rubin-era wording for 2026.
- UCIe/CXL note: updated to UCIe 3.0 and CXL 4.0 current specification context.
- HBM note: clarified HBM4 as the current production generation and retained HBM4E sampling context.


## Final clean-room audit corrections

A third, independent pass rebuilt the requirements and source inventory rather than trusting prior QA counts.
It found and corrected the following residual issues:

- Source-section inventory: corrected the count from 145 to 148 and preserved `3.10.3.1`-`3.10.3.3` headings.
- `isa_vs_microarchitecture.svg`: corrected callout arrows so the architectural contract points to the ISA layer.
- `alu_datapath.svg`: replaced ISA-specific `PC+4` wording with a generic sequential-next-PC path.
- `dram_hierarchy.svg`: clarified rank, DRAM-device, bank-group, bank, row-buffer, and cell-array hierarchy.
- TLB reach: qualified the simple entries-times-page-size formula for multiple page sizes.
- NoC: clarified that packet/flit switching is common but not part of the definition of a NoC.
- Multistage networks: separated logarithmic butterfly/omega/banyan properties from general Clos constructions.
- Memory scheduling: replaced the repository handle with the direct Rice-hosted ISCA paper PDF.

After these fixes, a fresh regression was run from frozen final bytes. No unresolved findings remained.

## Selective additions

New material is included only when it materially improves senior architecture interview preparation:

- TAGE as a modern branch-prediction mental model;
- separate physical-register renaming and ROB responsibilities;
- false sharing;
- vector-length-agnostic execution;
- independent thread scheduling and memory coalescing on GPUs;
- HBM4;
- prefetch accuracy, coverage, timeliness, and pollution;
- acquire/release memory ordering;
- UCIe and CXL.

The notes intentionally omit many research-level variants and vendor-specific microarchitectural details.

## Diagram reconstruction

All retained technical diagrams in `assets/` are deterministic SVGs reconstructed from the underlying concepts.

- `isa_vs_microarchitecture.svg`: software-visible contract vs. implementation.
- `alu_datapath.svg`: simple RISC ALU path and writeback.
- `load_store_datapath.svg`: effective-address generation and load/store path.
- `five_stage_pipeline.svg`: classic five-stage overlap and throughput.
- `branch_frontend.svg`: direction, target, BTB, RAS, next-PC selection, and resolution feedback.
- `two_bit_branch_predictor.svg`: four-state saturating counter.
- `gshare_predictor.svg`: PC/global-history XOR indexing and counter update.
- `ooo_core.svg`: rename, issue, PRF, ROB, LSQ, and in-order retirement.
- `data_parallelism_models.svg`: SIMD vs. vector vs. SIMT.
- `gpu_simt_hierarchy.svg`: grid, sibling blocks/warps, and threads.
- `cache_address_mapping.svg`: tag/index/offset and N-way lookup.
- `mesi_protocol.svg`: simplified MESI stable-state transitions, including write-miss/RFO.
- `virtual_memory_translation.svg`: TLB hit, page walk, and page-fault distinction.
- `dram_hierarchy.svg`: channel-to-bank hierarchy and row buffers.
- `hbm_stack.svg`: stacked DRAM, TSVs, package interface, and HBM4 width.
- `memory_controller.svg`: request reordering, timing, and QoS.
- `prefetching.svg`: next-line, stride, stream, and correlation concepts.
- `memory_ordering.svg`: coherence vs. consistency and message passing.
- `interconnect_topologies.svg`: ring, mesh, fat-tree, and crossbar concepts.
- `noc_router.svg`: input buffering, routing, VC/switch allocation, and crossbar.

## Diagram QA

The independent audit performed all of the following:

- rendered all 20 SVGs to PNG with CairoSVG;
- visually inspected the complete rendered set and the critical figures individually;
- compared major reconstructions against the original Chapter 3 screenshots;
- checked technical semantics against the written notes and authoritative sources;
- checked the outer image borders for clipping after rendering;
- verified every SVG parses as XML and every Markdown image link resolves;
- kept explicit white backgrounds for readability in GitHub light/dark themes.

These are conceptual teaching figures. They intentionally avoid undocumented vendor-specific topology or counts.

## Source map

Primary or authoritative references used during verification include:

- RISC-V ratified specifications: <https://docs.riscv.org/>
- RISC-V RVWMO: <https://docs.riscv.org/reference/isa/unpriv/rvwmo.html>
- Intel architecture manuals: <https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html>
- NVIDIA CUDA Programming Guide: <https://docs.nvidia.com/cuda/cuda-programming-guide/>
- NVIDIA Rubin architecture:
  <https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/>
- NVIDIA Vera Rubin production announcement:
  <https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory>
- Micron HBM4: <https://www.micron.com/products/memory/hbm/hbm4>
- Samsung HBM4E updates: <https://news.samsung.com/global/tag/hbm4e>
- STREAM benchmark: <https://www.cs.virginia.edu/stream/>
- UCIe specifications: <https://www.uciexpress.org/specifications>
- CXL specification: <https://computeexpresslink.org/cxl-specification/>

Classic research papers are cited directly in the relevant topic files where they add interview value.

## Final QA gates

The validated package is checked for:

- all 148 numbered source headings from `3.1` through `3.18.20` represented in the study files;
- Markdown image links resolving to local SVG assets;
- no Markdown line longer than 120 characters;
- all SVG files parsing and rendering successfully;
- rendered diagrams free of edge clipping;
- no temporary render/contact-sheet files in the delivered folder;
- concise interview-prep scope rather than lecture-note expansion.
