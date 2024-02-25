# Imports go at the top
from microbit import *

# Set the LED pins
red_pin = pin1   # pin1 is the red pin
green_pin = pin2 # pin2 is the green pin
blue_pin = pin3  # pin3 is the blue pin

# Define the colors as dictionaries
# Red
red = {'red': 255,       # Set the red value to 1
       'green': 0,     # Set the green value to 0
       'blue': 0}      # Set the blue value to 0
# Green
green = {'red': 0,     # Set the red value to 0
         'green': 255,   # Set the green value to 1
         'blue': 0}    # Set the blue value to 0
# Blue
blue = {'red': 0,      # Set the red value to 0
        'green': 0,    # Set the green value to 0
        'blue': 255}     # Set the blue value to 1
# Yellow
yellow = {'red': 255,    # Set the red value to 1
          'green': 255,  # Set the green value to 1
          'blue': 0}   # Set the blue value to 0
# Magenta
magenta = {'red': 255,   # Set the red value to 1
           'green': 0, # Set the green value to 0
           'blue': 255}  # Set the blue value to 1
# Cyan
cyan = {'red': 0,      # Set the red value to 0
        'green': 255,    # Set the green value to 1
        'blue': 255}     # Set the blue value to 1
# White
white = {'red': 255,     # Set the red value to 1
         'green': 255,   # Set the green value to 1
         'blue': 255}    # Set the blue value to 1
# Off
off = {'red': 0,       # Set the red value to 0
       'green': 0,     # Set the green value to 0
       'blue': 0}      # Set the blue value to 0

# Define a function to set the color
def set_color(color):
    red_pin.write_analog(color['red'])     # Set red_pin to the red value
    green_pin.write_analog(color['green']) # Set green_pin to the green value
    blue_pin.write_analog(color['blue'])   # Set blue_pin to the blue value


while True:
    # Flash the LED in different colors
    set_color(red)     # Set the LED to the color red
    sleep(500)         # Wait for 500ms (0.5 seconds)
    set_color(green)   # Set the LED to the color green
    sleep(500)         # Wait for 500ms (0.5 seconds)
    set_color(blue)    # Set the LED to the color blue
    sleep(500)         # Wait for 500ms (0.5 seconds)
    set_color(yellow)  # Set the LED to the color yellow
    sleep(500)         # Wait for 500ms (0.5 seconds)
    set_color(magenta) # Set the LED to the color magenta
    sleep(500)         # Wait for 500ms (0.5 seconds)
    set_color(cyan)    # Set the LED to the color cyan
    sleep(500)         # Wait for 500ms (0.5 seconds)
    set_color(white)   # Set the LED to the color white
    sleep(500)         # Wait for 500ms (0.5 seconds)
    set_color(off)     # Set the LED to the color off
    sleep(500)         # Wait for 500ms (0.5 seconds)