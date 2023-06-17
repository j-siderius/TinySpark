# Gesture recognition - deploying the model

Now it is time to deploy the trained model to the TinySpark development board. In order to do so, the recording code from [a previous section](../chapter3/gesture_recognition_data.md) is rewritten to accomodate the prediction. The trained weights are included in the code. Since the training phase of the neural network is not needed anymore, its code will not be included from [the previous section](../chapter3/gesture_recognition_training.md). The program will work by pressing `Button 1` and then recording a gesture. The on-board LED will be on when recording the gesture. The final prediction (the gesture with the highest probability) is printed to the serial console together with its probability.

[![Open In Github](../assets/images/github-badge.svg)](https://github.com/j-siderius/TinySpark/blob/main/docs/assets/examples/gesture_model.py)

```python title="gesture_model.py"
# Import all libraries
import time
import board
from apds9930.apds9930 import APDS9930
from digitalio import DigitalInOut, Direction, Pull

# Initialize I2C
i2c = board.I2C()
sensor = APDS9930(i2c)

# Initialise buttons 1 and 2
button1 = DigitalInOut(board.BUTTON1)
button1.direction = Direction.INPUT
button1.pull = Pull.UP
button2 = DigitalInOut(board.BUTTON2)
button2.direction = Direction.INPUT
button2.pull = Pull.UP

# Initialise LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

### Put the trained weights here ###
weights=[[0.664838063268332, 0.14475863419970098, 0.39798479496743655, -0.1996792640967368, -0.10042784907697525, -0.38665016231765525], [0.19784347834163832, -0.7106415457739413, 0.6545148412015216, 0.1258938146460059]]

# Define the activation function (linear)
def activation(x):
    return x

# Loop continuously
while True:

    # Check button 1 (note the signal is pulled up / high, so check for low signal)
    if button1.value == 0:

        # Startup delay
        recording = list()
        print("> Starting recording in 1sec")
        time.sleep(1)

        # Start recording
        led.value = 1
        distance = sensor.proximity
        recording.append(distance)
        print(f"{distance=}")
        # delay for 250ms
        time.sleep(0.250)
        distance = sensor.proximity
        recording.append(distance)
        print(f"{distance=}")
        # delay for another 250ms
        time.sleep(0.250)
        distance = sensor.proximity
        recording.append(distance)
        print(f"{distance=}")

        # Stop recording
        led.value = 0
        print("> Stopped recording")
    
        # Start predicting
        inputs = [r/100 for r in recording]

        # Calculate the output of the hidden layer
        hiddens = [
            activation(inputs[0] * weights[0][0] + inputs[1] * weights[0][1] + inputs[2] * weights[0][2]),
            activation(inputs[0] * weights[0][3] + inputs[1] * weights[0][4] + inputs[2] * weights[0][5])
        ]

        # Calculate the output from the output layer
        outputs = [
            activation(hiddens[0] * weights[1][0] + hiddens[1] * weights[1][1]),
            activation(hiddens[0] * weights[1][2] + hiddens[1] * weights[1][3]),
        ]

        # Print the prediction, keeping in mind that the output with the highest probability is picked
        if outputs[0] >= outputs[1]:
            print(f"Prediction: moving closer, p={outputs[0]}")
        else:
            print(f"Prediction: moving away, p={outputs[1]}")
    
    # Debounce the buttons
    time.sleep(0.01)
```

Deploy the model to the TinySpark development kit and add your trained weights to it. Press `Button 1` and see if the model predicted the gesture correctly.

??? info "Deployment problems"

    The trained model might behave differently than expected once it has been uploaded to the TinySpark development board. This could be due to a plethora of reasons, some are listed below.

    1. The measurement taken was not performed in the same way as the recordings during training (e.g. using a piece of cardboard vs your hand).
    2. The measurement taken was not performed in the same lighting conditions as the recordings during training (e.g. inside a dimly lit room vs outside).
    3. The model was trained using a narrow range of measurements (all measurements resembled each other very closely), this can lead to a skewed prediction model.
    4. The model was trained with too little samples.

---

In the next chapter, there will be some closing remarks, recommendations for further learning and project ideas to get you started on your own TinyML journey.