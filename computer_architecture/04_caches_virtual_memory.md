# 04 - Caches, Coherence, and Virtual Memory

Source mapping: Chapter 3, sections 3.10-3.11.8.

## 3.10 Caches

A cache exploits **temporal locality** and **spatial locality** to reduce average memory-access latency and reduce
traffic to lower memory levels.

For a two-level hierarchy:

\[
AMAT = T_{L1} + MR_{L1} \times T_{L2+}
\]

More generally, recursively include each lower level's hit time and miss rate.

### 3.10.1 Set Associativity

![Cache address mapping](assets/cache_address_mapping.svg)

*Figure: Original reconstruction of tag/index/offset decomposition and an N-way set-associative cache.*

An address is split into:

- **block offset:** byte within a cache line;
- **set index:** selects a set;
- **tag:** identifies which memory block occupies a way.

For a cache with capacity `C`, line size `B`, and associativity `A`:

\[
\text{sets} = \frac{C}{B \times A}
\]

Higher associativity reduces conflict misses but increases hit latency, tag checks, area, and replacement complexity.

### 3.10.2 Direct-Mapped and Fully Associative

- **Direct mapped:** one possible location per block; one way per set.
- **N-way set associative:** block can occupy any of `N` ways in its indexed set.
- **Fully associative:** any block can occupy any line; effectively one set.

Direct-mapped caches are simple and fast but vulnerable to pathological conflicts.

### 3.10.3 Cache Address Translation

#### 3.10.3.1 PIPT - physically indexed, physically tagged

Translation completes before cache lookup. It avoids virtual alias problems but places TLB translation on the hit
path unless other optimizations are used.

#### 3.10.3.2 VIVT - virtually indexed, virtually tagged

Fast lookup, but difficult because of:

- **synonyms:** different virtual addresses map to the same physical address;
- **homonyms:** the same virtual address in different address spaces maps to different physical addresses;
- coherence and context-switch complexity.

ASIDs help with homonyms but not the fundamental synonym problem.

#### 3.10.3.3 VIPT - virtually indexed, physically tagged

The set lookup begins using virtual-address bits while the TLB translates the virtual page number. The physical tag
is compared after translation.

A common design constraint is to keep all index bits within the page offset so virtual and physical indexing agree:

\[
\text{cache size} \leq \text{page size} \times \text{associativity}
\]

This is a design rule for straightforward synonym-safe VIPT L1 caches, not a universal law for every implementation.

### 3.10.4 Inclusive, Exclusive, and Non-Inclusive Caches

- **Inclusive:** every line in an upper cache is also present in the lower inclusive level.
- **Exclusive:** a line resides in only one selected level at a time.
- **Non-inclusive/non-exclusive:** neither relationship is guaranteed.

Inclusion can simplify snoop filtering because a lower-level directory or tag array can represent upper-level
presence. Exclusivity increases effective capacity but complicates movement and coherence.

### 3.10.5 Cache Writes

**Write-through:** update the next level on each write.

- simpler recovery and some coherence designs;
- high lower-level bandwidth demand;
- usually paired with a write buffer.

**Write-back:** modify only the cache line and write it to the next level on eviction or coherence action.

- lower write traffic;
- requires dirty state and more complex coherence/recovery.

### 3.10.6 Allocation on a Write Miss

- **Write allocate:** fetch/allocate the line, then update it.
- **No-write allocate:** send the write downward without filling this cache.

Common pairings:

- write-back + write-allocate;
- write-through + no-write-allocate.

They are conventions, not mandatory combinations.

### 3.10.7 Classification of Cache Misses

Classic 3C model:

- **compulsory:** first access to a block;
- **capacity:** would miss even in a fully associative cache of the same capacity;
- **conflict:** additional miss caused by restricted placement.

In multiprocessors, add a practical fourth category:

- **coherence miss:** another agent's write or ownership request invalidated the line.

### 3.10.8 Improving Cache Performance

Reduce miss rate:

- larger capacity;
- greater associativity;
- better indexing/skewing/hash functions;
- better replacement/insertion policy;
- software blocking/tiling and layout changes;
- prefetching.

Reduce miss latency:

- multilevel caches;
- critical-word first / early restart;
- non-blocking caches with multiple outstanding misses;
- banked caches and parallel tag/data access;
- hit-under-miss and miss-under-miss support.

### 3.10.9 Victim Cache and Hashing

A **victim cache** is a small fully associative buffer that holds recently evicted lines. It is especially effective
against conflict thrashing in low-associativity caches.

Hashing or skewed indexing changes the mapping from addresses to sets so repeated stride patterns are less likely to
collide systematically.

### 3.10.10 Software Approaches for Higher Hit Rate

#### Loop interchange

Traverse the contiguous dimension in the inner loop.

```c
// Row-major array: good locality
for (int i = 0; i < rows; ++i)
    for (int j = 0; j < cols; ++j)
        sum += a[i][j];
```

#### Blocking / tiling

Partition work so the active working set fits in a cache level. Matrix multiplication is the canonical example.

Other transformations:

- loop fusion;
- array-of-structures vs. structure-of-arrays changes;
- padding to reduce conflicts;
- data-layout changes to improve spatial locality.

### 3.10.11 Memory Interleaving / Banking

Split a storage structure into independently accessible banks so accesses can overlap.

Performance depends on the address-to-bank mapping. A poor mapping can send a regular stride repeatedly to one bank
and serialize traffic.

Banking appears in:

- caches;
- vector register files;
- DRAM;
- scratchpad/shared memory;
- NoC buffers and distributed SRAMs.

## 3.10.12 Cache Coherence

**Cache coherence** is the single-address problem: all processors must observe writes to one memory location in a
legal, serialized way.

It is different from **memory consistency**, which constrains ordering across different addresses.

A useful coherence invariant is **single-writer, multiple-reader (SWMR)**:

- one core may hold writable ownership; or
- multiple cores may hold read-only copies.

### Snooping vs. Directory Coherence

**Snooping:** coherence requests are observed by all relevant caches, traditionally over a broadcast medium.

- simple conceptually;
- low lookup latency in small systems;
- broadcast bandwidth and tag-lookup cost limit scaling.

**Directory:** a directory tracks sharers/owner and sends targeted messages.

- avoids global broadcast;
- scales to many nodes;
- needs directory storage and more complex request/response sequencing.

### 3.10.12.1 Snoopy Coherence

A snooping cache controller watches coherence traffic and updates its local state when another requester reads or
writes a line.

Common actions:

- invalidate local copies on another core's ownership request;
- supply data if this cache owns the newest version;
- downgrade from writable to shared state when another reader appears.

### 3.10.12.2 MESI

![MESI protocol](assets/mesi_protocol.svg)

*Figure: Simplified original MESI reconstruction. Real bus/directory protocols have more transient states.*

Stable MESI states:

- **M - Modified:** valid, dirty, writable, and present only here;
- **E - Exclusive:** valid, clean, writable, and present only here;
- **S - Shared:** valid, clean, potentially present in multiple caches;
- **I - Invalid:** no valid local copy.

Important transitions:

- read miss with no other cached copy -> `E`;
- read miss with another copy -> `S`;
- local write in `E` -> `M` silently;
- local write in `S` -> ownership request + invalidations -> `M`;
- another core reads a line in `M` -> owner supplies/flushes data and downgrades.

#### Request For Ownership - RFO

An RFO or ownership request obtains writable ownership. On a miss it fetches the line and invalidates competing
shared copies. If the requester already holds `S`, an upgrade can obtain ownership without refetching the data.

#### MOESI

MOESI adds **Owned (O)**: a dirty line may be shared, with one cache designated as the owner responsible for supplying
the latest data and eventually writing it back.

**Correction from the source:** `O` does not mean the owner can freely modify while sharers remain valid. A write still
requires invalidating shared copies first.

#### MESIF

MESIF adds **Forward (F)** to select one clean sharer as the preferred responder, avoiding multiple redundant shared
responses.

### False Sharing

Two threads can update different words that occupy the same cache line. Coherence then moves ownership of the entire
line back and forth even though the logical variables are independent.

Symptoms:

- high invalidation traffic;
- poor multicore scaling;
- performance improves after padding or per-thread partitioning.

False sharing is a critical interview concept missing from the original chapter.

### 3.10.12.3 Directory-Based Coherence

A directory entry commonly tracks:

- stable coherence state;
- current owner if writable/dirty;
- set or vector of sharers.

Typical messages:

```text
GetS / Read       request shared copy
GetM / ReadEx     request writable ownership
Upgrade           already have data; request invalidation of other sharers
Inv               invalidate a sharer
Data / Ack        response and completion
```

The directory is logically centralized per line but physically distributed across slices/nodes in scalable systems.

### 3.10.12.4 Snoop Filters

A snoop filter avoids unnecessary coherence probes.

- **source-side filter:** predicts which destinations need a probe, reducing network traffic;
- **destination-side filter:** receives the probe but may avoid an expensive local tag lookup.

An inclusive last-level directory/tag structure can naturally act as a presence filter for private caches.

## 3.11 Virtual Memory

Virtual memory separates the address space used by software from physical memory placement.

Benefits:

- isolation and protection;
- sparse address spaces;
- relocation;
- sharing;
- paging and oversubscription;
- memory-mapped files and copy-on-write.

![Virtual-memory translation](assets/virtual_memory_translation.svg)

*Figure: Original reconstruction emphasizing the TLB-miss versus page-fault distinction.*

### 3.11.1 Page Fault

A page fault is an architectural exception raised because translation or permissions cannot satisfy the access.
Examples include:

- valid virtual page not currently resident;
- unmapped address;
- protection violation;
- copy-on-write page requiring OS handling.

**Correction from the source:** a page fault is not limited to "page is on disk." Some faults are resolved without
storage I/O, and protection faults may terminate the access rather than fetch a page.

### 3.11.2 Address Translation

For page size `2^p`:

```text
virtual address  = virtual page number | page offset
physical address = physical frame      | page offset
```

The page offset does not change during translation.

### 3.11.3 Page Table Entry - PTE

A PTE commonly contains:

- physical frame number;
- valid/present state;
- read/write/execute permissions;
- user/supervisor permission;
- accessed/reference bit;
- dirty/modified bit;
- cacheability or memory-type attributes;
- architecture-specific metadata.

### 3.11.4 Page Hit

Here, **page hit** means the virtual page is resident in physical memory and the mapping permits the access.
It is not the same as a TLB hit. The source's diagram shows a successful page-table lookup:

1. The processor sends a virtual address to the MMU.
2. If the translation is not cached in the TLB, the MMU obtains the PTE through a page-table walk.
3. A valid, present mapping with sufficient permissions identifies the physical frame.
4. The MMU combines the frame number with the unchanged page offset and accesses the data cache/memory.
5. The data returns to the processor without a page-fault handler or paging I/O.

```text
virtual address -> TLB miss -> page-table walk -> resident, permitted page
                -> physical address -> data cache / memory -> data
```

For a 4 KiB page, virtual address `0x1234` has page number `1` and offset `0x234`. If its PTE maps to physical
frame `0xA`, the physical address is `0xA234`. A TLB miss may require discovering this mapping, but no page-in
is necessary while that mapping remains present and permits the access.

A **TLB hit** skips the walk; a **data-cache hit** avoids fetching the requested data from a lower memory level.
Neither is required for this resident-page access to succeed. Residency alone does not override permissions:
an access to a resident page can still raise a protection fault.

### 3.11.5 Page Fault Flow

Simplified demand-paging path:

1. instruction issues a virtual access;
2. TLB miss triggers a page-table walk;
3. PTE indicates the page is not resident;
4. processor raises a page-fault exception;
5. OS selects/allocates a physical frame;
6. OS obtains the page if needed and updates the PTE;
7. TLB state is updated or invalidated as required;
8. faulting instruction is restarted.

### TLB Miss vs. Page Fault

This distinction is frequently tested:

- **TLB miss:** translation is not in the TLB; hardware/software walks the page tables.
- **Page fault:** page-table state says the access cannot currently proceed architecturally.

Most ordinary TLB misses are satisfied without an OS page-fault handler.

### 3.11.6 CLOCK Page Replacement

CLOCK approximates LRU with a circular pointer and a reference bit:

1. inspect the current frame;
2. if reference bit is `1`, clear it and advance;
3. if reference bit is `0`, choose it as a victim;
4. continue until a victim is found.

Dirty victims may require writeback before reuse.

### 3.11.7 Multi-Level Page Tables

Multi-level tables avoid allocating page-table storage for unused regions of a sparse virtual address space.

A virtual page number is split into multiple indices. Each level selects the next table until the leaf PTE yields the
physical frame.

Tradeoff:

- saves page-table memory;
- increases translation latency on a TLB miss.

Page-walk caches and normal CPU caches reduce that cost.

### 3.11.8 Translation Lookaside Buffer - TLB

A TLB is a cache of virtual-to-physical translations and associated permissions.

Key design points:

- instruction vs. data TLBs;
- multilevel TLBs;
- associativity and reach;
- page size support;
- ASIDs/PCIDs to reduce flushes across context switches.

**TLB reach** for a single page size = number of entries x page size. With multiple page sizes, effective reach
depends on how entries are distributed across sizes. Huge pages increase reach but also increase allocation
granularity and can waste memory.

## Interview checklist

Be able to explain:

- direct mapped vs. set associative vs. fully associative;
- tag/index/offset and the associativity equation;
- VIPT and why page-offset indexing matters;
- write-back vs. write-through and write-allocate vs. no-write-allocate;
- compulsory/capacity/conflict/coherence misses;
- victim cache, banking, and software blocking;
- coherence vs. consistency;
- snoop vs. directory;
- MESI, RFO, MOESI Owned, false sharing;
- virtual page, physical frame, PTE, TLB, page walk, page fault;
- why TLB miss != page fault.

## References

- Intel architecture manuals: <https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html>
- Arm architecture and AMBA coherence material: <https://developer.arm.com/>
- Stanford CS149 cache coherence:
<https://gfxcourses.stanford.edu/cs149/fall24content/media/cachecoherence/13_coherence.pdf>
- N. Jouppi, victim caches and stream buffers:
  <https://www.cs.cmu.edu/afs/cs/academic/class/15740-s18/www/papers/jouppi90.pdf>
- Intel page-fault overview:
<https://www.intel.com/content/www/us/en/docs/vtune-profiler/cookbook/2024-0/page-faults.html>
