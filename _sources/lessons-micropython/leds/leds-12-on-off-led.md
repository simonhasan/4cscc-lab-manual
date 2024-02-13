# Turing an LED on and Off with the micro:bit Buttons

TODO

```python
# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed
    if button_a.is_pressed():
        # Turn the LED on
        led_pin.write_digital(1)
    # Otherwise  
    else:
        # Turn the LED off
        led_pin.write_digital(0)
    # Wait for 10ms (0.01 seconds)
    sleep(10)

```

```{note}
In the previous section it was stated that the Boolean data type had two values `True` and `False` with corresponding integer values `1` and `0` respectively. It is possible to turn an LED on and off using a `bool` as demonstrated below:

```python
# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed
    if button_a.is_pressed():
        # Turn the LED on
        led_pin.write_digital(True)
    # Otherwise  
    else:
        # Turn the LED off
        led_pin.write_digital(False)
    # Wait for 10ms (0.01 seconds)
    sleep(10)

```

TODO

```python
# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed
    if button_a.is_pressed():
        # Turn the LED on
        led_pin.write_digital(1)
    # If button B is pressed
    if button_b.is_pressed():
        # Turn the LED off
        led_pin.write_digital(0)
    # Wait for 10ms (0.01 seconds)
    sleep(10)

```

TODO

```python
# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1

# Code in a 'while True:' loop repeats forever
while True:
    # If button A is pressed
    if button_a.is_pressed():
        # Turn the LED on
        led_pin.write_digital(1)
    # If button B is pressed
    elif button_b.is_pressed():
        # Turn the LED off
        led_pin.write_digital(0)
    # Otherwise
    else:
        # Do nothing
        pass
    # Wait for 10ms (0.01 seconds)
    sleep(10)
    
```