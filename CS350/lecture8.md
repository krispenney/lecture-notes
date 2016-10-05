# Lecture  8 - Oct 4, 2016

 ``` C
// queuefxer solution
// Goal avoid deadlock

#define N NUMBER_OF_QUEUES

struct queue queues[N];
// struct lock *the_big_lock; // Problem with one lock: silly to wait to completely unrelated queues

// void *lock locks[N]; // Problem with multiple: try to do i, j and j, i will try to acquire the locks in opposite order

void Transfer(int i, int j){
  // Use resource ordering
  if(i==j){
    lock_acquire(locks[i]);
  }else if(i < j){
    lock_acquire(locks[i]);
    lock_acquire(locks[j]);
  }else{
    lock_acquire(locks[j]);
    lock_acquire(locks[i]);
  }

  if(!empty(queue[i])){   
    void *value = pop(queues[i]);
    push(queues[j], value);
  }

  if(i==j){
    lock_release(locks[i]);
  }else if(i < j){
    lock_release(locks[j]);
    lock_release(locks[i]);
  }else{
    lock_release(locks[i]);
    lock_release(locks[j]);
  }
}

// Problem: Transfer(3,3); --> It will wait for itself
// A giant lock wouldn't have cared -> Add in check
 ```

 ``` C

// Problem with this: Preemption after releasing lock i, then queue[i] could be empty again, thus causing problems.
void Transfer(int i, int j){
  lock_acquire(locks[i]);
  if(!empty(queues[i])){
    if(j < i) {
      lock_release(locks[i]);
      lock_acquire(locks[j]);
      lock_acquire(locks[i]);
    }else {
      lock_acquire(locks[i]);
    }
    void *value = pop(queues[i]);
    push(queues[j], value);
    lock_release(locks[j]);
  }
  lock_release(locks[i]);
}
 ```

## Processes
* Kernel and Application code isolated. need to go into privileged mode in order to access kernel functions.

### Exceptions
* Jump to exception handler in memory.
* Handler check the exception type and handles appropriately.
* Note syscall exception type.
  * **syscall** instruction in MIPS to do this.

### Interrupts
* Waiting hardware device.

**Problem**: How to know which system call we actually want to run?

### System Call Codes
* kernel defines a code for each system call it understands.
* Place the system call code into register v0.
* The kernel's exception handler checks this code to determine which system call has been requested.

### ABI
The system call codes and code location are part of the kernel **ABI (Application Binary Interface)**. The kernel and applications must agree in order for software to work as excepted.

### System Call Parameters
System calls take parameters and return values (similar to functions).
The application places parameter value in kernel-specified locations before the syscall, looks for return value in kernel specified locations.
* Both are specified by the ABI
* More than 4 params are needed, they have to go onto the stack (where it is very complicated to get them).

### Stack Handling
If the process has complete control over the registers, it can set the stack pointer to a nonsense value, or nearly fill the stack, so that pushing onto the stack will result in an interrupt.
**Problem**: How to ensure the kernel has stack space to work with?

**Solution**: User and Kernel Stacks
* Each OS/161 process has two stacks, although it only uses one at a time.
* **User (Application) Stack): used while application code is executing.
  * Cannot be trusted (for safety)
* **Kernel Stack**: Used while the thread is executing kernel code (after an exception/interrupt)
  * Part of the kernel
  * in OS/161 : t_stack field of thread points to this stack/
  * Holds activation records for application functions.
  * the kernel creates this stack after an interrupt / exception.

### Exception Handling
1. Save the application stack pointer without changing any registers / touching the application stack
  * except for k0, k1
2. Switch the stack pointer to kernel stack for that thread.
3. Carefully save application state and the address of the interrupted instruction.
4. calls mips_trap, passing a pointer to the trap frame as a param.

* Summary
  * Jump from user stack (which we can't trust) to kernel stack (which we can.)
  * carefully save
  * mips_trap
  * run system call, modify the trap frame with the return values
  * carefully return to user code.
  * switch back to unprivileged state
  * Back to library code
  * Application sees the result that it's expecting.

## Multiprocessing
* multiple processes existing at the same time.
* All processes need to share available hardware resources.
  * each process' virtual memory is implemented using some of the available physical memory. The OS decides how much each process gets.
  * each process' threads are scheduled on to available CPUs/cores by the OS.
  * processes share access to other resources by making system calls.
* The Kernel's job to ensure that each process is isolated from each other.
  * Can have interprocess communication, only at the explicit request of the involved processes.
