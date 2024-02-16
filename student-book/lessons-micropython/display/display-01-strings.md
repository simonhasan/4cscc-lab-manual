# The String (`str`) Data Type

Computers manipulate data. Data can come in several forms. Not all data is handled the same way, so information is organized into different types. The same operations can be used to manipulate the data within data types. Consider the following examples:

`100` is a number that can be used in mathematical computations. The `'100'` in the sentence, `I have 100 things in my mind.' ` Is part of a sequence of characters. A series of characters in computer science is called a **string**. 

In Python, strings are characters between single `' '` or double `" "` quotes.

The three examples below the three examples below demonstrate how a numeric data type differs from a string:

**Example 1:**

<iframe src="https://trinket.io/embed/python3/f10fdf980c" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In Example 1, the numeric data type and the string data type can use the `+` operator, but the output is very different. In `1 + 2`, the `+` works as expected with numbers and functions as an addition operator, returning `3` . In `'1' + '2'`, the result is `12`. This is because with strings the `+` is what is known as a concatenation operator, meaning it links sequences of strings together. In `'1 + 2'`, the `+` is a character in the string. 

**Example 2:**

<iframe src="https://trinket.io/embed/python3/ce5a838eb2" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

In Example 3, when attempting to use a `+` between a string and an integer, the `TypeError` displayed below is returned. 

```bash
TypeError: can only concatenate str (not "int") to str
```

Python operates from left to right and encounters the string first, expecting another string to follow after the `+`.



**Example 3:**

<iframe src="https://trinket.io/embed/python3/fc0c9bc3f6" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

Similarly, when Python encounters the numeric data type first, it returns a different type error, expecting another numeric type after the `+`. This error can be seen below:

```bash
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

