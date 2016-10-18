# Lecture 15 - October 17, 2016

## Notes
* Wednesday cancelled: watch first 50mins of video (piazza)
* Midterm: Next Monday
  * MC
  * Code
  * SA
  * **Know about interactor trees**

## Visual Perception

### Colour Perception
* How to describe colour?
  * **Additive Model (RGB)**
    * Keep adding light until you get white.
    * Good for displays / things that produce light
    * **HSV Colour Model**
      * Hue: Determines colour
      * Saturation: How much of that colour?
      * Value / Brightness: How much light is emitted of that colour?
  * **Subtractive Model**
    * Colour determined by what is being absorbed
    * Typically used in printing (CMY/CMYK)

* Perceiving Colour
  * Cones: Used to percieve colour (focus)
    * Highest concentration by the eye's macula.
    * Three kinds: Blue, Green, "red" (yellow)
    * Each stimulated by their respective colours.
    * Fewer blue cones, harder to notice blues than reds.
  * Rods: Distinguish light from dark (peripheral vision)

  * Perception depends on how colours are presented, harder when
    * pale
    * small thin objects
    * colours patches are far apart.

  * Colour blindness
    * Monochromacity: 2 or 3 types of cones missing
    * Dichromacy: 1 type missing
      * Protanopia: missing red
      * Deuteranopia: missing green
      * Tritanopia: missing blue (and blue sensitive rods)
    * **Implications**: Don't rely only on colour to distinguish objects (i.e. error messages, don't make just red, add an icon)

  * The brain gives about 50% of vision resources to area where cones are clustered (which make up only about 1% of surface area)

* Implications
  * Put messages where users are looking
  * Reserve red for standout
  * Use icons to account for colour blindness
  * Make use of motion to attract attention.
    * Be subtle (can be annoying).

### Hardware

* Displays all based on RGB
* common idea:
  * Pixels (three subpixels (RGB), vary each to give a colour).
* 16 vs. 24 vs. 32 bit colour
  * 16: 5r, 5g, 5b
  * 24: 8 bits for each
  * 32: 8 bit for colour + 8-bit alpha channel
* CRT Displays:
  * Electron beam to excite Phosphor coating --> Phosphor glows different colours.
  * Maybe useful to display curved objects
* LCDs
  * Various layers and filters
  * Polarizing filters can block, twist light. Only let through certain dimensions.
  * Can be inefficient:
    * Layers waste a lot of light by blocking it
  * LED : An LCD with a LED backlight, more efficient, even lighting

* OLED
  * No backlight, bendable, more expensive
  * Fewer layers
  * Matrix of LED, excited to produce light.

## Direct Manipulation

### User Interaction vs. User Interface
* UI: User expresses intention, receives feedback.
* Interaction: What the user does to express their intentions, over time

### Direct Manipulation by Example - A Series of Analogies
* Dragging a document into the trash
* Change size of shape by dragging on a handle.
* Music controls like physical player.
