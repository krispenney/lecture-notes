# Lecture 6 - Sept 27, 2106

## Semaphores
* Like locks, more powerful.
* Either 0 or a positive integer
* **P** operation: Decrement or wait until positive to decrement
* **V** operation: Increment

``` C
struct semaphore {
  unsigned int value;
  struct wchan *sleep;
  struct spinlock *lock;
};

// Decrement value if positive
// Wait if 0
void P(struct semaphore *sem){
  spinlock_aquire(sem->lock);
  while (sem->value == 0){
    spinlock_release(sem->lock);
    wchan_sleep(sem->sleep);
    spinlock_aquire(sem->lock);
  }
  --sem->value;
  spinlock_release(sem->lock);
}

// wc_lock, need a way to context switch away and unlock the wait channel at the same time

void V(struct semaphore *sem){
  spinlock_aquire(sem->lock);
  ++sem->value;
  wchan_lock(sem->sleep);
  wchan_wakeone(sem->sleep); // wakeone never waits
  spinlock_release(sem->lock);
}
```

## Condition Variables
* Another synchronization primitive
* A condition variable is intended to work together with a lock: condition variables are only used from critical sections.
* Allow threads to wait for arbitrary conditions to become true inside of a critical section.
* Operations:

  1. **wait**: causes calling thread to block and releases the lock associated with the condition variable. When thread is unblocked, reacquire the lock.
  2. **signal**: If any threads blocked, one is unblocked
  3. **broadcast**: wake_all

* Example: bounded buffer
  * count > 0 (items in the buffer)
  * count < N (there is free space in the buffer)

* When a condition is not true, wait until it becomes true
  * Really this means wait until someone wakes you up.
  * Another thread will check the condition and wake you up (using signal or broadcast).
  * Note: Calling signal or broadcast to a condition with no waiters has no effect
* While your waiting for a condition to be true. wait takes you out of the critical section, potentially allowing another thread to pass through.
* Potentially two levels of waiting, first for the condition, second to acquire the lock.
* OS/161 uses Mesa-style condition variables.

* Slides 44 and 45
  * Need to check in the while loop because signal may change by the time that the thread it woken up.
  * cv_signal doesn't actually touch the lock.
