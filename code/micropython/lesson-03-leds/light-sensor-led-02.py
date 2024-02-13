# Imports go at the top
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
    