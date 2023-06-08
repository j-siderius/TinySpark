# Import all libraries
import time
import board
from adafruit_lsm6ds.lsm6ds3trc import LSM6DS3TRC

# Initialize I2C
i2c = board.I2C()
sensor = LSM6DS3TRC(i2c, address=0x6b)

# Print the data continuously
while True:
    print("Acceleration: X:%.5f, Y: %.5f, Z: %.5f m/s^2" % (sensor.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (sensor.gyro))
    print("")
    time.sleep(0.1)