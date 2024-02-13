# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the state of the logo touch sensor
    print('Logo touched:', pin_logo.is_touched())
    sleep(100) # Wait for 100ms (0.1 seconds)