# Lecture 26 - Nov 23, 2016
* Can do small tasks on UI thread without locking up UI.
* Use Threads for longer / more intense tasks
1. Run on UI Thread
    * Break tasks into subtasks, 
2. Run on another thread
    * BAD: If on another thread, need to update UI on UI thread (put into event queue) -> Swing not thread safe.

### Why UI Toolkits aren't thread safe
* Conflicting approach of User generated and Event generated threads
* User: Top down to hardware
* Event: Bottom up from hardware.
* These have to interact at some point, any locking mechanism would cause problems.

### Types of Threads
* Initial Thread: When app started (main)
* Event Dispatch Thread (UI Thread)
* Worker Threads (Background Threads)

### Long Tasks and MVC
* model needs to be concerned with UI
    * Stopping and Starting
    * Notifications
    * Progress

## Responsiveness in a Web App
* Gen1 : Server does most of processing
* Gen2: Adding Javascript
* Gen3: Most of UI can run in the brower.

## Input Performance
* "Big-O for UIs"
* How to choose between designs without actually implementing them
* Evaluating performance.

### KLM (Keystroke Level Modelling)
* Describe each task as a series of operators

* Example
    * One Text Field
        * P: Point mouse into field
        * BB: click onto field (down and up)
        * H: Move hands back to keyboard 
        * K * 10: Typing 10 characters
        * H: Hands back to the mouse
        * Total (Just the Sum): 5.1 seconds 
    * Three Drop Downs
        * P 
        * B
        * P (choose current month)
        * B (up, choose month)
        * Total 3 * PBPB = 7.2 seconds
    * Three Textfields

* Mental Operator
    * Sometimes people need to think about the current task before they can actually do it.
    * cognitive consious
    * can model novice vs. experienced users (novice users need to think more)

* Pros:
    * Easy
    * Can be done off of ideas
* Cons:
    * Out of date
    * typing speed is variable (depends on users)
    * **Biggest:** Input depends (trackpad, mouse, touchpad), distance
