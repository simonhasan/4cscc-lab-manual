# Python: The `while` Loop

```py
# Imports go at the top
from microbit import *

# Scroll "Python" on the display
display.scroll('Python') 
```



```python
# Imports go at the top
from microbit import *


message = 'Python'

# Scroll "Python" on the display
display.scroll(message) 
```





## A Simple `while` Loop

![while-flowchart-generic](assets/while-flowchart-generic.png)

## A Typical micro:bit `while` Loop

![while-flowchart-infinite](assets/while-flowchart-infinite.png)

```python
# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Scroll "Python" on the display
    display.scroll('Python') 
```



![while-flowchart-microbit](assets/while-flowchart-microbit.png)

```python
# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    # Show each character of "Python" individually on the display
    display.show('Python') 
```

TODO