# Lecture 15 - Nov 1

## Assignment 2b

### execv
* Replaces the currently running program with a new program

### Runprogram
* used to load and execute the first program from the menu
* execv needs to do basically the same thing.

## Review
* Want the kernel in virtual memory (easier to share data), note challenges
  1. Bootstrapping: Solve by adding an extra bit to the MMU.
  2. Sharing: Solve by overlapping virtual memories of user and kernel
* Note that the top half of memory is privileged.

## In-Class Problem: Address Translation on the MIPS

### 0x01113fa0
Note that the last 3 digits are for the offset: FA0
0x7FFFE -> 0x01113
0x7FFFEFA0

Suppose the kernel is mapped as in slide 52 of VM:
0x81113FA0 (kseg 0)
0xA1113FA0 (kseg 1)

### 0x0100a088
0x8100a088
0xa100a088

### 0x0100b014
0x8100b014
0xa100b014

## Exploiting Secondary Storage
* Up to this point have assumed that there is enough VM to store all programs.
* May have more virtual memory space than physical space available.
* Swap pages between secondary storage and memory, such that they are in memory when needed.

* Set of virtual pages in physical memory is called the **resident set**.
* The resident set will change over time.
  * Add extra bit to PTE
  | valid | Present     | Description |
  | :------------- | :------------- |:----- |
  | 1 | 1 | Page is valid and in memory |
  | 1 | 0 | Page is valid, but not in memory |
  | 0 | x | Page is invalid |

### Page Faults
* If hardware managed TLB, MMU checks the PTE, throws an exception, kernel handle.
* If software managed TLB, kernel detects the problem after TLB miss.
* To maintain high performance, need to ensure that page faults are rare.

### Replacement Policies
* **FIFO**: Replace the oldest memory pages (garbage)
* **MIN**: Optimal, requires knowledge of the future. Replace frame that won't be referenced for the longest (obviously don't know this.)
* Locality:
  * **Temporal**: More likely to access recent addresses frequently
  * **Spacial**: More likely to access nearby pages.
* **Clock**: Identical to FIFO, skip a page of use bit is set

## Summary
* Started with memory addresses are physical
* Translation
  * Paging
    * Swapping
  * Kernel Memory

* Address goes to MMU
* MMU looks up address in TLB, if not there throws an exception, handled by the kernel
