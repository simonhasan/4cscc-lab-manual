# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Display the temperature
    display.scroll('Temperature: ' + str(temperature()) + 'C')
    sleep(100) # Wait for 100ms (0.1 seconds)