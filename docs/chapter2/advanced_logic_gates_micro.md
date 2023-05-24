# Advanced logic gates on the TinySpark development board

Now that we have implemented our first neural network, let's deploy it to our TinySpark development kit.

Again, the two buttons, `button 1` and `button 2`, are used to simulate the inputs. The LED (`LED13`) will show if the output is LOW/0 or HIGH/1.

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
weights = [
     0.2,
     0.3,
     0.5,
     0.6,
    -0.5,
     0.9
]

# defining the activation function
def activation(x):
    if x >= 0.5:
        return 1
    else:
        return 0


# loop endlessly
while 1:
    input1 = button1.value
    input2 = button2.value

    neuron1 = activation( (input1 * weights[0]) + (input2 * weights[1]) )
    neuron2 = activation( (input1 * weights[2]) + (input2 * weights[3]) )
    output = activation( (neuron1 * weights[4]) + (neuron2 * weights[5]) )
    if output >= 0.5:
        # activation = 1
        led.value = True
    else:
        # activation = 0
        led.value = False
```

Let's upload the code and see if our network works on the development board!