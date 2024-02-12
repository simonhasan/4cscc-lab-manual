# Using an LED with the Light Sensor

TODO


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