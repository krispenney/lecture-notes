# Lecture 16 - Nov 8

## Recall
* Secondary Storage is slow
* Can used different replacement policies to tell when to swap memory
* Clock replacement algorithm + use bit

## Post-Midterm Depression

## Assignment 2b
* Trick is argument passing
  1. See picture of argv and argc in assignment hints
  2. Alignment:

## CPU Scheduling

### Simple Scheduling Model
* For each job, given
  * job arrival time (a<sub>i</sub>)
  * job run time (r<sub>i</sub>)
* For each job, define
  * response time: time between job's arrival and when the job starts to run.
  * turnaround time: time between job's arrival and when the job finished.
* We need to decide when each job should run, to achieve some goal.
  * minimize average turnaround time?
  * minimize average response time?

**Basic Non-Preemptive Schedulers: FCFS and SJF
* FCFS: First come first serve
  * avoids starvation
  * pre-emptive variant: round robin
* SJF: Shortest job first - run jobs in increasing order
  * minimize average runaround time
  * longer jobs may starve
  * pre-emptive variant: SRTF (Shortest Remaining Time First)


### Slide 8 - Round Robin Example
* When job 4 is loaded at time 5: Job 3 is running and Jobs 1 and 2 are waiting.
* Job 4 is put to the back of the list: 1, 2, 4

### SRTF
* Job 3 runs for quantum, gets preempted, but is then rescheduled since it is now the shortest job.
* Gets good turnaround time, but longer jobs get starved.

### Slide 10
* Jobs are actually threads
* Real CPU scheduling differs from simple:
  * Don't know run times of threads
  * Threads are sometimes not runnable, when blocked
  * threads may have different priorities.
  * Objective is to achieve a balance of:
    * responsiveness: ensure threads get run regularly
    * fairness
      * Round robin gives equal priority to each thread, even UI.
    * efficiency

### Multi Level Feedback Queues
* Objective:
  * good responsiveness for interactive threads (things the user would use).
    * interactive threads are frequently blocked, waiting for human interaction.
  * non-interactive threads make as much progress as possible.
* Approach: give higher priority to interactive threads so that they run whenever they are ready.
* Problem: how to determine which threads are interactive and which are not?
* Scheduler maintains **n** round-robin ready queues (Q_1, ..., Q_n)
* Q_n is the highest priority, decreasing priority
* if Q_n is empty, choose a thread from Q<sub>n-1</sub>
* Give a larger Quantum to lower priority threads, smaller for higher priority.
* if thread uses it's entire quantum and is preempted, demote it to a lower thread.
* If a thread blocks, put in Q<sub>n</sub> when it wakes up.
* To prevent starvation, periodically move all threads to Q<sub>n</sub>
