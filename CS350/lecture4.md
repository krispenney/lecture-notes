# Lecture 4 - Sept 20, 2016: Synchronization

## Last Thread Excerceise
* Quantum Q never actually matters in these examples.
* **Part 1**
  * Thread 1 runs for C time, because C < Q Thread 1 won't be preempted
  * Thread 2 runs for C time
  * After S time, Thread 1 runs for C time again
  * N\*(C+S) + C
  * 1: |--C--|---S---|--C--|---S---|--C--|
  * 2: |-----|--C--|---S---|--C--|---S---|
  * Extra C for hanging sleep time at the very end while thread 2 finishs for sleepsing
* **Part 2**
  * S < C < Q
  * 1: |--C--|--S--|--C--|--S--|
  * 2: |-----|--C--|--S--|--C--|
  * 2CN + S (S for hanging sleep time
## Lecture 
  * Recall add, sub volitile example and problems with accessing the same resources with multiple threads.
  * Race condition occurs: not synchronized.
  * Solutions
    * Don't use premption - problems, also yeild when blocking
    * **Mutual Exclusion**
      * identify critical sections in the program, only allow one critical section to run at any given time. 
      * Could set this up as a form of blocking
      * **Locks**
        * Aquire/Release, ensures only one thread can aquire the lock (set it to true) at any given time in case of premption. 
        * When the thread releases the lock, another thread can acquire the lock.
        * **Implementation - Spin Locks**
          * Slide 13: Problem: could be prempted while aquiring the lock, allowing another thread to take the lock. But when this thread can run again causing the race condition.
          * Proper implementation requires hardware to manage this. This can provide a way to test and set a lock in a single atomic (indivisible) operation. Therefore, impossible for preemption to occur. xchg instruction for x86. 
            * xchg: Acquire changes on slide 17. Makes the race condition impossible. Known as a spin lock.
            * SPARC cas
              * Acquire(bool *lock){
              *   while(cas(lock, false, true) == true);
              * }
            * MIPS: Test and set Slide 19-20?
            * OS/161: Slide 21
          * Potential problem with spin locks: thread doesn't release the lock, causing deadlock.
          * Wasteful: thread could potentially accomplish nothing during it's entire quantum while trying to acquire the lock, wastes time and power.
        * **Actual Locks** - slide 23
          * Similar to spinlocks., locks are used to enforece mutual exclusion
          * spinlocks spin (problem), locks block
            * This allows another thread to run 
    * **Thread Blocking** - Slide 25
      * Sometimes a thread will need to wait for something
        * wait for a lock to be released from another thread
        * data from slow (relative) device
        * input from keyboard
        * wait for busy device to become idle
      * When a thread blocks, it stops running
        * The scheduler chooses a new thread to run
        * context switch from the blocking thread to th new thread occurs
        * The blocking thread is queued in a wait queue (not on the ready list)
      * Eventually, a blocked thread is signaled and awakened by another thread.
      * In OS/161 **Wait Channels**
        * Used to implement thread blocking in OS/161
        * wchan_sleep:
          * blocks calling thread on wait channel wc
          * causes a context switch, like thread_yield
        * wchan_wakeall
          * unblock all threads sleeping on the wait channel, wc.
        * wchan_wakeone
          * wake up only one thread sleeping on wc (good for locks)
        * wchan_lock
          * prevent operations on wait channel wc
      * **See revised thread states (slide 29)**
      * **Locks with Thread Blocking**
        * 

