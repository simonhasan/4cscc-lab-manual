# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Check if button A is pressed
    button_a = button_a.is_pressed()
    # Check if button B is pressed
    button_b = button_b.is_pressed()
    # Print the state of the buttons
    print('A:', button_a, 'B:', button_b)