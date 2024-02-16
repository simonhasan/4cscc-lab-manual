# Building an LED Circuit

TODO

## Building an LED Circuit with the Adafruit Dragontail (Or Similar Type)

Insert the micro:bit into the micro:bit to the Adafruit Dragontail.

![blink-led-diagram-adafruit-00](assets/blink-led-diagram-adafruit-00.png)

Insert the LED into the breadboard. 

- **Make sure that the LED and the cathode are not on the same row on the breadboard. **
- **Take note of which lead is the anode.**

```{tip}
Chose a side that the LED lead will always be facing (right or left). This helps prevent incomplete circuits and makes it easier to remember which lead is the anode and which lead is the cathode. 
```



![blink-led-diagram-adafruit-01](assets/blink-led-diagram-adafruit-01.png)

Attach a resistor to the row with the cathode lead of the LED.

```{note}
The resistor can be attached to either the anode or the cathode in an LED circuit. Pick one lead (either anode or cathode) and attach it to that lead every time an LED circuit is built. 
```



![blink-led-diagram-adafruit-02](assets/blink-led-diagram-adafruit-02.png)

Attach the resistor to the GND rail on the side of the breadboard.

```{note}
It is also possible to use the resistor as the lead from the GND rail to the cathode.
```



![blink-led-diagram-adafruit-03](assets/blink-led-diagram-adafruit-03.png)

Place a jumper wire from the row attached to Pin 1 to the row with the anode.

![blink-led-diagram-adafruit-04](assets/blink-led-diagram-adafruit-04.png)

The circuit is complete.

![blink-led-adafruit](assets/blink-led-adafruit.png)

---

## Building an LED Circuit with an ELECFREAKS micro:bit Breakout Board (Or Similar Type)

Insert the micro:bit into the micro:bit to the breakout board.

![blink-led-diagram-elecfreaks-00](assets/blink-led-diagram-elecfreaks-00.png)

Insert the LED into the breadboard. 

- **Make sure that the LED and the cathode are not on the same row on the breadboard. **
- **Take note of which lead is the anode.**

```{tip}
Chose a side that the LED lead will always be facing (right or left). This helps prevent incomplete circuits and makes it easier to remember which lead is the anode and which lead is the cathode. 
```



![blink-led-diagram-elecfreaks-01](assets/blink-led-diagram-elecfreaks-01.png)

Attach a resistor to the row with the cathode lead of the LED.

```{note}
The resistor can be attached to either the anode or the cathode in an LED circuit. Pick one lead (either anode or cathode) and attach it to that lead every time an LED circuit is built. 
```

![blink-led-diagram-elecfreaks-02](assets/blink-led-diagram-elecfreaks-02.png)

Attach the resistor to a GND pin.

```{note}
Any GND pin will work on these types of breakout boards. The GND pin does not need to be adjacent to the GPIO pin.
```



![blink-led-diagram-elecfreaks-03](assets/blink-led-diagram-elecfreaks-03.png)

Place a jumper wire from the Pin 1 to the row with the anode.

![blink-led-diagram-elecfreaks-04](assets/blink-led-diagram-elecfreaks-04.png)

The circuit is complete.

![blink-led-elecfreaks](assets/blink-led-elecfreaks.png)

---

## Building an LED Circuit with the SpakFun Qwiic micro:bit Breakout Board (Or Similar Type)

TODO

![blink-led-diagram-sparkfun-00](assets/blink-led-diagram-sparkfun-00.png)

TODO

![blink-led-diagram-sparkfun-01](assets/blink-led-diagram-sparkfun-01.png)

TODO

![blink-led-diagram-sparkfun-02](assets/blink-led-diagram-sparkfun-02.png)

TODO

![blink-led-diagram-sparkfun-03](assets/blink-led-diagram-sparkfun-03.png)

TODO

![blink-led-diagram-sparkfun-04](assets/blink-led-diagram-sparkfun-04.png)

The circuit is complete.

![blink-led-sparkfun](assets/blink-led-sparkfun.png)

---

## Troubleshooting the LED Circuit

If the LED is not illuminating:

- Check that the anode and cathode leads are not on the same row on the breadboard.
- Check that the GPIO pin is the correct GPIO pin in the code.
- Check that the GPIO pin is connected to the anode.
- Check that the cathode is connected to GND.
- Check that the resistor is connected to the anode and the GND. 

