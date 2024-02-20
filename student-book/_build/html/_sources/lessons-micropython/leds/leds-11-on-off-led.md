# Turning an LED on and Off with the micro:bit Buttons

TODO

![flowchart-button-led-01](assets/flowchart-button-led-01.png)

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
    # Wait for 10ms (0.01 seconds)
    sleep(10)
    
```

TODO

![flowchart-button-led-02](assets/flowchart-button-led-02.png)

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

TODO

![flowchart-button-led-03](assets/flowchart-button-led-03.png)

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