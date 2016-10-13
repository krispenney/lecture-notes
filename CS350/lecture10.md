# Lecture 10 - Virtual Memory - October 13, 2016

## Last Week: Sys Call Stack
Recall the chart on slide 19
1. Application has calls a function that requires a syscall.
2. Sys call library
3. Syscall exception (upgrade privilege), kernel exception handler, put exception code in register, handler checks the code
  * Save trap frame and load new context for kernel
  * Params for which syscall and any other data
  * Write result back into the trap frame
  * Switch trap frame and reload
4. Back to unprivileged code, back to syscall library which puts everything back to place
5. back to code

## Last Week: In class problem

### Question 1: Fork - See test.c
Creates a new process, but doesn't load a new program. Note that we don't know the exact order in which the threads will run in.

* If child goes first:
  * Child
    * A: 10
    * C: 10
  * Parent: **Note** the new process has it's own duplicated memory.
    * B: 0
    * C: 100
* (A: 10), (B: 0), (C:10), (C:100)
* ... Other possibilities.

* This is not possible:
  * C, C, B, A
  * Each thread still has to run in sequence.

### Question 2: Process Tree - See test2.c
**Insert Picture Here**x

## Virtual Memory
* Each process requires Virtual Memory and VM requires a process.

### Physical Addresses
* If physical addresses have **P** bits, maximum amount of addressable physical memory is 2^P bytes
* Each address refers to a distinct byte of memory.
* The amount of physical memory can be less than the maximum amount of memory (i.e. 2^48 ~ 256TB of memory - obviously don't actually have this much).
* This is what the kernel / machine actually deals with.

### Virtual Memory
* Every process has it's own view of memory, provided by the kernel.
* Why?
  * In order to keep them isolated from each other.
    * Processes could mess up / not agree on memory locations and cause problems.
  * Not every process will need all of physical memory.
* Virtual Memory holds process's:
  * the code
  * data
  * program stack
* Gives processes an abstraction of physical memory, that satisfies the processes expectations.
* Running applications only see virtual addresses
  * PC and stack pointer hold virtual addresses of the next instruction and stack.
  * pointers to variables are virtual
  * jumps/branches refer to virtual addresses.
* Processes are only aware / allowed to access it's own virtual memory.
  * Note that it is possible for processes to request that their virtual memory overlap with another's (thus same physical addresses), in order to share data.
### Address Translation
* Each virtual memory is mapped to a different part of physical memory.
* Need to translate virtual memory addresses into physical memory addresses.
* All real operations (loading, storage) take place in physical memory and are given back to the process.

* How to do this?
  * Could make loading and storing privileged instructions --> This is a lot of overhead (whenever load / store from stack)
  * Actually done by the hardware, using information provided by the kernel.

### Dynamic Relocation - Slide 11
* One style of virtual memory (not actually used anymore).
* Each process has
  * **An offset** (from 0x00)
  * **A limit**: How much physical space is it allowed
* hardware provides a **Memory Management Unit**
  * checks if limit < virtual address, raises an exception (not allowed to access)
  * otherwise, MMU adds the base address (offset) to the virtual address and does the lookup in physical memory.
* OS's job to ensure that each process has a separate base address and a limit.
  * OS must also change the values in the MMU's registers during each address space switch (privileged).
  * Example: need to do this when context switching to a thread in a different process.
  *
* **Properties**:
  * Each virtual address space corresponds to a contiguous range of physical addresses.
  * OS needs to track which parts of physical memory are in use, which are free.
  * Different address spaces may provide different sizes.
  * **External Fragmentation**: wasted unallocated space required because processes may expand it's memory space.

### Dynamic Relation Example

| Name | Address |
|:----------------|:-------------:|
| Bound Register | 0x0011 8000 |
| Relocation Register | 0x0010 0000 |
| Process 1: Virtual Addr | 0x000A 1024 |
| Process 1: Physical addr | 0x001A 1024 |
| Process 1: Virtual Addr | 0x0010 E048 |
| Process 1: Physical Addr | 0x0020 E048 |

| Name | Address |
|:----------------|:-------------:|
| Bound | 0x001 0000 |
| Reloc | 0x0030 0000 |
| Process 2: Virtual | 0x0001 8090 |
| Process 2: Physical | **Exception** |

| Name | Address |
|:---------------|:--------------:|
| Bound | 0x000A 1184 |
| Reloc | 0x0020 0000 |
| Process 3: V | 0x000A 1024 |
| Process 3: P | 0x002A 1024 |

### Address Translation: Paging
* The modern style of address translation.
* Each virtual address space is divided into fixed-size chunks - **pages**
* Physical address space is divided into **frames** (size of frames == size of pages)
* OS maintains a **page table** for each process. Specifies the frame in which each of the process's pages are located.
  * The mapping between pages and frames.
  * Potential for **Internal Fragmentation**: wasted allocated space.
    * If page size 32kb and process only requires 12kb, it still gets a full page whether it needs it or not.
    * This is less bad than external since processes typically won't be much smaller than a page.
  * Physical addresses may not be contiguous between pages.
* MMU has to translate virtual addresses to physical using the page table of the running process.
  * OS tells the MMU what page table to use.
  * Page table is stored in physical memory.
  * Has:
    * page table base register: the physical address of the first entry of the page table
    * page table length register: The number of entries in the page table.
  * To lookup:
    * determine page number and offset of the virtual address
    * check if page number larger than length register.
      * If so, raise an exception
    * otherwise MMU uses page table to determine the frame number of the frame the holds the virtual page, and combines the frame number and the offset to determine the physical address.
  * **See Slide 27 for addressing scheme**

### Paging Example 28 - Next Time

| Name | Process 1 | Process 2 |
| Physical 1 |  | |
| Physical 2 | | |
