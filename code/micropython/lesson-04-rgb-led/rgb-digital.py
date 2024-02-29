# Imports go at the top
from microbit import *

# Turn off the display
display.off() # This disables the display to access GPIO pins

# Set the LED pins
red_pin = pin1   # pin1 is the red pin
green_pin = pin2 # pin2 is the green pin
blue_pin = pin3  # pin3 is the blue pin

# Code in a 'while True:' loop repeats forever
while True:
    # Set the LED to red
    red_pin.write_digital(1)   # Set red_pin to 1
    green_pin.write_digital(0) # Set green_pin to 0
    blue_pin.write_digital(0)  # Set blue_pin to 0
    sleep(100) # Wait for 100ms (0.1 seconds)
    # Set the LED to green
    red_pin.write_digital(0)   # Set red_pin to 0
    green_pin.write_digital(1) # Set green_pin to 1
    blue_pin.write_digital(0)  # Set blue_pin to 0
    sleep(100) # Wait for 100ms (0.1 seconds)
    # Set the LED to blue
    red_pin.write_digital(0)   # Set red_pin to 0
    green_pin.write_digital(0) # Set green_pin to 0
    blue_pin.write_digital(1)  # Set blue_pin to 1
    sleep(100) # Wait for 100ms (0.1 seconds)
    # Set the LED to off
    red_pin.write_digital(0)   # Set red_pin to 0
    green_pin.write_digital(0) # Set green_pin to 0
    blue_pin.write_digital(0)  # Set blue_pin to 0
    sleep(100) # Wait for 1 second