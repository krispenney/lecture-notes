# Lecture 14 - Oct 27, 2016

## In Class Problem Multilevel Paging
* Virtual and Physical addresses: 64-bits long (bigger than real)
* Page Size is 1MB (2<sup>20</sup> bytes) --> Frame size same
* The size of a page table Entry is 16 bytes

| 12 (P_1) | 16 (P_2) | 16 (P_3) | 20 (Offset) |

1. How many bits of each virtual address are needed to represent the page offset?
* 2^20 bytes -> Need 20 bits to show where we are in the page --> offset.

2. What is the max number of entries in an individual page table?
2^20/2^4 = 2^16 = 65,536 PTE's

3. What is number of levels of page tables that will be required for virtual-to-physical translation in this system?
* 16 - bits for every level because 2^16 entries need to be addressed in a table.
* 3 levels of page tables

4. A particular process uses only 128MB (2^27 bytes) of VM, with virtual address range from 0 to 2^27 - 1. How many individual page tables, at each level, will be required to translate this Process' address space?
* Offset doesn't change what page we're in (20-bits).
* 27-20 bits = 7-bits, only changes bits in the third level.
* In P_1 - bits always zero, just one valid entry
* In P_2 - bits always zero, just one valid entry
* P_3 - 2^7 entries at this level
* 3MB in total for P_1, P_2, P_3
* 2^36 + 1 bytes

**Implication of questions** Small changes in one area typically affect other sections.

## Initializing an Address Space
* ELF Format (Executable and Linking Format)
  * Segment descriptor: describe segments that need to be loaded in, tells if it should be executable or read-only
  * Virtual address of the first instruction

### Address space segments
* Header tells what the segments and segment images (actual data)
* Contiguous Virtual address space,

* Load the segment image into where ever the ELF file tells us to, if size bigger than image set the remainder to 0.

### cs350-objdump - Tool to view ELF files

## Virtual Memory for the Kernel
Up to here always assumed that the kernel assumes physical memory. Makes it awkward to work with kernel structures.

1. Bootstrapping: How to get kernel into virtual memory, even though it helps to implement it?
  * Solutions to bootstrapping problem are architecture specific.
2. Sharing: If the kernel is in virtual memory, sharing data between kernel and applications is easier.
  * Make kernel's VM overlap with process' VM.
  * Point Kernel VM Pages to Process VM pages.
  * Some chunk of virtual memory belongs to the kernel. This is why the process' stack is inset towards the centre.
  * Memory protection: flags on pages, mark all of kernel VM pages as "untouchable" --> require privileged mode, causes an exception if trying to access in user mode.

  * 2/2 Division : Lower 2GB reserved for applications, Upper 2GB is reserved for the kernel.
    * TLB maps the user space.
    * once in kernel mode, cache kernel addresses in the TLB. User addresses stay accessible to the kernel.
    * Means that a applications can't use more than 2GB of data
