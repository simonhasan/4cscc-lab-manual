# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the compass heading
    print('Compass heading:', compass.heading())
    sleep(100) # Wait for 100ms (0.1 seconds)