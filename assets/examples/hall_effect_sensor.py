# Import all libaries
import time
import board
from analogio import AnalogIn

# Initialise the pin
analog_in = AnalogIn(board.HALL_EFFECT)

# Calibrated sensor values
_quiescentV = 1.57332
_sensitivity = 0.0016

# Calculate the magnetic Gauss from the Hall effect sensor
def get_gauss():
    measuredV = (analog_in.value * 3.3) / 65536
    gauss = (measuredV - _quiescentV) / _sensitivity
    return gauss

# Check the magnetic field every second
while True:
    print(f"{get_gauss()} GS")
    time.sleep(1)