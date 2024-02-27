# The Temperature Sensor

The micro:bit has a built-in temperature sensor located inside its processor. It's not a dedicated sensor for precise measurements, but it can give you a good approximation of the ambient temperature around the micro:bit. It measures temperature in degrees Celsius (°C) with ±5℃ accuracy.

![microbit-back-processor](assets/microbit-back-processor.png)

## Printing the Temperature Reading to Serial



```python
# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the temperature
    print('Temperature:', temperature(), 'C') 
    sleep(100) # Wait for 100ms (0.1 seconds)
```

