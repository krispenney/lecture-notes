# Lecture 17 - Nov 10

## Scheduling
* Balance of fairness, responsiveness, efficiency.
* Can't have all of them perfectly, trade-offs.

### Multi level feedback example

| | Queue     | R.T | Blocked? |
| :------------- | :------------- | :-- |
| T1 (Interactive) | | 9 | yes |
| T2 | - | 5 | DONE |
| T3 | - | 5 | DONE |
* Total runtime: 19 time units

### Linux Completely Fair example

|  | Weight | Real R.T | Virtual R.T | Blocked? |
| :------------- | :------------- | :-- | :-- |
| T1 (Interactive) | | 6 | 11.1 | YES |
| T2 | - | 5 | 9.5 | DONE |
| T3 | - | 5 | 12.7 | DONE |

* Notice how the distribution of Real R.T was more fair then the previous example.

## Scheduling on Multi-Core CPUs

### Pre Core Ready Queues
* Keep threads on same core
* No need for synchronization
* Simultaneously schedule
* Uneven distribution of threads to cores. Can be very unfair. Could have idle threads unnecessarily.

### Shared Ready Queues
* Use one Queue for all cores.
* Now have to worry about synchronization.
* Better scale, for efficient use of resources
* All threads have equal access to all cores.
* **Contention** access to ready queue is a critical section.

### Cache Affinity:
* When CPU (each core) accesses a physical memory address, it is cached
* If uses shared queue, cache is lost, or is lost.
* Threads develop an **Affinity** for a particular core, cached data is likely to be there.
* Per Core Queues: all threads in a particular queue have affinity for the same core.
* Shared queue doesn't benefit from this.

### Load Balancing
* Want to ensure a good distribution of thread load between threads.
* Need to do this occasionally, to keep core affinity.
* Per-Core Queue:
  * If a core's queue decides that it's overloaded, it may look at another threads queue and migrate a thread.
  * Deadlock is a concern. Two threads may look at each cores thread at the same time.


## Devices and I/O
* Need to be handled by the OS, requires privilege.
* Can't have random applications messing with hardware uncontrolled.

### Devices Example
* Timer/clock
* Disk Drive
* Serial Console
* Network Interface

### Device Registers
* Devices have registers of fixed sizes that allow for communication between OS and hardware.

### Device Driver
* a part of the kernel that interacts with a device.
* Typically loaded into the kernel, has privilege.
* **Polling** Kernel driver repeatedly checks device status.
  * Wasting time, can't run other threads.

**Can use interrupts to avoid polling**
* read / write data
* wc_sleep and be woken up when the hardware status is complete.
* Other threads are now available to run on this core.
* New thread will be interrupted at some point and jump to the interrupt handler to wake up the sleeping thread.

### How to Access Devices?
1. Special I/O instructions - x86
  * Device registers are assigned "port" numbers
  * instructions transfer data between a specified port and a CPU register.
2. Memory Mapped - I/O - Modern
  * each device register has a physical memory address.
  * device drivers can read or write to device registers using normal **lw** and **sw** instructions.
  * Appears as accessing normal memory.
  * Must agree on ranges of memory.
