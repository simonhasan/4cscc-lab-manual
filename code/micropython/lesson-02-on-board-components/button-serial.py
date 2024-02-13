# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the state of button A and button B
    print('A:', button_a.is_pressed(), 'B:', button_b.is_pressed())
    sleep(100) # Wait for 100ms (0.1 seconds)