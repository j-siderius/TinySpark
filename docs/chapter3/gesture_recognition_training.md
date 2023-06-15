# Gesture recognition - training the model

To continue building the neural network that will recognise gestures, the mathemathics as discussed in a [previous section](../chapter3/training.md) will be implemented in Python. Then the aquired data from the [last section](../chapter3/gesture_recognition_data.md) will be used to train the network. Finally, the tuned weights will be used to run the model on the TinySpark development kit in order to detect gestures.

There are some nuances to keep in mind with this training program.

1. Since it is not possible any more to determine the starting weights by hand in a meaningful way, they are initialised randomly (using a uniform random distribution).
2. The system will output the probability $p$ that a gesture is either moving closer $[1, 0]$ or moving away $[0, 1]$.
3. In order to introduce some variance into the training, the samples are shuffled for each training cycle.
4. As done in the [previous chapter](../chapter2/plant_monitoring.md), the inputs are pre-processed: $measuremt_{in} = \frac{measurement}{100}$. This is done in order to limit the range of weights.
5. A loss value is kept in order to check if the network is improving. This loss is printed every 10 training cycles in order to see the progress.

See if the model is able to train successfully on the measurements recorded in the [last section](../chapter3/gesture_recognition_data.md).

[![Open In Colab](assets/images/colab-badge.svg)](https://colab.research.google.com/drive/1iXkkWpqd0snpFr8fS0Kxw4A0u2fysBC8#scrollTo=G1Upy1Z1iPvS)

```python title="training_model.py"
# Import the random library to initialise the weights
import random

### Put the recorded measurements here ### 
moving_closer = [
  [0.0, 35.5, 120.1],
  [2.625, 33.375, 127.875],
  [19.0, 56.375, 127.875],
  [47.875, 51.375, 127.875],
  [40.125, 89.375, 127.875]
]

moving_away = [
  [104.54, 2.375, 0.0],
  [127.875, 33.625, 5.4],
  [120.3, 39.125, 0.0],
  [127.875, 103.25, 23.8],
  [127.875, 29.25, 0.0]
]

# Labeling the collected data, outputting the probability of that gesture
# output1 = p(moving closer), output2 = p(moving away)
moving_closer_labeled = [(sample, [1, 0]) for sample in moving_closer]
moving_away_labeled = [(sample, [0, 1]) for sample in moving_away]

# Making one pile of samples from the split samples above
samples = moving_closer_labeled + moving_away_labeled

# Initialise the weights for the network randomly, define the learning rate and epochs (itterations)
weights = [
    [random.uniform(-0.1, 0.1) for _ in range(6)],
    [random.uniform(-0.1, 0.1) for _ in range(4)]
]
learning_rate = 0.01
epochs = 100

# Define the activation function (linear)
def activation(x):
    return x

# Run the training for the configured epochs
for epoch in range(epochs):

    # Shuffle the samples in order to introduces some variance into the training
    random.shuffle(samples)

    # Define a total loss for the whole system
    loss = 0.0

    # Run through all samples
    for sample in samples:

        # Separate the inputs and expected outputs from the sample, pre-processing the inputs
        inputs = [s/100 for s in sample[0]]
        expected = sample[1]

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

        # Calculate the errors
        errors = [
            outputs[0] - expected[0],
            outputs[1] - expected[1]
        ]

        # Add the errors to the system loss
        loss += errors[0] + errors[1]

        # Calculate the deltas for each weight
        deltas = [
            [
                errors[0] * 1 * hiddens[0] * 1 * inputs[0] + errors[1] * 1 * hiddens[0] * 1 * inputs[0],
                errors[0] * 1 * hiddens[0] * 1 * inputs[1] + errors[1] * 1 * hiddens[0] * 1 * inputs[1],
                errors[0] * 1 * hiddens[0] * 1 * inputs[2] + errors[1] * 1 * hiddens[0] * 1 * inputs[2],
                errors[0] * 1 * hiddens[1] * 1 * inputs[0] + errors[1] * 1 * hiddens[1] * 1 * inputs[0],
                errors[0] * 1 * hiddens[1] * 1 * inputs[1] + errors[1] * 1 * hiddens[1] * 1 * inputs[1],
                errors[0] * 1 * hiddens[1] * 1 * inputs[2] + errors[1] * 1 * hiddens[1] * 1 * inputs[2],
            ],
            [
                errors[0] * 1 * hiddens[0],
                errors[0] * 1 * hiddens[1],
                errors[1] * 1 * hiddens[0],
                errors[1] * 1 * hiddens[1]
            ]
        ]

        # Apply the calculated deltas to the weights, keeping in mind the learning rate
        for layer in range(len(weights)):
            for weight in range(len(weights[layer])):
                weights[layer][weight] -= learning_rate * deltas[layer][weight]

    # Print the loss every 10 epochs in order to check progress
    if epoch % 10 == 0:
        print(f"{epoch:} {loss=}")

# Print the final loss of the system and the weights
print(f"{loss=}")
print(f"{weights=}")
```



