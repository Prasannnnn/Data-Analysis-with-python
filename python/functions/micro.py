from machine import Pin
import time

# set up pin 15 as an input to read our button's state
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# intialising a timer variable we will use to keep track of time
timer = 0

while True:
    # this ensures that we check the button every second
    time.sleep(1)
    
    # if the button is pressed, then increase the timer by 1 second
    if button.value() == 1:
        timer = timer + 1
    
    # print the variable timer to the shell
    print(timer)