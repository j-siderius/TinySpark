# Include all libraries
import time
import board
from adafruit_bme280 import basic as adafruit_bme280

# Initialize I2C
i2c = board.I2C()
sensor = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Print all readings every 2 seconds
while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    print("Pressure: %0.1f hPa" % sensor.pressure)
    time.sleep(2)