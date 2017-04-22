# Lecture 22 - Nov 29, 2016

## Pathname Translation Problem
``` C
int translate(string path) {
  int components = num_components(path);
  int inumber = 0;
  for(int c = 0; c < components; ++c){
    string cur_comp = get_component(i+1, path);

    if(is_directory(dir)){
      // Is directory, get it's i number
      dir = dsearch(dir, cur_comp);
      // Couldn't find anything, throw an error
      if dir == -1 { return INVALID; }
    }else{
      // Not a directory and haven't reach the end of the path
      return INVALID;
    }
  }
  return inumber;
}
```

* **Note**: In a real OS, in the kernel you would store the inumber for the current working directory.
  * Allows for file paths that don't start from a '/' (relative)
  * Rooted paths start with '/' (absolute)
  * /.. == / (Can't go higher than root)

## In-Memory (non-persistent structures)
* Per processes
  * **Descriptor table**
    * Which file descriptors does this process have open?
    * To which file does each open descriptor refer?
    * What is the current file position for each descriptor?
* System Wide
  * Open file table
    * Can't actually delete open files, can remove hard links.
  * i-node cache: allows quick look up of recently used nodes
    * need to make sure the cache stays valid
    * need to track whether to access from the disk or from the cache?
    * May need to synchronize with disk.
  * Block Cache: Save recently used blocks.

## Reading a File (/foo/bar)
* Writing is similar
1. Read is the root i-node
  * It's at some "well known position" (i-node 2)
  * i-node 1 is usually for tacking bad blocks.
  * Tells us that this is a directory and where the data is
2. Read the data blocks corresponding to the root directory
  * Associates strings to i-number
3. Lookup foo in the i-node table
4. Read i-node
5. Lookup data that the i-node points to (for bar)
6. read i-node for bar
  * Is user allowed to access file? <-- permission check
7. Alloc a file descriptor in the descriptor table for the process that called open.
  * Set position to 0
  * Increments the open counter
  * Note that the open program doesn't actually read any of the file's data.
8. Find the data block for the file
  * May need to follow direct / indirect pointers
9. Update the i-node with a new access time
  * May need to update file meta-data on a read.
  * Depends on file system design.
10. Update the file position in the descriptor table.
11. Get the actual block of data and read it in
12. Close the file
  * Decrement the file's counter in the open file counter (which may result in deleting the file.)
  * Dealloc the file descriptor

## Creating a File (/foo/bar)
1. call the create system call
  * Would have to make sure /foo is a directory
    * Read the root i-node to find foo
    * Check if the bar file already exists in foo (this would cause a fail)
  * Search for a new i-number in the bit map
  * init the bar i-node
  * Update the foo i-node to show that foo exists
2. At this point the file exists, but it's empty. Write data.
  * Read the direct pointers from bar's i-node
  * See that all of the direct pointers are empty
  * Alloc data blocks
  * Check if free, write that it is now in use, in data bit-map.
  * Write data into the block
  * Into the i-node, assign the direct pointer to the data block.

## Problems Caused by Failures
Types:
  1. Disk failing: Not much that can be done
  2. Computer crashes while running a filesystem operation.
    * Note that a single file system operation (read / write / delete ...) have many underlying operations.
    * System failure will destroy in-memory file system structs
    * **Goal**: Make persistent structures as crash consistent as possible.
      * Choose an order of operation that reduce the chances of breaking things.

### Fault Tolerance
* Can write special-purpose consistency checkers, in order to help validate the file system.
  * Runs after a crash, before normal operations resume.
  * find and attempt to repair inconsistencies.
    * files without directories.
    * empty data blocks

## In-Class Problem:
* Key Part: seek, how many blocks need to be allocated to write the data?
  * lseek: **causes** spend a bunch of time ensure that pointers exist / file exists.
    * **But this only updates the file descriptor**
  * **write**: The full price for this will be paid.

# Interprocess Communication
* Shared memory locations
* Maps sections of virtual memory to a file.
* File driver has it's own cache 
