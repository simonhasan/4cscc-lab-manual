# Serial Communication

Serial communication is a method of transferring data between two or more devices over a serial interface, typically using a single communication line.

Using serial communication with the micro:bit is using its built-in USB interface as a serial port. When connected to a computer via USB, the micro:bit appears as a virtual serial port, allowing data to be sent and received using serial communication protocols. This enables bi-directional communication between the micro:bit and the computer, facilitating tasks such as programming, data logging, and interaction with user input.

The micro:bit display is an excellent way to display data, but sometimes data changes faster than the `display.scroll()` method. There is an efficien way to display data using the `print()` function using serial communication. 





![serial-demo-01](assets/serial-demo-01.png)

TODO

```python
# Imports go at the top
from microbit import *

greeting = 'Hello. My name is Alice.'

# Code in a 'while True:' loop repeats forever
while True:
    display.scroll(greeting)

```

TODO

![serial-demo-02](assets/serial-demo-02.png)

TODO

```python
# Imports go at the top
from microbit import *

greeting = 'Hello. My name is Alice.'

# Code in a 'while True:' loop repeats forever
while True:
    display.scroll(greeting)
    print(greeting)

```
TODO

![serial-demo-03](assets/serial-demo-03.png)

TODO