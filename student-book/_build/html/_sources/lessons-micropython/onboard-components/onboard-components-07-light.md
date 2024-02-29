# The Light Sensor

The micro:bit features light sensing capability through the 5x5 LED matrix display. It's not a dedicated sensor for precise measurements, but the light-sensing capability measures the intensity of ambient light in the surrounding environment.

Using the light sensor, the micro:bit can detect changes in light levels, allowing it to respond to different lighting conditions. For example, in programming projects, the micro:bit can be programmed to adjust its behavior based on changes in light intensity, such as turning on an LED when it gets dark or changing the display brightness in response to ambient light.

![microbit-front-leds](assets/microbit-front-leds.png)

## Displaying the Light Sensor Reading on the micro:bit Display

TODO

## Printing the Light Sensor Reading to Serial



```python
# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the light level
    print('Light level:', display.read_light_level())
    sleep(100) # Wait for 100ms (0.1 seconds)
```

