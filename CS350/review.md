# Final Review Class
* File exam is cumulative

## In Class Problem: File Systems
``` C
  char x[1000];
  lseek(f, 10500, SEEK_SET);
  write(f, x, 1000);
  read(f, x, 1000);
```
* Seeking means that there must be 10500 bytes
* **lseek**: updates the file location in the descriptor
  * The cost of the seek could be put here.
  * 0 reads
  * 0 writes
* **write**
  1. read the i-node
  2. read the free data block list
  3. write free data block list (12 blocks ceil(11588/1024))
  4. Write direct pointers + indirection pointer
  5. write indirect block, pointer to new block
  6. 12x write data block
  * 2 reads
  * 15 writes (without cache), 0 writes (if using the cache), 4 (if file system has holes)
* **read**
  1. read i-node
  2. error
    * The location after the write is at the end of the file there is nothing to read at this point.
  * 1 read (no cache)
  * 0 reads (cache)

## Threads
## Synchronization
* Load linked and store conditional
  * ll %2, %3: loading a word into a register, cpu remembers the address of the most recent load linked.
    * if someone else touches that address in between, sc will fail
  * sc %1, %3
    * store into address, if and only if no one has touched the load linked address.
  * Want to change a register atomically
## System Calls
## Processes
* The core of modern operating systems.
* Gives you:
  * address space (relation to VM)
    * Accessed through MMU -> TLB
    * Possibility for vm_fault if we don't know the mappings
    * paging: looks through page table and updates the TLB (or discovers page isn't present loads from disk)
      * Swapping
        * I/O (Blocking)
          * Perform a context switch, a new process
          * bring back when the data has loaded.
  * file descriptors (filesystems)
    * Direct access to the file system
    * i-numbers
      * i-nodes
        * I/O (Blocking) - to the i-node itself
        * data blocks (I/O, Blocking)
  * threads
    * kernel is able to view threads independently
    * Scheduling
      * Preemption
        * Timer device (interrupts)
    synchronization
      * atomic operations in hardware
        * blocking
  * run in user mode (lack kernel privilege)
    * Use a system call to break out.
      * kernel mode
## Virtual Memory
* TLB vs. Memory Cache.
  * Memory Cache.
    * Physically closer to the CPU
  * TLB
    * If page table is in memory, will make use of memory cache
    * TLB is small cache in the MMU, can lookup in one shot (even for multi-level page table).
    * Software managed TLB, the TLB is the direct line of communication with the MMU.
## Swapping
* Idea: More processes loaded than can fit into virtual memory.
* A page can be valid and present: page is valid and in memory
* Can be valid and not present: page is valid, and not in memory (i.e. stored on the disk)
* If it's not valid, present doesn't matter.
* **Problem**: Swapping things in and out. Need a replacement policy
  * **FIFO**
  * **Optimal**: Replacing the page that will not be referenced for the longest times
    * Impossible
  * **Clock replacement Alg.**: Like FIFO, but adds a use bit. Gives a second chance to stay in memory.
## Scheduling
## I/O
* kseg1
  * Devices and device registers are memory mapped on MIPS.
  * device registers have a physical memory address.
  * kseg1 is uncached: access devices devices through here.
  * kseg0 is cached: access kernel memory through here.
  * kseg0 and kseg1: Mapped to the same memory space.
## Disks
## Filesystems
* i-numbers: every file is really just an i-number, an index into an array (i-node), which point to data.
  * Multiple file names can map to the same i-node.
* i-node contains file meta-data and references to the actual file data.
* directories are a special type of file that maps string file names to i-numbers.
