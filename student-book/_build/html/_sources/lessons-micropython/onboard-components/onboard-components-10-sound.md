# The Sound Sensor

TODO

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

