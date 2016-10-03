# Lecture 11 - October 4, 2016

## Visual Design

### Gestalt Principals
* Proximity
* Similarity
* Good Continuation
* Closure
* Figure/Ground
* Law of Prägnanz
* Uniform Connectedness
* Alignment

### Testing out UIs
* Don't ask if they like it
  * Most people try to be nice.
  * Ask the vague questions: What do you think about this?
* **Squint test**: Mimic the early portion of visual recognition system

## MVC

### Rational
* Show same data in multiple view.
* Multiple views, loosely coupled to the underlying data model
  * PowerPoint: Main slide view, side slide panel
  * Photoshop: Main work area, Image navigator
    * Main work area composed of multiple layers, change in work area should change layers
    * Rearranging layers should change the main work area.
* UI is typically updated faster and more frequently than the underlying application, decoupling these allows for easier maintenance.

### Solution
* **Controllers**: has a reference to the Model, has access to it's public interface.
* **Model**: has a reference to a basic view interface (update view)
  * When the Model changes, it calls "update view"
  * Representation of app data.
* **View**: has a reference to the model
