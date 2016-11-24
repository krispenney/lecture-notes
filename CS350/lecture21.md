# Lecture 21 - Nov 24

## File Systems
Recall: Directories don't contain files. Just a linking of string names to i-numbers. i-numbers are file data. Multiple directories can have references to the same file, so it is not reasonable to say that a file is "in" a directory. If there are no hard links left and no one has the file open, the file is deleted.
Multiple file systems work via mounting. Not obvious which file system your in via path name.

If creating a new file, need to know which i-nodes and data-nodes are free. Create bit-maps for both of these.
**Superblock**: The very first block of a filesystem. this contains meta-data about the entire filesystem.

Use i-number to index into the i-nodes, The i-node tells us which data blocks to look into. i-nodes contain various pieces of file meta-data.

### How do large files work?
* Since blocks are a fixed size, the file size is limited.
* Fix this via indirection on the i-nodes (point to another block of direct pointers).
* **double indirect pointers**: Point to a block of indirect pointers. Each indirect pointers point to a block of direct pointers.
* **Note**: The indirections are sequential, start with direct pointers, then indirect (if big enough), then double indirect (if big) ...
  * Only want to have indirection if your file is large enough.
  * Avoid the overhead if possible.
  * Price needs to be paid for indirection, in order to allocate the blocks for the levels of indirect pointers.s
* Need some sort of NULL pointer in order to determine if an indirect block actually points to something, or is NULL.
* Indirection allows a file to be stored non-sequentially on disk.

### Lots of tuneable params
* How many i-nodes should a file system have?
  * Determines how many files you can have.
* What is the "right" block size?
  * If too small, need more blocks.
  * If too big, then may waste space for small files (can't use part of a block).
* Need to tune all parameters, appropriately. Choose the default to work often.

## Directories
Directories are implemented as a specific type of file. Has data blocks that store the actual contents of the directory (the mapping from string names to i-numbers).

Only the kernel can write to a directory file, in response to a file system operation (creating a file, creating a link). This is because multiple invariants must be maintained in order to function correctly.

The Superblock contains the i-number of the root directory. This is the only way to access containing i-numbers.

## Implications
Unix, looking for a path: You may actually end up jumping to a different file system.
(For below assume one file system)
* Each i-number is an index into the i-node table.
* i-node gives meta-data for a file and pointers to the actual data.
  * For a directory, this data gives the mapping from string names to i-numbers.
  * **Don't think of files as part of a directory**
* follow down this path using the i-numbers until the file is reached.
  * If a file is large, it may have indirection pointers that point to additional data blocks (levels of indirection is in order).
  * These indirect blocks can be laid out in any order.
  * As the file expands, add more data blocks.
  * Potential for data fragmentation
  * The fact that a file has multiple links is irrelevant once you have the file, any path will give the exact same information / permissions.
  * **File-Type**: File, Directories, and special
