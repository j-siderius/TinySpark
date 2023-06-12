# Gesture recognition - data aquisition

In this mini-project, a simple gesture recognition system will be built. Using the on-board proximity sensor introduced in the [TinySpark development section](../kit/devkit.md), three states will be detected: 

- no movement / no object
- moving closer
- moving away

To detect these gestures, a network that takes in multiple proximity readings needs to be devised. In this example, three measurements will be input into the network, one measurement that is current, one that was 250ms ago, and one that is 500ms ago. This _Time series_[^1] prediction method is a common way to analyse real-time sensor data using a neural network.

[^1]:<https://en.wikipedia.org/wiki/Time_series>

In order to train an accurate neural network, it is important to record actual data on the end device. One of the possible downsides of local, on-device machine learning

**TODO: write more on local recording / remote training**

![Recording data locally, processing / training remote, deploy locally](https://placehold.co/600x400?text=Device+>+Cloud+>+Device)

Starting off, some data needs to be recorded on the TinySpark development kit. The code below will start the recording of the datapoints one second after button 1 is pressed. The LED will show when a recording is made. After the recording has finished, the values will be stored in an array. Once button 2 is pressed, all datapoints are printed onto the serial console. From there, it is possible to copy them over to a training program, which will be discussed further along this section.

[![Open In Github](../assets/images/github-badge.svg)]()

```python title="gesture_data_recording.py"
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

# Array for storing the measurements
proximity_readings = list()

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
        proximity_readings.append(recording)

    # Check button 2
    elif button2.value == 0:

        # Print all recordings to the serial console, in form of an array
        print("Recordings: [-500ms, -250ms, current]")
        print("[")
        for recording in proximity_readings:
            print(f"[{recording[0]}, {recording[1]}, {recording[2]}],")
        print("]")

        # Clear the measurement storage
        proximity_readings = list()
        
        # Pause a bit after resetting
        time.sleep(1)

    # Debounce the buttons
    time.sleep(0.01)
```

To record some datapoints, press button 1 and when the LED turns on, then perform a gesture. After recording some datapoints, press button 2 to print them to the serial console. It is advisable to record all datapoints for one type of gesture, then print those, then continue to record the next type. _About 5 datapoints per gesture is enough for this example._

In the next section, the measurements will be run through the neural network and the weights will be trained using backpropagation.