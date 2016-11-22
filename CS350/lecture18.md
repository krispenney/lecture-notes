# Lecture 18 - Nov 15, 2016

## Assignment 3 Review

### TLB Replacement
* TLBLO_DIRTY == Entry is writable

### Read-Only Text Segment
* load_elf file, after the elf file is loaded. all entries will have the dirty flag turned on, fix this by either resetting the flag on all entries, or flush the TLB.

## Devices
* Recall using interrupts to avoid polling device registers.
* How to access drivers
    1. Special I/O instructions
    2. Treat registers as memory


