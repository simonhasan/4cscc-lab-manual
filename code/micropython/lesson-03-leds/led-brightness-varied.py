# Imports go at the top
from microbit import *

# Set the LED pin
led_pin = pin1
# Set the brightness levels
led_off = 0              # 0 is off
led_one_quarter = 255    # 255 is 1/4 brightness
led_half = 511           # 511 is 1/2 brightness  
led_three_quarters = 767 # 767 is 3/4 brightness
led_full = 1023          # 1023 is full brightness

# Code in a 'while True:' loop repeats forever
while True:
    # Turn the LED on at 1/4 brightness
    led_pin.write_analog(led_one_quarter)
    # Wait for 500ms (0.5 seconds)
    sleep(500)
    # Turn the LED on at 1/2 brightness
    led_pin.write_analog(led_half)
    # Wait for 500ms (0.5 seconds)
    sleep(500)
    # Turn the LED on at 3/4 brightness
    led_pin.write_analog(led_three_quarters)
    # Wait for 500ms (0.5 seconds)
    sleep(500)
    # Turn the LED on at full brightness
    led_pin.write_analog(led_full)
    # Wait for 500ms (0.5 seconds)
    sleep(500)
    # Turn the LED off
    led_pin.write_digital(0)
    # Wait for 500ms (0.5 seconds)
    sleep(500)

