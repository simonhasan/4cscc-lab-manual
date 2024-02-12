# Variables

Variables in computer science are similar to variables in mathematics. In mathematics, variables represent a numerical value. In Python, variables can represent almost anything, such as strings, numbers, pins on the micro:bit, sensor values, etc.

Variables have to be declared or assigned to a name. To declare a variable you use the assignment operator `=`.

````
```{note}
The assignment operater `=` does not represent equality as it does in mathematics. To represent equality, see section TODO.
```
````

 ## Naming Variables

Variable names come with some constraints:

### Variable names cannot start with a number



### Variable names can use alphanumeric characters



### Variables cannot have whitespace (spaces)



### Variables can contain an underscore `_`. This may make the variable more readable `myname` vs `my_name`.



### Variables cannot be a Python or micro:bit MicroPython keywords

#### Logical and Control Flow Keywords:
- **`and`**: Used for logical AND operations.
- **`or`**: Used for logical OR operations.
- **`not`**: Used for logical NOT operations.
- `if`, `elif`, `else`: Used for conditional statements.
- `while`: Used for creating loops.
- `for`: Used for iterating over sequences.
- `break`: Used to exit a loop prematurely.
- `continue`: Used to skip the current iteration and proceed to the next one.
- `pass`: A placeholder statement that does nothing.
- `return`: Used to exit a function and return a value.
- `try`, `except`, `finally`: Used for exception handling.
- `assert`: Used for debugging and ensuring conditions are met.
- `with`: Used for context management (e.g., file handling).
#### Data Types and Constants:
- `True`, `False`: Boolean constants.
- `None`: Represents the absence of a value (similar to null in other languages).
#### Function and Class Keywords:
- `def`: Used to define functions.
- class: Used to define classes.
#### Other Keywords:
`global`: Used to declare global variables.
`lambda`: Used to create anonymous functions.
`yield`: Used in generator functions.
#### micro:bit Keywords (Some are legal, but should be avoided)
- `microbit`: The micro:bit module name.
- 



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
|**A**|`sensor 1 val`|**Invalid**     |The variable name has whitespace                             |
|**B**|`sensor1_val` |**Valid**       |                                                             |
|**C**|`1sensor_val` |**Invalid**     |The variable name starts with a number                       |
|**D**|`sensor1-val` |**Invalid**     |The variable name has special characters with other than `_`.|
|**C**|`sensor_v@l`  |**Invalid**     |The variable name has special characters with other than `_`.|
|**F**|`SENSOR_VAL`  |**Valid**       |                                                             |

```


```python
from microbit import *

text = 'This is a Python string.'

while True:
    display.show(text)
```