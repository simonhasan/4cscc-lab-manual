# Flashing Random Colors on an RGB LED

TODO

## Zero-Based Indexing

**Zero-based indexing** and one-based indexing are two ways of numbering the elements of an array or a list in programming languages. In zero-based indexing, the first element has an index of 0, while in **one-based indexing**, the first element has an index of 1. The choice of indexing scheme can affect how the array is accessed and manipulated in the code. For example, in zero-based indexing, the last element of an array of length $i$ has an index of  $i-1$. In contrast, in one-based indexing, it has an index of $i$. Python is a programming language that uses zero-based indexing, which means that the first element of a sequence has an index of the length $i-1$. Other zero-based indexing languages include C, C++, Java, and Ruby. Some languages that use one-based indexing are Julia, MATLAB, Fortran, and R.

## The `random` module

The `random` module generates **pseudo-random numbers** and performs random actions in Python. It provides various functions to create random numbers from different distributions, such as uniform, normal, exponential, etc. The random module can be helpful in simulations, games, cryptography, and other applications that require randomness. Randomness plays a crucial role in statistical computing.

### `randint`

TODO

## Flashing Random Colors

TODO

```python
# Imports go at the top
from microbit import *
from random import randint # Import the randint function from the random module

# Set the LED pins
red_pin = pin1   # pin1 is the red pin
green_pin = pin2 # pin2 is the green pin
blue_pin = pin3  # pin3 is the blue pin

# Define a function to set a random red
def set_random_red():
    red_pin.write_analog(randint(0, 1023))   # Set red_pin to a random value
    green_pin.write_analog(0)               # Set green_pin to 0
    blue_pin.write_analog(0)                # Set blue_pin to 0

# Define a function to set a random green
def set_random_green():
    red_pin.write_analog(0)                 # Set red_pin to 0
    green_pin.write_analog(randint(0, 1023)) # Set green_pin to a random value
    blue_pin.write_analog(0)                # Set blue_pin to 0

# Define a function to set a random blue
def set_random_blue():
    red_pin.write_analog(0)                 # Set red_pin to 0
    green_pin.write_analog(0)               # Set green_pin to 0
    blue_pin.write_analog(randint(0, 1023))  # Set blue_pin to a random value

def set_off():
    red_pin.write_analog(0)                 # Set red_pin to 0
    green_pin.write_analog(0)               # Set green_pin to 0
    blue_pin.write_analog(0)                # Set blue_pin to 0

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed, set a random red
    if button_a.is_pressed():
        set_random_red()
    # If button B is pressed, set a random green
    elif button_b.is_pressed():
        set_random_green()
    # If the logo is touched, set a random blue
    elif pin_logo.is_touched():
        set_random_blue()
    # If no buttons are pressed, set the LED to the color off
    else:
        set_off()
    sleep(100) # Wait for 100ms (0.1 seconds)
```

