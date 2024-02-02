# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.HEART)       # Display the heart image
    sleep(500)                      # Wait for 500 milliseconds (half a second)
    display.show(Image.HEART_SMALL) # Display the small heart image
    sleep(500)                      # Wait for 500 milliseconds (half a second)