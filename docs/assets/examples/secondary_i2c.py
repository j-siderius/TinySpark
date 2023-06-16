# import needed libraries
import busio
from board import *

# define the secondary i2c object with the new pins
i2c2 = busio.I2C(GPIO16, GPIO17)

# use the i2c2 object below