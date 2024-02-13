# The Captive Touch Pins

The micro:bit gas a captive touch logo that can be used similar to a button. The logo uses the electrical properties of the human body to TODO

![microbit-front-captive-touch-pins](assets/microbit-front-captive-touch-pins.png)

## Printing the State of the Captive Touch Pins to Serial



```python
# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the state of pin 0, pin 1 and pin 2 touch sensors
    print('Pin 0:', pin0.is_touched(), 'Pin 1:', pin1.is_touched(), 'Pin 2:', pin2.is_touched())
    sleep(100) # Wait for 100ms (0.1 seconds)
```

