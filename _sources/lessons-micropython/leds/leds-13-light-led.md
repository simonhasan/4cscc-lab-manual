# Using an LED with the Light Sensor

The previous section introduced writing analog values to an LED to control the brightness. In this section, the brightness of an LED will be controlled by the input of the on-board light sensor.



As mentioned in section TODO:LINK TO LESSON, the light sensor returns an `int` value between `0` and `255.`

![aqi-chart](assets/aqi-chart.png)


```python
# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1

# Code in a 'while True:' loop repeats forever
while True:
    # Get the light level from the display
    light_level = display.read_light_level()
    # Set the brightness of the LED to the light level
    led_pin.write_analog(light_level)
    # Wait for 10ms (0.01 seconds)
    sleep(10)

```

```python
from microbit import *
from map_val import Map

# Set the LED pin
led_pin = pin1

# Code in a 'while True:' loop repeats forever
while True:
    # Get the light level from the display
    light_level = display.read_light_level()
    # Map the light level to the LED brightness in reverse
    map_light_level = Map(light_level, 0, 255, 1023, 0)
    # Set the brightness of the LED to the light level
    led_pin.write_analog(map_light_level)
    # Wait for 10ms (0.01 seconds)
    sleep(10)
    
```