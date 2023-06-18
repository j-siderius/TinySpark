# import the library to take care of the pins
import board
from digitalio import DigitalInOut, Direction, Pull

# initialise the pins
button1 = DigitalInOut(board.BUTTON1)
button1.direction = Direction.INPUT
button1.pull = Pull.UP
button2 = DigitalInOut(board.BUTTON2)
button2.direction = Direction.INPUT
button2.pull = Pull.UP
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

# turn the LED on
led.value = True

# loop endlessly
while 1:
    # check if a button is pressed, and print if it is (buttons are pulled HIGH, so check for low)
    if not button1.value:
        print("button1 pressed")
    if not button2.value:
        print("button2 pressed")