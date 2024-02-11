# Blinking an LED

TODO

## Debugging

The following code is supposed to make an LED on `pin1` blink, but it is not working. How can the code be fixed?

![quiz-led-01](assets/quiz-led-01.png)

```{admonition} Click here to reveal the solutions.
:class: dropdown
Solution:
![quiz-led-02](assets/quiz-led-02.png)

The variable pointing to `pin1` is `led_pin`, but the variable used in the `while` loop is `led`. This variable has not been declared. Changing `led` to `led_pin` will fix the code.

![quiz-led-solution](assets/quiz-led-solution.png)

```