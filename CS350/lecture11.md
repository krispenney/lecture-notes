# Lecture 11 - October 18, 2016

## Assignment 2a
* See Slide Deck on Piazza

### Fork
* Process is described by a data structure
* If the child exists while the parent isn't waiting:
  * child goes into a zombie state
  * has no threads associate to it.
  * Exists until the parent asks for the exit code.
* Need to create a new thread for the child process (in order to safely pass the trap frame).
* **Pay Attention to order!!**
1. Create Process structure for child process.
  * proc_create_runprogram : to create process struct.
    * Could return NULL if out of space, need to handle this.
2. Create and copy address space.
  * as_copy() : creates a new address space, and copies the pages from old to new.
    * Could return NULL, need to kill off the old process and return -1 from fork.
  * curproc_setas to figure out how to give a process an address space
3. Assign PID to child process and create parent/child relationship.
  * PIDs must be unique and reusable.
  * Mutex, don't want multiple threads forking at the same time.
4. Create thread for the child process
  * thread_fork(): creates a new thread in the current process
    * need to move it to the new process.
  * Need to pass trapframe to child
    * Note that trapframes are associated with threads, no way to do this until now.
  * How to pass trapframe?
    * Pass the pointer between (need to be careful).
5. Child thread needs to put trapframe onto it's stack and modify it so the it returns the correct value.
6. Modify trapframe to ensure parent and child get different values.
  * Why not modify for parent?
    * The child has to start off where the parent was.
    * the child has nothing to return back into.
    * creating kernel stack from scratch, so everything needs to be done manually.

### Waitpid
* Need to figure out how to handle parent exiting before child.
* See helper macros.
* WNOHANG: Way to check if a child has actually exited, without waiting for it.

### Getpid
* return single value from struct.
* Need to make sure the first process can call get pid at all.

### \_exit
* current process to exit

## Virtual Memory

### Paging
* Divide up memory into chunks (pages), chunks of physical memory (frames).
* MMU --> handles translation.
* Add an extra bit to page table entry: to check if a page is valid, solves wasted space.

### Address translation examples (Slide 26)
| Virtual Address     | Physical     |
| :------------- | :------------- |
| v = 0x102c       | page 1, valid. 0x260c|
| v = 0x9800 | Invalid, exception |
| v = 0x0024 | Page a, valid, p = 0x0f024

| Virtual | Physical     |
| :------------- | :------------- |
| v=0x102c       | 0x1502c       |
| v=0x9800 | 0x32800 |
| v=0x0024 | 0x14024 |

### Other info found in PTEs
1. May want write protection bit, can have read-only pages.
  * If try to write to a read-only page, the MMU will throw an exception.
2. Bit to track page usage
  * reference (use) bit: has the process used the page recently (read or write)
  * dirty: changed something in memory.
  * These are set by the MMU, and read by the kernel.

### Page Table Size
* Size of page table may cause a problem.
* Where? reserve space in kernel memory for the page table (must be contiguous, unlike actual pages).
