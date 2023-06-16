# import the library to take care of our pins
import board
from digitalio import DigitalInOut, Direction

# initialise the pins
button1 = DigitalInOut(board.BUTTON1)
button1.direction = Direction.INPUT
button2 = DigitalInOut(board.BUTTON2)
button2.direction = Direction.INPUT
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

# turn the LED on
led.value = True

# loop endlessly
while 1:
    # check if a button is pressed, and print if it is
    if button1.value is True:
        print("button1 pressed")
    if button2.value is True:
        print("button2 pressed")