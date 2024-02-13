# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the temperature
    print('Temperature:', temperature(), 'C') 
    sleep(100) # Wait for 100ms (0.1 seconds)