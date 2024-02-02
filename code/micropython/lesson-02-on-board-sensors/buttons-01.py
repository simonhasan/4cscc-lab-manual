# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Check if button A is pressed
    if button_a.is_pressed():
        display.show('A') # Display 'A' if button A is pressed