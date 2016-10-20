# Lecture 12 - Oct 20, 2016

## Paging Problem: Simple Paging

### Question 1 : Number of Entries in Page Table
* 2^(32-12)

### Question 2 : Number of Valid Entires
* 128/4 = 32 valid entires.
* Could have internal fragmentation, but note the use of virtual memory where this doesn't matter. If it was physical would need to consider this.

### Question 3 : Translation
* 0x00001A60
  * Frame 1 --> 0x00235
  * 0x00235A60
* 0x00000fb5
  * Frame 2 --> 0x00234
  * 0x00234fb5
* 0x00004664
  * Frame 4 --> 0x00004
  * 0x00004664

### Question 4 :
* 2^(32)/(16*1024)
* Number of bits for the offset: 14-bits for offset, 32-14=18-bits for page number

## Lecture

### TLBs (Hardware managed)
* Execution of each machine instruction may have multiple memory operations
  * one to fetch instruction
  * 1+ to fetch instruction operands

* Address translation through a page table adds one extra memory operation for each memory operation performed during instruction execution.
* **TLB: Translation Lookaside Buffer**
  * small Cache of address translations contained in the MMU
  * TLB: translates Page # --> Frame #
  * When MMU needs to lookup a frame number:
    * Check cache, if found return translation.
    * Else, lookup the frame number from the Page Table, add this to TLB (kickout potentially), return frame #
    * **important**: When switching to a new address space, the kernel needs to invalidate the TLB.
      * The kernel and MMU need to agree on what a page table looks like
### TLB (Software Managed)
* Just give the MMU a TLB, let the kernel manage translation.
  * MMU just needs to understand TLB entries.
* If the TLB doesn't have a page # in cache, it raises an exception.
* Allows the kernel to manage it's TLB however it wants to.

* IF TLB Miss, raise exception, kernel handles:
  1. determine the frame number for p
  2. add (p, f) to TLB
  * Instruction that caused the exception is retried.

### A More Realistic Virtual Memory
* Lots unused space in virtual memory.
* Applications may use discontiguous **segments** of virtual memory. Each segment is contiguous.
  * Code
  * Data (grows up)
  * Stack (grows back)
* Large gap between data and stack because we want to give them room to expand.

### Segmentation
* Kernel is allowed to map memory (the page table) however it wants to.
* Let the kernel only care about segments of virtual memory.
* The kernel maintains an offset and limit for each segment, instead of a single offset and limit for the entire address space.
  * The MMU has multiple offset and limit registers, one pair for each segment.
  * Segment ID, offset within the segment (K bits for segment ID).
    * 2^k Segments
    * 2^(V-K) bytes per segment.
  * Kernel decides where each segment is placed in physical memory.
* The MMU (kernel part) - needs a relocation register and a limit register for each segment.
  * R_i - relocation offset
  * L_i - limit
* **Slide 49** Split v (instead of p)

### Segmented Address Translation Example (Process A)
* Didn't give the segment size on slide: Assume
| Limit Register | Relocation Register     |
| :------------- | :------------- |
| 0x2000       | 0x38000       |
| 0x5000       | 0x10000       |

| V_Addr | Segment     | offset | p |
| :------------- | :------------- | :--- | :--- |
| 0x1240       | 0       | 0x1240 | 0x38000 + 0x1240 = 0x39420 |
| 0xa0a0 | 1 | 0x20a0 (in segment 1) | 0x10000 + 0x20A0 = 0x120A0 |
| 0x66ac | 0 | 0x66ac | Exception |
| 0xe880 | 1 | 0x6880 | Exception |

### Problems with Segmentation
* Basically just having giant pages.
* Because stack and data will grow into each other, no way to know where to place them.

### Two-Level Paging
* What's used instead of Segmentation
* Have multiple smaller tables, instead of one large, contiguous page.
* If all PTE in a smaller table are invalid, can avoid creating the table all together.

* Addresses have 3 parts:
  1. level one page number: index directory
  2. level two page number: index page
  3. offset within the page.

* MMU's page table base register.
