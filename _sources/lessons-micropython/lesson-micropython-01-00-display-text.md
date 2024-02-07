# The micro:bit Display (MicroPython)

TODO
## The 5x5 LED Matrix Display

TODO


## Displaying Text

### Strings

TODO

### `display.scroll()`

TODO

![display-scroll-micropython](assets/display-scroll-micropython.gif)



TODO

```python
from microbit import * 

display.scroll('Python')
```



### `display.show()`

TODO

![display-show-micropython](assets/display-show-micropython.gif)

TODO

```python
from microbit import *

display.show('Python')
```



## The `for` Loop

TODO

```python
from microbit import *

while True:
    display.scroll('Python')
```

TODO

```python
from microbit import *

while True:
    display.show('Python')
```

TODO



## Variables

TODO

```python
from microbit import *

text = 'This is a Python string.'

while True:
    display.show(text)
```

