# Lecture 13 - Oct 25, 2016

## Two Level Paging
* Instead of a single page table to map entire virtual memory, split the page table into multiple smaller page tables. Add a page table directory.
  * If all Page Table Entries in a smaller table are invalid, avoid creating that table entirely.

* Virtual Address has three parts (p<sub>1</sub>, p<sub>2</sub>, o):
  1. Level one page number: used to index the directory
  2. Level two page number: used to index a page table
  3. Offset within the page

### Address Translation with two-level paging
* MMU's page table base register points to the page table directory for the current process.
1. index into the page table directory with p<sub>1</sub>, gets a pointer to a 2nd level page table.
2. if directory entry is not valid, raise an exception.
3. index into the 2nd level page table using p<sub>2</sub> to find the PTE for the page being accessed.
4. if the PTE is not valid, raise an exception.
5. otherwise, combine the frame number from the PTE with **o** to determine the physical address (same as single-level paging).

### Limits of Two-Level paging
* One Goal: keep individual page tables small.
* Suppose:
  * 40-bit virtual addresses:
  * the size of a PTE is 4 bytes.
  * Page size is 4KB (2<sup>12</sup> bytes)
  * like to limit each page table's size to 4KB.
* **Problem**: For large address spaces, may need a large parge table directory. Which is the problem that we were trying to avoid by introducing a second level.
  * can be up to 2<sup>28</sup> pages in a virtual memory
  * a single page table can hold 2<sup>10</sup> PTEs
  * may need up to 2<sup>18</sup> page tables.
  * the page table directory will have to have 2<sup>18</sup> Entries.
  * If a directory entry is 4 bytes, the diretory will occupy 1MB.

## Multi-Level Paging
Allows the large directory problem to be solved by introducing additional levels of directories. 4-levels in x86-64.
* Properties:
  * Can map large virtual memories by adding more levels.
  * Individual pages tables/directories can remain small.
  * can avoid allocating page tables and directories that are not needed for programs that use a small amount of virtual memory.
  * TLB misses become more expensive as the number of levels go up, as more directories mustbe accessed to fined the correct PTE.
## Virtual Memory in OS/161 on MIPS: dumbvm
* 32-bit pages virtual and physical addresses.
* Uses a software managed TLB:
  * Raises exception on every TLB miss. --> Handled by kernel function, vm_fault
  * kernel is free to record page-to-frame mappings however it wants to.
* **vm_fault**
  * uses info from **addrspace** struct to determine a page-to-frame mapping to load into the TLB.
  * separate addrspace struct for each process
  * each addrspace struct describes where it's process's pages are stored in physical memory.
  * an addrspace struct does the same job as a page table, but the addrspace struct is simpler because OS/161 places all pages of each segment contiguously in physical memory.

``` C
struct addrspace {
  vaddr_t as_vbase1; /* base virtual address of code segment */
  paddr_t as_pbase1; /* base physical address of code segment */
  size_t as_npages1; /* size (in pages) of code segment */
  vaddr_t as_vbase2; /* base virtual address of data segment */
  paddr_t as_pbase2; /* base physical address of data segment */
  size_t as_npages2; /* size (in pages) of data segment */
  paddr_t as_stackpbase; /* base physical address of stack */
};

```

### Initializing an Address Space
