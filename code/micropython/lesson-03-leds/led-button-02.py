# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed
    if button_a.is_pressed():
        # Turn the LED on
        led_pin.write_digital(1)
    # Otherwise  
    else:
        # Turn the LED off
        led_pin.write_digital(0)
    # Wait for 10ms (0.01 seconds)
    sleep(10)