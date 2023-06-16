# Gesture recognition - training the model

To continue building the neural network that will recognise gestures, the mathemathics as discussed in a [previous section](../chapter3/training.md) will be implemented in Python. Then the aquired data from the [last section](../chapter3/gesture_recognition_data.md) will be used to train the network. Finally, the tuned weights will be used to run the model on the TinySpark development kit in order to detect gestures.

For this model, a neural network with two hidden neurons and two output neurons is chosen. Since three measurements are taken, three input neurons are required. For the output, two neurons are chosen, as to give the probability of each of the gestures: $\text{output1}=p(\text{moving closer})$ and $\text{output2}=p(\text{moving away})$. The weights are initialised randomly, since it is not possible to determine starting weights by hand in a meaningful way anymore. The randomisation uses a uniform random distribution between $-1$ and $1$. Below, a depiction of the described neural network can be found.

![Gesture neural network 3-2-2 with weights](../assets/images/nn_3-2-2_weights.png)

With the measurements take in the [previous section](../chapter3/gesture_recognition_data.md), one example calculation will be performed on a _moving closer_ measurement. All variables that belong together will be grouped into an array for convenience. Additionally, the linear activation function is defined.

$$
\displaylines{
\text{measurement}=[5.1, 46.7, 120.5]\\
\text{expected output}=[1, 0]\\
\text{weights}1=[-0.50, 0.22, -0.91, 0.61, 0.14, -0.48]\\
\text{weights}2=[0.73, 0.29, -0.29, -0.24]\\
f(x)=x\\
}
$$

Since the measurement values are quite large, and it is best to keep the weights in a network within managable ranges (e.g. between $-2$ and $2$), some pre-processing of the data needs to be performed again. For each measurement in the measurements array, the following calculation will be performed

$$
measurement_{in} = \frac{measurement}{100}
$$

$$
\displaylines{
\text{measurement}=[5.1, 46.7, 120.5]\\
\text{measurement}_{in}=[0.051, 0.467, 1.205]\\
}
$$

The hidden layer can now be determined by using the feedforward calculation.

$$
\displaylines{
\text{hidden}1=f(\text{measurement}_{in}1 * \text{weights}11 + \text{measurement}_{in}2 * \text{weights}12 + \text{measurement}_{in}3 * \text{weights}13)\\
\text{hidden}2=f(\text{measurement}_{in}1 * \text{weights}14 + \text{measurement}_{in}2 * \text{weights}15 + \text{measurement}_{in}3 * \text{weights}16)\\
\text{output}1=f(\text{hidden}1 * \text{weights}21 + \text{hidden}2 * \text{weights}22)\\
\text{output}2=f(\text{hidden}1 * \text{weights}23 + \text{hidden}2 * \text{weights}24)\\
}
$$

$$
\displaylines{
\text{hidden}1=-1.0193\\
\text{hidden}2=-0.4819\\
\text{output}1=-0.8839\\
\text{output}2=0.41126\\
}
$$

Now the error is calculated. Additionally, since there is more than one output, the _Loss_ is calculated. This serves as a measure of all error in the system (the compound error). There are many different loss functions[^1], but for the sake of simplicity, our loss function will just be a summation of the errors.

[^1]:<https://en.wikipedia.org/wiki/Loss_function>

$$
\displaylines{
    \text{error}1=\text{output}1 - \text{expected output}1 = -0.8839 - 1 = -1.8839\\
    \text{error}2=\text{output}2 - \text{expected output}2 = 0.41126 - 0 = 0.4116\\
    \text{loss}=\text{error}1 + \text{error}2 = -1.4723
}
$$

To now make the model a bit more accurate, backpropagation will be performed. First, the deltas of the output layer weights ($\text{weights}2$) will be calculated. This is again done by going 'backwards' and using the derivatives, as shown in one of the [previous sections](../chapter3/training.md).

$$
\displaylines{
\delta_{weights}21=f'(x)*\text{sum}'_{weights}21*\text{error}1=1*-1.0193*-1.8893=1.9258\\
\delta_{weights}22=f'(x)*\text{sum}'_{weights}22*\text{error}1=1*-0.4819*-1.8893=0.9105\\
\delta_{weights}23=f'(x)*\text{sum}'_{weights}23*\text{error}2=1*-1.0193*0.4116=-0.4195\\
\delta_{weights}24=f'(x)*\text{sum}'_{weights}24*\text{error}2=1*-0.4819*0.4116=-0.1984\\
}
$$

<!-- TODO: calculate one example by hand above -->

There are some nuances to keep in mind with this training program.

1. Since it is not possible any more to determine the starting weights by hand in a meaningful way, they are initialised randomly (using a uniform random distribution).
2. The system will output the probability $p$ that a gesture is either moving closer $[1, 0]$ or moving away $[0, 1]$.
3. In order to introduce some variance into the training, the samples are shuffled for each training cycle.
4. As done in the [previous chapter](../chapter2/plant_monitoring.md), the inputs are pre-processed: $measurement_{in} = \frac{measurement}{100}$. This is done in order to limit the range of weights.
5. A loss value is kept in order to check if the network is improving. This loss is printed every 10 training cycles in order to see the progress.

See if the model is able to train successfully on the measurements recorded in the [last section](../chapter3/gesture_recognition_data.md).

[![Open In Colab](../assets/images/colab-badge.svg)](https://colab.research.google.com/drive/1iXkkWpqd0snpFr8fS0Kxw4A0u2fysBC8#scrollTo=G1Upy1Z1iPvS)

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

If the loss at the end of training is satisfactory, the weights can be copied / stored and loaded into the model that runs on the TinySpark development kit. This will be done in the next section.

