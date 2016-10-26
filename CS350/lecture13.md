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
* When the kernel creates a process to run a program, it must create an address space for the process, load the program's code and data into the address space.
  * OS/161 pre-loads the address space before the program runs.
  * Most OS's do this on demand - Why? -->
* A program's code anddata are described in an **executable file**, which is created when the program is compiled and linked.
* OS/161 expects exec files to be in **ELF Format** (Executable and Linking Format)
* The OS/161 execv syscall re-initializes the address space of a process:

``` C
int execv(const char *program, char **args);

```

* The **program** param ofexecv should be the name of the ELF file for the program that is to be loaded intothe address space.

### ELF Files
* ELF Files contain address space segment descriptions, which are useful to the kernel when it is loading a new address space.
* The ELF fileidentifies the (virtual) address of the program's first instruction.
* The ELF file also contains lots of other information (section descriptors, symbol table) that is useful to compilers, linkers, and debuggers, loaders and other tools used to build programs.

* Segments:
  * Header describing the segments and segment images. Has an entry for each segment which describes:
    * the virtual address of the segment start.
    * length of the segment in the virtual address space.
    * location of the start of the segment image in the ELF file (if present)
    * the length of the segment image in the ELF file (if present(.))
  * Each segment describes a contiguous region of the virtual address space.
  * The **image** is an exact copy of te binary data that should be loaded into the specified portion of the virtual address space.
    * Image may be smaller than the address space segment, in this case the rest of the address space segment is expected to be zero-filled
    * When OS/161 initializes an address space, the kernel copies segment images from the ELF file to the specifiedportions of the virtual address space.
* For OS/161 dumbvm implementation, assumes ELF file contains two segments:
  * **text segment**: containing the program code and any read-only data.
  * **Data segment**: containing any other global program data.
* ELF file does not describe the stack
* dumbvm creates a **stack segment** for each process. 12 pages long, ending at virtual address 0x7fffffff (kern/sscall/loadelf.c)

## Virtual Memory for the Kernel
* Want the Kernel to live in Virtual Memory, some challenges:
  1. **Bootstrapping**: because the kernel helps to implement virtual memory, how can the kernel run in virtual memory when it is starting?
    * Solutions are architecture-specific
  2. **Sharing**: Sometimes data needs to be copied between the kernel and application programs, how can this happen if they are in different virtual address spaces?
    * Can be addressed by making the kernel's virtual memory overlap with the process' virtual memory.

## Exploiting Secondary Storage
* Allows virtual address spaces that are larger than the physical space avaliable
  * Let pages from virtual memories be stored in secondary storage (disk, SSD)
* Allow greater multiprogramming levels by using less of the avaliable (primary) memory for each process.
  * Swap pages (or segments) between secondary storage and primary memory so that they are in primary memory when needed.

### Resident Sets and Present Bits
* When swapping is used, some pages of each virtual memory will be in physical memory, others will not.
  * The set of pages in physical memory is called the **resident set**
  * A process's resident set will change over time as pages are swapped in and out of physical memory.
* To track which pages are in physical memory, each PTE needs to contain an extra bit, **the present bit**
  * valid = 1, present = 1: page valid and in memory
  * valid = 1, present = 0: page valid and not in memory
  * valid = 0, present = x: invalid page

### Page Fault: Attempting to access a non-resident page
* When a process tries to access a page that is not in memory, the problem is detected because the page's present bit is 0.:
  * On a machine with **Hardware managed TLB**, the MMU detects this when it checks the page's PTE, generates an exception, which the kernel must handle.
  * on a machine with a software-managed TLB, the kernel detects the problem when it checks the page's PTE after a TLB miss

* When a page-fault happens, it is the kernel's job to:
  1. swap the page into memory from secondary storage, evicting another page from memory if necessary.
  2. Update the PTE (set the present bit)
  3. Return from the exception so that the application can retry the virtual memory access that caused the page fault.

### Secondary Storage is slow
* Disk access milliseconds, SSD read 10's-100's microseconds
* MEmeory access times much faster (100's of nanoseconds)

* If secondary storage is 1000 access times are 1000 times slower than memory access, then:
  * If 1/10 average accesses result in a page fault, the average memory access time with swapping will be about 100 times larger than it wold be without swapping.
  * If 1/100 average accesses result in a page fault, average memory access time is ~10 times larger than it would be without swapping.
  * If 1/1000, About 2 times larger than without swapping.
* **Implication**: The kernel needs to ensure that page faults are rare.
  * limit the number of process, ensures enough physical memory per process
  * try to be smart about which pages are kept in physical memory, and which are evicted.
  * hide latencies, i.e. by preetching pages before a process needs them.

### FIFO Replacement Policy
* When time to evict, replace the page that has been in memory the longest

### MIN (Optimal) Replacement Policy
* Replace the page that will not be referenced for the longest time (requires knowledge of the future)

### Least Recently Used (LRU) Replacement Policy

### Locality
* Real programs don't access their virtual memories randomly:
  * **Temporal Locality**: programs are more likely to access pages that they have accessed recently than paes that they have not accessed recently.
  * **Spacial Locality**: Programs are likely to access parts of memory that are closeto parts of memory they have accessed recently.
* Locality helps to keep pages faults low.

## Measuring Memory accesses
* Kernel is unaware of which pagesa program is using unless there is an exception.
* Makes it difficult for the kernel to exploit locality by implementing a replacement policy (like LRU)
* MMU can help to solve by tracking page accesses in hardware
* Add a use bit (reference bit) to each PTE
  * Set by the MMU each time the page is used
  * read and cleared by the kernel
* Use bit provides a small amount of memory usage information that can be exploited by the kernel

### The Clock Replacement Algorithm
* Exploits the use bit
* Identical to FIFO, except a page is skipped if it's use bit is set.
* The clock algorithm can be visualized as a victim pointer that cycles through
the page frames. The pointer moves whenever a replacement is necessary:
while use bit of victim is set
  clear use bit of victim
  victim = (victim + 1) % num_frames
choose victim for replacement
victim = (victim + 1) % num_frames
