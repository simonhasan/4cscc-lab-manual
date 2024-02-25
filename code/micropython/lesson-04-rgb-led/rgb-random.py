# Imports go at the top
from microbit import *
from random import randint # Import the randint function from the random module

# Set the LED pins
red_pin = pin1   # pin1 is the red pin
green_pin = pin2 # pin2 is the green pin
blue_pin = pin3  # pin3 is the blue pin

# Define a function to set a random red
def set_random_red():
    red_pin.write_analog(randint(0, 255))   # Set red_pin to a random value
    green_pin.write_analog(0)               # Set green_pin to 0
    blue_pin.write_analog(0)                # Set blue_pin to 0

# Define a function to set a random green
def set_random_green():
    red_pin.write_analog(0)                 # Set red_pin to 0
    green_pin.write_analog(randint(0, 255)) # Set green_pin to a random value
    blue_pin.write_analog(0)                # Set blue_pin to 0

# Define a function to set a random blue
def set_random_blue():
    red_pin.write_analog(0)                 # Set red_pin to 0
    green_pin.write_analog(0)               # Set green_pin to 0
    blue_pin.write_analog(randint(0, 255))  # Set blue_pin to a random value

def set_off():
    red_pin.write_analog(0)                 # Set red_pin to 0
    green_pin.write_analog(0)               # Set green_pin to 0
    blue_pin.write_analog(0)                # Set blue_pin to 0

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed, set a random red
    if button_a.is_pressed():
        set_random_red()
    # If button B is pressed, set a random green
    elif button_b.is_pressed():
        set_random_green()
    # If the logo is touched, set a random blue
    elif pin_logo.is_touched():
        set_random_blue()
    # If no buttons are pressed, set the LED to the color off
    else:
        set_off()
    sleep(100) # Wait for 100ms (0.1 seconds)