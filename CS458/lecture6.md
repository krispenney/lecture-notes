# Lecture 6 - May 22, 2018

## Spectre

### speculative execution
- CPUs will evaluate certain branches while waiting for the results of other instructions.
- Store the result in the cache
- CPU may take the branch, thereby using the result in the cache.

### Attack
```C
if (x < array_1_size) {
  y = array_2[array_1[x]]
}
```
- Have some secret array, somewhere in memory (ex. a password buffer)
- have a variable `array_1_size` that is uncached
- via speculative execution, it will lead to a particular index of array2 being stored in the cache. Then next reads to that index will be faster, due to the cache.
  - bounds checking (into kernel memory space), that should have happened, didn't.
- **Side Channel**: a secret that was leaked into the cache that was not supposed to be leaked.
- **Covert Channel**: Information hidden in an observable channel.

## Operating Systems
- allow multiple people to access different resources, on the same machine.

### History
- multiple users to use the same hardware
- **sequentially**: One after the other
  - executives
- **Interleaving**: Multiple
  - monitors
- OS makes resources available to the user, restricts based on some policy.
  - protects users from themselves / other users
  - One process shouldn't be able to damage another.
- Protected objects:
  - memory: processes in differenet memory spaces
  - data: home directories protected
  - CPU: one process can't starve the CPU

#### Separation
keep one user's object separate from other users

- **physical**: different physical resources for different users
  - expensive and inefficient
- **temporal**: execute different users programs at different times
- **Logical**: users are given the impression that no other users exist
  - as done by the operating system
- **Cryptographic**: Encrypt the data, make it unintelligble from other users.

#### Sharing
- sometimes users want to share resources
- flexible sharing (i.e. not all or nothing)
  - define which files other processes / resources can access
  - limited time
  - whether things can be shared,
  - Use cases
    - can do read, but not write
    - can't do read, but not print (could just take a picture)
    - maybe just aggregates.

### Memory Address Protection
- prevent one program from corrupting other programs / data
- Os can exploit hardware support
  - i.e. MMU

#### Protection Techniques
- Fence Register
  - raise an exception if memory access was below the address in the fence register
  - assuming single-user OS only
  - what if a buffer overflow?
    - the process could destroy itself, but the OS / kernel space would be fine.
- Base/Bounds
  - If a process tries to access any memory, check if it is within the bounds
  - different values for each user program, prevent destroying other processes.
  - problems: limited flexibility
    - Process A wants to share memory with Process B, can't happen
- Tagged architecture
  - each memory word has additional bits that indicate the access rights to that word
  - problem: large overhead for each word.
    - hard to port OS to new hardware
- Segmentation
  - each program has multiple address spaces
  - segments for code, data, stack
  - allows definition of some parts as sharable, private, etc.
  - Segmentation table keeps track
    - Base address, offset
  - Can result in fragmentation
    - certain areas remain free as program quits
    - some segments may not be able to fit in the gaps
  - advantages
    - hardware is fast
    - can share data with other processes (logical separation)
    - define access rights to segment
  - disadvantages
    - external fragmentation
    - segments have dynamic lengths, out of bounds checking expensive.
    - user defined names, matching is difficult
- Paging
  - Pages: virtual address space is divided into equal size chunks
  - Frames: physical memory divided into equal size chunks
  - Frame Size == Page Size
  - advantages
    - each address reference checked by hardware
    - share access to a page
    - access rights for pages
    - pages can be stored in disk, to be loaded later
  - disadvantages
    - internal fragmentation
      - if the page size is smaller than the frame size, it won't fill the full space
    - Can't assign different levels of protection for different variables, can only do it at the page level.

Modern OS's use both segmentation and paging,
- Memory protection bits indicate no access, read/write permissions, read-only
- no exec bit, prevents execution of elements stored on the stack.
  - **does it prevent all buffer overflows?** No, using [return oriented programming](https://en.wikipedia.org/wiki/Return-oriented_programming#Return-into-library_technique).

### Access Control
OS has many resources with access control, follows some policy to do so.

Goals
1. check every access
2. enforce least privilege: assign the fewest number of permissions required to perform the task.
3. Verify acceptable use: limit types of activity that can be performed on an object.
  - maybe can push or pop, but not clear the data structure

#### AC Matrix
- Set of protected objects
- set of subjects
- intersection is access rights

| Users / Files | F 1 | F2 | F3 |
|-|-|-|-|
| Alice | orw | rx | o |
| Bob | r | orx | - |

Rarely implemented in modern OS
- Really big, there may only be 2 users, but many files

#### AC List
- Each object has a list of subjects and their access control rights.
- column-wise view of the matrix
- determine the set of allowed users per object
  - fast, go though all items of the list
- determine set of objects the user can access
  - slow, need to go through all
- Revoke a user's access rights to an object
  - fast, go through the list from that object
  - If all object: slow

#### Capabilities
- A row-wise view into the matrix
- unforgeable token that gives it's owner access rights
  - if they are forgeable then there's issues
  - could change access rights (password file)
- crypto schemes
- determine the set of allowed users per object
  - look at all of the tokens for that object
  - slow
- determine set of objects the user can access
  - fast, go through the tokens that the user has.
- Revoke a user's access rights to an object
  - fast, go through the tokens that the user has
  - all: fast, same as above

#### ACL + Caps
- Used to leverage the performance benefits of each
- each file has an ACL, checked when opening
- problems
  - suppose a user gets access to a particular resource at login
  - after login, their access is revoked
  - since they have the token, they can still access until logout, when their token is revoked.
  - Related TOCTTOU
    - don't check references
    - everything should be checked to ACL, but performance problems

#### Role-based Access Control (RBAC)
- many users with the same capabilities
- role: student, prof, developer, etc
  - Profs can see student's grades
- instead of changing everything, simply change someone's role
  - when a developer becomes a manager, update their role

##### Hierarchical Extension
- Manager is an employee
- TA is a student
- Users have multiple roles, can different depending on the project / job

##### Separation of Duty
- A payment needs to be signed by an employee and a manager (must be different people)
