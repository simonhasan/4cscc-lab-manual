# The Boolean (`bool`) Data Type

TODO

Up until this point, two data types have been presented. These data types are reviewed below:

## Reviewing Data Types

### Strings

A  string is a data type used for a character or a sequence of characters. Strings are characters between quotes `' '` or double quotes `" "`. 



### Integers





## The Boolean Data Type



### About



### Truth Tables



### Boolean Operators

#### Boolean Operators in Mathematics



| $p$  | $q$  | $p\land q$ | $p\lor q$ |
| ---- | ---- | ---------- | --------- |
| T    | T    | T          | T         |
| T    | F    | F          | T         |
| F    | T    | F          | T         |
| F    | F    | F          | F         |



| $p$  | $q$  | $\neg p$ | $\neg q$ |
| ---- | ---- | -------- | -------- |
| T    | T    | F        | F        |
| T    | F    | F        | T        |
| F    | T    | T        | F        |
| F    | F    | T        | T        |



| $p$  | $q$  | $\neg p$ | $\neg q$ | $p\land q$ | $p\lor q$ | $\neg p \land q$ | $p \land \neg q$ | $\neg p \land \neg q$ | $\neg p \lor q$ | $p \lor \neg q$ | $\neg p \lor \neg q$ |
| ---- | ---- | -------- | -------- | ---------- | --------- | ---------------- | ---------------- | --------------------- | --------------- | --------------- | -------------------- |
| T    | T    | F        | F        | T          | T         | F                | F                | F                     | T               | T               | F                    |
| T    | F    | F        | T        | F          | T         | F                | T                | F                     | F               | T               | T                    |
| F    | T    | T        | F        | F          | T         | T                | F                | F                     | T               | F               | T                    |
| F    | F    | T        | T        | F          | F         | F                | F                | T                     | T               | T               | T                    |



#### Boolean Operators in Python
