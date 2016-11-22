# Lecture 20 - Nov 22, 2016

## In Class Problem: Disk I/O
Suppose that a server has a single disk drive and one single-core processor.
Need to consider: seek time (assume average 5ms), rotation, transfer time.

* Rotation time: 100 RPS -> (1/100) 10ms
    * ~5ms - sometimes full, sometimes no rotation
* Transfer Time:
    * 1024 (2<sup>10</sup>) tracks, 2<sup>27</sup> bytes
    * Average bytes per track: 2<sup>17</sup>
    * 2<sup>12</sup> / 2<sup>17</sup>
    * 10ms -> 0.3125ms
* Total Disk Time: 5+5+0.3125 = 10.3125ms (Average time to service request)
* Cycle Time: 5ms (CPU running) + 10.3125ms = 15.3125ms
1. Suppose that k=1. Estimate the CPU utilization, i.e. the fraction of the time that the CPU is not idle.
* 5 / 15.3125 = ~32%

2. Repeat Q1, Assume k = 2
* 10 / (10.3125\*2) = ~48% Utilization
* In this case, always blocked by the disk

3. If k = 3?
* After this point, blocking by the disk

## File Systems

### File Interface
* **Open**: Returns a file identifier, which is used in subsequent operations to identify the file.
* **Close**: Removes this information.
* **Read**: copies data from a file into virtual address space.
* **Write**: copies data from a virtual address space to file.
* **Seek**: enables non-sequential reading/writing
  * Changes the file position associated with a descriptor (just a kernel data structure)
  * Next read / write start from here
* Files may have additional meta-data

### Directories and File Names
* Directories map file names (strings) to i-numbers
  * i-numbers a unique id for a file / directory (within the file system).
  * given an i-number, the system can find the actual data.
* Directories don't have files, just map names

### Links
* a **hard link**: links a name and an i-number
  * Every entry in a directory is a hard link.
* When a file is created, so is a hard link
  * Create i number in directory
  * Create hard link.
* Can have multiple links: Map multiple strings to the same number.
* When the last hard link to a file is removed, so is the file.
  * **unlink**: removes a single path name from a file.
  * When opening a file, this creates a temporary hard link. Process has the i-number.

### Multiple File Systems
* Could have multiple HDDs / Network, each have different file systems.
* Global namespace to tell which file system we're in.
* Windows: prefix path with the file system name.
* Unix: Gives the illusion of multiple filesystems, by "inserting" another filesystem inside another, **Mounting**.
  * Creates the illusion that there is just one file system,

### File System Implementation
Persistant Storage:
  * file data / meta-data
  * Directories and links
  * File system meta-data

Non-Perisient:
  * open files per process
  * memory caches

* Example
  * 256kb disk
  * 512 bytes sector size
  * 512 total sectors in disk
  * Groups every 8 consecutive sectors into a block
    * helps minimize seeks (spacial locality)
    * 64 total blocks
    
