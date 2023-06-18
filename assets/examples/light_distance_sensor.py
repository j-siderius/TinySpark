# Import all libraries
import time
import board
from apds9930.apds9930 import APDS9930

# Initialize I2C
i2c = board.I2C()
sensor = APDS9930(i2c)

# Print ALS at startup
time.sleep(1)
print(f"{sensor.als=}")

# Print the proximity continuously
while True:
    time.sleep(0.1)
    print(f"{sensor.proximity=}")