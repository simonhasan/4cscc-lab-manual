# The `on start` and `forever` Blocks

When MakeCode is first loaded, two blocks are preloaded by default.

![blocks-on-start-forever](assets/blocks-on-start-forever.png)

## The `on start` Block



![block-on-start](assets/block-on-start.png)



## The `forever` Block

The `forever` block is a particular block representing a **loop** in MakeCode, particularly an **infinite loop**. Loops are control structures that allow the repetition of a set of instructions or a set of code blocks. Typically, there is a **terminating condition** that enables the flow of the code to exit the loop. An infinite loop repeats a set of instructions infinitely or continuously without a terminating condition. 

```{note}
Infinite loops are used frequently when coding with microcontrollers. In other coding applications, infinite loops are often undesireable as they can cause the program to be become unresponsibe or use much of the processers capabilities.
```



The `forever` block is displayed below with a `show string` block with the string `"Hello!"`.

![block-forever](assets/block-forever.png)

This code displays the string `"Hello"`across the micro:bit display in an infinite loop (forever/again and again...)