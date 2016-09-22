# Lecture 5 - Sept 22, 2016
* Last time: Mutual Exclusion via locks
* Slide 22
  * y == 0 -> something went wrong
  * x -> tells us whether or not the lock was locked
* Slide 29
  * Each wait channel has it's own blocked queue
  * Need to make sure that waking always happens after sleeping (be very careful of preemption)
## Semaphores
  * A semaphore is a synchronization primitive that can be used to enforce mutual exclusion requirements. It can also e used to solve other kinds of synchronization problems.
  * More powerful than locks (can use semaphores to implement locks)
  * Supports two operations:
    1. **P**: If the integer value is greater than 0, decrement it. Otherwise, wait until the value is greater than 0 and then decrement it.
    2. **V**: increment the value of the semaphore
    * Instead of being unlocked and locked -> 0 for locked and 1 <= for "unlocked".
    * Both atomic operations
  * Slide 33 : Using semaphores exactly as a lock
  * But they are more powerful
  * **Producer / Consumer Synchronization with Bounded Buffer**
    * threads (producers) that add items to a buffer
    * threads (consumers) that remove items from the buffer
    * Want to ensure that consumers do not consume unless something is in the buffer
    * If the buffer has a finite capactiy, need to ensure producers want put things in when it's full.
    * Now the integer value can relate to how much space is left / how many objects in the buffer.
``` C
struct buffer {
    void *items[N];
    sem num_of_items;
    sem remaining_space;
};

void init_buffer(struct buffer *b){
    num_of_items = sem_create("Number of items", 0);
    remaining_space = sem_create("Remaining Space", N);
}

void producer(struct buffer *b){
    // generating data d
    P(remaining_space); // decrements remaining space (waits until there's space)
    push(b, d);
    V(num_of_items);
}
void consumer(struct buffer *b){}
```
  * Why do we want both count and remaining space? 
