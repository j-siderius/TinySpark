# Logic gates on the TinySpark development board

Now that we have implemented our first neuron 'network', let's see how we can transport this network to our TinySpark development kit.

We are going to use the two buttons, `button 1` and `button 2` on the development kit to simulate our inputs, and we will use an LED (`LED13`) to show if our output is LOW/0 or HIGH/1. In order to access the Inputs and Outputs of the development kit, we need some code.

[![Open In Github](../assets/images/github-badge.svg)]()

```python title="devboard_input_output.py"
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

# turn the LED on
led.value = True

# loop endlessly
while 1:
    # check if a button is pressed, and print if it is
    if button1.value is True:
        print("button1 pressed")
    if button2.value is True:
        print("button2 pressed")
```

![TinyML development board](../assets/images/devboard.png)

Now let's implement the logic from our last section, and build the neuron 'network' into our development board code.

[![Open In Github](../assets/images/github-badge.svg)]()

```python title="devboard_OR_gate.py"
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
```

Let's upload the code and see if our neuron works on the development board!