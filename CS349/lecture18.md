# Lecture 18 - October 24, 2016

## Evaluating Instruments

### Degree of Indirection
* **"By Far the biggest/important"**
* **Spatial**
* **Temporal**
### Degree of integration
* Degrees of freedom instrument / Degrees of freedom input.
* Implication: 
  * Ratio of 1 is perfect, 
  * 1 < --> is problamatic (have to multiplex somehow, i.e. (x, y) -> (x, y, z)?), 
  * < 1 - not ideal, but easy to deal with
### Degree of Compatibility
* Similarity between motions, high is ideal.
* i.e. Dragging is high degree
* Medium = Traditional scroll bars
* Dialog box: low - none

## GUI != Direct Manipulation
* Many commands are invoked indirectly (Menus, dialogs, toolbars)
* Hidden objects of interest (Stylesheets)

## Direct Manipulation Issues
* Visually impaired people can't see the graphics.
* Significant screen real estate often required.
* Switching between keyboard and mouse is time consuming.
* Analogies may not be clear (diminishing importance)

## Implementing Direct Manipulation
* Two locations with special meaning (folder, trash bin)

### Hit Tests
* Determine what the pointer is pointing at.
``` Java
for(Item item : displayList) {
    if(item.contains(mouse.x, mouse.y)){
    }
}
```
* Needs to be fast for programmer and computer.

## 2D Graphics
* **Model** mathematical representation of an image containing the important properties of an object, data structure.
* **Rendering** Using the properties of the model to create a displayable image.

### Affine Transformations
* Translation: Add a scalar to each vertex
* Uniform Scaling: Multiply each vertex by a scalar
  * When it's not at the origin, scaling also translates.
* Rotation: refer to origin, rotate about
  * x = r * cos(\Phi)
  * y = r * sin(\Phi)
  * x`= r * cost(\Phi + \Theta)
    * = r * [cos(\Phi)cost(\Theta) - sin(\Phi)cos(\Theta)]
    * = x*cos(\Theta) - y * sin(\Theta)
  * y` = xsin(\Theta) + ycos(\Theta)
  
