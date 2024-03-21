# Variables

In mathematics, a **variable** is a symbol or letter used to represent an unknown quantity or a value that can change within a given context or equation. Variables are typically denoted by letters such as $x$, $y$, or $z$​, and their values can vary depending on the conditions or constraints of the problem being considered.

In computer science, a **variable** is a symbolic name associated with a memory location that stores data. Variables are placeholders for values that can change during a program's execution. They represent and manipulate different data types, such as numbers, strings, or objects, allowing programmers to work with dynamic information and perform computations. 

Variables allow programmers to store and manipulate data within a program. They can hold different data types, such as numbers, strings, lists, or more complex objects. Variables in Python are **dynamically typed**, meaning their type is determined at runtime based on the value assigned to them. This flexibility makes Python versatile for various programming tasks, as variables can be reassigned to different types of data as needed during execution.

Variables must be declared or assigned a name. To declare a variable, you use the assignment operator `=`.


```{note}
The assignment operator `=` does not represent equality as it does in mathematics. To represent equality, see section TODO.
```

Here are some examples:

```python
led_pin = 1
name = 'Oscar'
sensor_val = analog_read(sensor_pin)
```





 ## Naming Variables

Variable names come with some constraints:

### Variable Names Cannot Start with a Number
Starting a variable with a number is not valid. If a number is needed to index the variable name, place the number after the variable name.

### Variable Names Can Only Use Alphanumeric Characters
Variable names can contain characters `a-z`, `A-Z`, and `0-9` (as long as it is not at the beginning of the variable name).

```{note}
There are different naming convensions for variable names. 

|Naming Convension|Examples|Explination|
|-----------------|--------|-----------|
|**Snake Case**| `led_pin`<br> `sensor_val`<br>`number_of_students`|Words all lower case and separated by an underscore. **This is the prefeded naming convension by many Python programmers.**|
|**Camel Case**| `ledPin`<br> `sensorVal`<br>`numberOfStudents`|The first word is lower case, and all subsequent words are capitalized. This is valid but not seen as frequently as Snake Case.|
|**Pascal Case**|`LedPin`<br>`SensorVal`<br>`NumberOfStudents`|The first letter of every word is capitalixed. This is valid but discouraged. Pascal Case is used to identify classes.|
|**Uppercase**| `LED_PIN`<br>`SENSOR_VAL`<br>`NUMBER_OF_STUDENTS`|All letters are capitalized. This is valid but discouraged. Uppercase is used to identify constants (variables that should not be changed or reassigned). Python does not have true constants and having uppercase variable names helps distinguish these variables for others.|

Naming convensions may differ depending on the company or the project. It may be possible that a naming convension is set. To read more about the naming convensions in Python see [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/#naming-conventions). 

```

### Variables Cannot Have Whitespace
Whitespace is a character such as spaces or tabs.


### Variables Cannot Contain Special Characters Other Than an Underscore `_`. 
An underscore (`_`) is the only valid special or non-alphanumeric character allowed in variable names. This may make the variable more readable `myname` vs `my_name`.



### Variables Cannot Be Python or micro:bit MicroPython Keywords

#### Logical and Control Flow Keywords:
- **`and`**: Used for logical AND operations.
- **`or`**: Used for logical OR operations.
- **`not`**: Used for logical NOT operations.
- **`if`**, **`elif`**, **`else`**: Used for conditional statements.
- **`while`**: Used for creating loops.
- **`for`**: Used for iterating over sequences.
- **`break`**: Used to exit a loop prematurely.
- **`continue`**: Used to skip the current iteration and proceed to the next one.
- **`pass`**: A placeholder statement that does nothing.
- **`return`**: Used to exit a function and return a value.
- **`try`**, **`except`**, **`finally`**: Used for exception handling.
- **`assert`**: Used for debugging and ensuring conditions are met.
- **`with`**: Used for context management (e.g., file handling).
#### Data Types and Constants:
- **`True`**, **`False`**: Boolean constants.
- **`None`**: Represents the absence of a value (similar to null in other languages).
#### Function and Class Keywords:
- **`def`**: Used to define functions.
- **`class`**: Used to define classes.
#### Other Keywords:
**`global`**: Used to declare global variables.
**`lambda`**: Used to create anonymous functions.
**`yield`**: Used in generator functions.

#### micro:bit Keywords (Some are legal, but should be avoided)
- **`microbit`**: The micro:bit module name.
- TODO

## Python Naming Conventions



### Constants



## The Behavior of Variables

TODO



<iframe width="800" height="800" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=x%20%3D%201%0Aprint%28'x%20id%3A',%20id%28x%29%29%0A%0Ay%20%3D%202%0Aprint%28'y%20id%3A',%20id%28y%29%29%0A%0Az%20%3D%20y%0Aprint%28'z%20id%3A',%20id%28z%29%29%0A%0Ay%20%3D%20x%0Aprint%28'x%20id%3A',%20id%28x%29%29%0Aprint%28'y%20id%3A',%20id%28y%29%29%0Aprint%28'z%20id%3A',%20id%28z%29%29%0A%0Ax%20%3D%20'1'%0Aprint%28'x%20id%3A',%20id%28x%29%29%0Aprint%28'y%20id%3A',%20id%28y%29%29%0Aprint%28'z%20id%3A',%20id%28z%29%29&codeDivHeight=400&codeDivWidth=350&cumulative=true&curInstr=0&heapPrimitives=true&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

## Checkpoint: Identify the Valid and Invalid variable names.

Discuss the following:
- Which variable names are valid?
- Which variable names are invalid? 
- If the variable names are invalid, describe the reasoning.

**A**. `sensor 1 val`

**B**. `sensor1_val`

**C**. `1sensor_val`

**D**. `sensor1-val`

**E**. `sensor_v@l`

**F**. `SENSOR_VAL`

```{admonition} Click here to reveal the solutions.
:class: dropdown
Solution:
|     |Variable Name |Valid or Invalid|Reason                                                       |
|-----|--------------|----------------|-------------------------------------------------------------|
|**A**|`sensor 1 val`|***Invalid***   |The variable name has whitespace.                            |
|**B**|`sensor1_val` |**Valid**       |                                                             |
|**C**|`1sensor_val` |***Invalid***   |The variable name starts with a number.                      |
|**D**|`sensor1-val` |***Invalid***   |The variable name has a special character `-` other than `_`.|
|**E**|`sensor_v@l`  |***Invalid***   |The variable name has a special character `@` other than `_`.|
|**F**|`SENSOR_VAL`  |**Valid**       |                                                             |

```


```python
# Imports go at the top
from microbit import *

text = 'This is a Python string.'

while True:
    display.show(text)
```