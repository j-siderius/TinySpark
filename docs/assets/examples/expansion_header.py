# Include all libraries
import time
import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn, AnalogOut

# Initialise all pins
pin10 = DigitalInOut(board.GPIO10)
pin10.direction = INPUT
pin11 = DigitalInOut(board.GPIO11)
pin11.direction = INPUT
pin12 = DigitalInOut(board.GPIO12)
pin12.direction = INPUT

pin47 = DigitalInOut(board.GPIO47)
pin47.direction = OUTPUT
pin48 = DigitalInOut(board.GPIO48)
pin48.direction = OUTPUT

pin6 = AnalogIn(board.GPIO6)
pin7 = AnalogIn(board.GPIO7)

pin9 = AnalogOut(board.GPIO9)

# Method for calculating voltage
def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# Check all pin values and change all outputs every second
while True:
    # Print all digital and analog readings
    print(f"{pin10.value=}, {pin11.value=}, {pin12.value=}, {get_voltage(pin6)=}, {get_voltage(pin7)=}") 
    
    # Reverse the digitalpin values
    pin47.value = not pin47.value
    pin48.value = not pin48.value

    # Ramp through the voltage
    if pin9.value < 65535:
        pin9.value += 1
    else:
        pin9.value = 0

    time.sleep(1)