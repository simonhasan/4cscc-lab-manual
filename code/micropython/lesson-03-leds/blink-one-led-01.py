# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1

# Code in a 'while True:' loop repeats forever
while True:
    # Turn the LED on
    led_pin.write_digital(1)
    # Wait for 500ms (0.5 seconds)
    sleep(500)
    # Turn the LED off
    led_pin.write_digital(0)
    # Wait for 500ms (0.5 seconds)
    sleep(500)

