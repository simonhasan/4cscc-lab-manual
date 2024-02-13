# The Light Sensor

TODO

![microbit-front-leds](assets/microbit-front-leds.png)

## Printing the Light Sensor Reading to Serial



```python
# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the light level
    print('Light level:', display.read_light_level())
    sleep(100) # Wait for 100ms (0.1 seconds)
```

