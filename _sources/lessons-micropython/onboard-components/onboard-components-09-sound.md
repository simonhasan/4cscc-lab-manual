# The Sound Sensor

The micro:bit sound sensor (microphone) is a built-in sensor that detects sound levels in the surrounding environment. This sensor measures the intensity or amplitude of sound waves, allowing the micro:bit to respond to changes in sound levels.

Using the sound sensor, the micro:bit can detect sound events, such as claps, music, or spoken words, and respond accordingly in programmed applications. For example, it can be used to trigger actions, control animations, or display visualizations in response to sound input.

The micro:bit sound sensor is displayed below:

![microbit-front-microphone](assets/microbit-front-microphone.png)

## Printing the Sound Level to Serial



```python
# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Print the sound level
    print('Sound level:', microphone.sound_level())
    sleep(100) # Wait for 100ms (0.1 seconds)
```

