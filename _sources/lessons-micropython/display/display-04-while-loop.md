# Python: The `while` Loop

In Python, a `while` loop is a control flow statement that repeatedly executes a code block if a specified condition remains `True`. It provides a way to create iterative processes in your code, allowing you to repeat instructions until a specific condition is met or becomes `False`.

The syntax of a `while` loop consists of the keyword `while`, followed by a condition, and a colon `:`. The code block to be executed repeatedly is indented underneath the `while` statement. Inside the code block, you typically include statements that update the variables involved in the condition, ensuring that the loop eventually terminates when the condition evaluates to `False`.

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