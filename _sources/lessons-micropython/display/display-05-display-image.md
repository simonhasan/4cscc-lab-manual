# Built-In Images

TODO

The BBC micro:bit has 64 built-in images that can be displayed on the 5x5 LED matrix display using Python.

## Displaying Built-In Image

To display a built-in image, the following line of code is used:

```{note}
The image name is always in uppercase.
```



### `display.show(Image.ENTER_IMAGE)`

```python
# Imports go at the top
from microbit import *

display.show(Image.HEART)       # Display the heart image

```

![built-in-heart-example](assets/built-in-heart-example.png)

---

## Built-In Image Inventory

The built-in images can separated into the following categories:

- Affirmations
- Arrows
- Animals
- Clocks
- Faces
- Music
- Miscellaneous

These categories and images are presented below:

### Affirmations

| Affirmation                              | Code        |
| ---------------------------------------- | ----------- |
| ![built-in-no](assets/built-in-no.png)   | `Image.NO`  |
| ![built-in-yes](assets/built-in-yes.png) | `Image.YES` |



### Arrows

| Arrow                                              | Code             |
| -------------------------------------------------- | ---------------- |
| ![built-in-arrow-e](assets/built-in-arrow-e.png)   | `Image.ARROW_E`  |
| ![built-in-arrow-n](assets/built-in-arrow-n.png)   | `Image.ARROW_N`  |
| ![built-in-arrow-ne](assets/built-in-arrow-ne.png) | `Image.ARROW_NE` |
| ![built-in-arrow-nw](assets/built-in-arrow-nw.png) | `Image.ARROW_NW` |
| ![built-in-arrow-s](assets/built-in-arrow-s.png)   | `Image.ARROW_S`  |
| ![built-in-arrow-se](assets/built-in-arrow-se.png) | `Image.ARROW_SE` |
| ![built-in-arrow-sw](assets/built-in-arrow-sw.png) | `Image.ARROW_SW` |
| ![built-in-arrow-w](assets/built-in-arrow-w.png)   | `Image.ARROW_W`  |



### Animals

| Animal                                               | Code              |
| ---------------------------------------------------- | ----------------- |
| ![built-in-butterfly](assets/built-in-butterfly.png) | `Image.BUTTERFLY` |
| ![built-in-cow](assets/built-in-cow.png)             | `Image.COW`       |
| ![built-in-duck](assets/built-in-duck.png)           | `Image.DUCK`      |
| ![built-in-giraffe](assets/built-in-giraffe.png)     | `Image.GIRAFFE`   |
| ![built-in-rabbit](assets/built-in-rabbit.png)       | `Image.RABBIT`    |
| ![built-in-snake](assets/built-in-snake.png)         | `Image.SNAKE`     |
| ![built-in-tortoise](assets/built-in-tortoise.png)   | `Image.TORTOISE`  |



### Clocks

| Clock                                              | Code            |
| -------------------------------------------------- | --------------- |
| ![built-in-clock-01](assets/built-in-clock-01.png) | `Image.CLOCK1`  |
| ![built-in-clock-02](assets/built-in-clock-02.png) | `Image.CLOCK2`  |
| ![built-in-clock-03](assets/built-in-clock-03.png) | `Image.CLOCK3`  |
| ![built-in-clock-04](assets/built-in-clock-04.png) | `Image.CLOCK4`  |
| ![built-in-clock-05](assets/built-in-clock-05.png) | `Image.CLOCK5`  |
| ![built-in-clock-06](assets/built-in-clock-06.png) | `Image.CLOCK6`  |
| ![built-in-clock-07](assets/built-in-clock-07.png) | `Image.CLOCK7`  |
| ![built-in-clock-08](assets/built-in-clock-08.png) | `Image.CLOCK8`  |
| ![built-in-clock-09](assets/built-in-clock-09.png) | `Image.CLOCK9`  |
| ![built-in-clock-10](assets/built-in-clock-10.png) | `Image.CLOCK10` |
| ![built-in-clock-11](assets/built-in-clock-11.png) | `Image.CLOCK11` |
| ![built-in-clock-12](assets/built-in-clock-12.png) | `Image.CLOCK12` |



### Faces

| Face                                               | Code             |
| -------------------------------------------------- | ---------------- |
| ![built-in-angry](assets/built-in-angry.png)       | `Image.ANGRY`    |
| ![built-in-asleep](assets/built-in-asleep.png)     | `Image.ASLEEP`   |
| ![built-in-confused](assets/built-in-confused.png) | `Image.CONFUSED` |
| ![built-in-fabulous](assets/built-in-fabulous.png) | `Image.FABULOUS` |
| ![built-in-happy](assets/built-in-happy.png)       | `Image.HAPPY`    |
| ![built-in-meh](assets/built-in-meh.png)           | `Image.MEH`      |
| ![built-in-sad](assets/built-in-sad.png)           | `Image.SAD`      |
| ![built-in-silly](assets/built-in-silly.png)       | `Image.SILLY`    |
| ![built-in-smile](assets/built-in-smile.png)       | `Image.SMILE`    |



### Music Notes

| Music Note                                                   |                  |
| ------------------------------------------------------------ | ---------------- |
| ![built-in-music-crotchet](assets/built-in-music-crotchet.png) | `Image.CROTCHET` |
| ![built-in-music-quaver](assets/built-in-music-quaver.png)   | `Image.QUAVER`   |
| ![built-in-music-quavers](assets/built-in-music-quavers.png) | `Image.QUAVERS`  |



### Shapes

| Shape                                                        | Code                  |
| ------------------------------------------------------------ | --------------------- |
| ![built-in-diamond](assets/built-in-diamond.png)             | `Image.DIAMOND`       |
| ![built-in-diamond-small](assets/built-in-diamond-small.png) | `Image.DIAMOND_SMALL` |
| ![built-in-heart](assets/built-in-heart.png)                 | `Image.HEART`         |
| ![built-in-heart-small](assets/built-in-heart-small.png)     | `Image.HEART_SMALL`   |
| ![built-in-square](assets/built-in-square.png)               | `Image.SQUARE`        |
| ![built-in-square-small](assets/built-in-square-small.png)   | `Image.SQUARE_SMALL`  |
| ![built-in-triangle](assets/built-in-triangle.png)           | `Image.TRIANGLE`      |
| ![built-in-triangle-left](assets/built-in-triangle-left.png) | `Image.TRIANGLE_LEFT` |



### Miscellaneous

|                                                          |                     |
| -------------------------------------------------------- | ------------------- |
| ![built-in-chessboard](assets/built-in-chessboard.png)   | `Image.CHESSBOARD`  |
| ![built-in-ghost](assets/built-in-ghost.png)             | `Image.GHOST`       |
| ![built-in-house](assets/built-in-house.png)             | `Image.HOUSE`       |
| ![built-in-pacman](assets/built-in-pacman.png)           | `Image.PACMAN`      |
| ![built-in-pitchfork](assets/built-in-pitchfork.png)     | `Image.PITCHFORK`   |
| ![built-in-rollerscate](assets/built-in-rollerscate.png) | `Image.ROLLERSKATE` |
| ![built-in-scissors](assets/built-in-scissors.png)       | `Image.SCISSORS`    |
| ![built-in-skull](assets/built-in-skull.png)             | `Image.SKULL`       |
| ![built-in-stickfigure](assets/built-in-stickfigure.png) | `Image.STICKFIGURE` |
| ![built-in-sword](assets/built-in-sword.png)             | `Image.SWORD`       |
| ![built-in-target](assets/built-in-target.png)           | `Image.TARGET`      |
| ![built-in-tshirt](assets/built-in-tshirt.png)           | `Image.TSHIRT`      |
| ![built-in-umbrella](assets/built-in-umbrella.png)       | `Image.UMBRELLA`    |
| ![built-in-xmas](assets/built-in-xmas.png)               | `Image.XMAS`        |

## Debugging

The following image is intended to be displayed on the micro:bit, but there is an error in the code. 

![quiz-image](assets/quiz-image.png)

Which line of code is correct for displaying the image above?

**A**: `display.scroll(Image.HOUSE)`

**B**: `display(Image.HOUSE)`

**C**: `display.show(Image.house)`

**D**: `display.show(Image.HOUSE)`

```{admonition} Click here to reveal the solutions.
:class: dropdown
Solutions:
**D**: `display.show(Image.HOUSE)`

Explination:
**A**: This uses the `display.scroll()` method. This is only used with strings.
**B**: The method is incomplete.
**C**: The attribute of `Image` is not capitalized.
```