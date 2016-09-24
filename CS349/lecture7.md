# Lecture 7 - Event Dispatch - Sept 23, 2016
## Event Dispatch
* **Event Dispatch** : Getting events to the correct widget
  * Event Capture -> Event Queue -> Event Dispatch
* **Event Handling**: Running the right code in that widget 
* View Heirarchy == Interactor tree
  * Event Dispatch -> traverse the tree to find the correct widget
  * Both Heavy and light weight widgets have this tree, just difference in the toolkit.
  * The correct widget is the one under the mouse, with the highest z-index (lowest child)
  * **Bottom-up** Positional Dispatch
    * From leaf nodes in the interactor tree.
    * Leaf node given first oppourtunity to act.
    * If it can't pass to it's parent.
      * Why: Slide 11 - Colour picker - better communicate state if palette tracks selected color
  * **Top-Down** Positional Dispatch
    * Event routed to highest level node (in the tree) that is under the cursor.
    * If can't handle it, pass to child.
    * Parent can enforce certain conditions 
      * logging
      * disables all children
  * Type of dispatch is set by the toolkit.
  * Slide 14 for odd behaviour of positional dispatch
    * Fixed by **Focus**
      * at most one widget in focus for a particular event type (keyboard, mouse) at a time
      * Often use a Focus Manager to help manage focus
  * **Accelorator Key Dispatch**
    * Key command to before certain action
    * bypass dispatch and focus 
  * X uses Top Down dispatch
    * event loop at the application record
    * application has to decide which window to route the event to.
## Event Handling
    * Event Dispatch : Which window / widget should recieve the event
    * Event handling: Widget has the event, how to bind the event to some code?
    * **Goals**
      * Easy to understand, implement, debug
      * Good performance
    * Different Methods
      * **Switch Statement**
        * Using event loop, switch on event type
        * If multiple windows, need an outer switch statement for the window
        * Problem:
          * BWS already figured out which window got the event, repeating work by checking again
          * focuses everything to one spot, hard to collaborate with multiple programmers
      * **WindowProc**
        * Each window gets a WindowProc function
        * each window manages it's own events
      * **Event Table Binding**
        * Each window has a table of procudure pointers
        * potentially point to defaults, replace pointers for custom action
        * Problem: Lack of clarity for programmer
      * **Inheritance Binding*
        * A nicer way to implement tables
        * Inheritance tree and implement override relavent methods
        * Problems: 
          * Lots of subclasses and lots of boiler plate code
          * Can't filter out irrelavant events 
        * Take away: Use inheritance for extending class functionality, not for event binding.
      * **Strategy Design Pattern**
        * Each widget has a list of items that implement different listener interfaces (list of mouseListeners)
        * Improvments:
          * Can filter events
          * easy to scale (just add new interfaces)
      * **Inner Class**
        * Each object has it's own listener implementations
      * **Javascript**
        * Uses both top-down and bottom up
      * **Delegate Binding**
        * Like function pointers in C/C++, similar to previous using function instead of methods
      * **High Rate**
        * Pen / Touch
        * Events motion may be skipped
        * Special Methods to get these.
