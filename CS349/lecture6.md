# Lecture 6 : Widgets
* Multi windows in X
  * Have two actually separate windows
  * Have a child window inside another window
  * Differences
    * User can't resize / relocated child window
  * Why use child window?
    * For reusable child elements -> **Widgets**
* **Widgets**
  * A generic name for parts of an interface that have their own behaviour
  * Accept and interpret their own events
  * Usually put into reusable libraries
  * **Heaveyweight widgit toolkit**
    * BWS provides widgets
    * since base window system provides them, user events can be passed directly to components by BWS/OS
    * Can preserve look-and-feel of platform
    * OS-specific
      * Cross platform support difficult
  * **Lightweight widget toolgit**
    * OS provides top level window; widget toolkit draws it's own widgets in the window
    * Toolkit responsible for handling their own events
* **Widget toolkit design goals**
  * **Complete**: UI designers should have all they need
  * **Consistent**: 
    * User: Look-and-feel
    * Developers: API
  * **Customizable**
    * devs can reasonably extend the existing functionality
    1. Properties : colour, font, orientation, etc.
    2. Pluggable Behaviour
      * Delegate to behaviour to somewhere else 
      * ActionListener: Responding to an event
  * **Why?** - reuse 
  * **Characterization** - Slide 20
    * model the widget manipulates (number, text, choice)
    * how do they implement the model? (simple - self-contained, abstract - delegates)
    * Events that the widget generates (action, change)
    * Properties which change behaviour and appearance
    * contains subwidgets or is stand-alone
      * Standalone: Label
      * Containing Subwidgets: TabController
    * Input mapped across many different widgets
      * different inputs have different types of input
        * Mouse - (x, y)
        * Keyboard - key input
      * Inputs can map to the same **Logical Input Device**
        * Logical button device
          * generates a pushed event
          * Can have many different appearances: can be activated by a click, menu item, keyboard shortcut
  * Note Multiple **MVC** within an application
    * Application level
    * Widget level
