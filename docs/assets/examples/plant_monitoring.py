# import the libraries to take care of our sensor and manage time
import board
import time
from adafruit_bme280 import basic as adafruit_bme280

# initialise the environmental sensor
i2c = board.I2C()
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# store our weights
weights = [
    0.3,
    -0.5,
    -0.6,
    0.4,
    0.7,
    0.5
]

# defining the activation function
def activation(x):
    if x >= 0.5:
        return 1
    else:
        return 0

# loop endlessly
while 1:
    # get the sensor readings and print them
    temperature = bme280.temperature
    humidity = bme280.relative_humidity
    print(f"Temperature: {temperature}, Humidity: {humidity}")

    # pre-processing the inputs
    temp_in = (temperature - 25) / 10
    humid_in = (humidity - 70) / 10

    # perform network calculations
    neuron1 = activation( (temp_in * weights[0]) + (humid_in * weights[1]) )
    neuron2 = activation( (temp_in * weights[2]) + (humid_in * weights[3]) )
    output = activation( (neuron1 * weights[4]) + (neuron2 * weights[5]) )

    # printing the result
    if output == 1:
        print("Growing conditions are good")
    else:
        print("Growing conditions are poor")

    # perform the prediction every 2 seconds to see if it has changed
    time.sleep(2)