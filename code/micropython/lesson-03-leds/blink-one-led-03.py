# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1
# Set the LED to on
led_on = True
# Set the LED to off
led_off = False

# Code in a 'while True:' loop repeats forever
while True:
    # Turn the LED on
    led_pin.write_digital(led_on)
    # Wait for 500ms (0.5 seconds)
    sleep(500)
    # Turn the LED off
    led_pin.write_digital(led_off)
    # Wait for 500ms (0.5 seconds)
    sleep(500)

