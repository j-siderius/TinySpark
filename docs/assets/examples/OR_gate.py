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

# store our weights
weight1 = 0.5
weight2 = 0.9

# loop endlessly
while 1:
    input1 = button1.value
    input2 = button2.value

    sum = (input1 * weight1) + (input2 * weight2)
    if sum >= 0.5:
        # activation = 1
        led.value = True
    else:
        # activation = 0
        led.value = False