# Dictionaries

TODO

![dictionaries](assets/dictionaries.png)

```python
# Imports go at the top
from microbit import *

# Set the LED pins
red_pin = pin1   # pin1 is the red pin
green_pin = pin2 # pin2 is the green pin
blue_pin = pin3  # pin3 is the blue pin

# Define the colors as dictionaries
red = {'red': 255, 'green': 0, 'blue': 0} 
green = {'red': 0, 'green': 255, 'blue': 0}
blue = {'red': 0, 'green': 0, 'blue': 255}
yellow = {'red': 255, 'green': 255, 'blue': 0}
magenta = {'red': 255, 'green': 0, 'blue': 255}
cyan = {'red': 0, 'green': 255, 'blue': 255}
white = {'red': 255, 'green': 255, 'blue': 255}
off = {'red': 0, 'green': 0, 'blue': 0}

# Define a function to set the color
def set_color(color):
    red_pin.write_analog(color['red'])     # Set red_pin to the red value
    green_pin.write_analog(color['green']) # Set green_pin to the green value
    blue_pin.write_analog(color['blue'])   # Set blue_pin to the blue value


while True:
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
```

