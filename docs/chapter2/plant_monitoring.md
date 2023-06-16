# Advanced plant monitoring

In the first chapter, Logic gates were introduced. The mini-project programmed a OR gate in Python, and later implemented it onto the TinySpark development board.

During this mini-project, plant care is of highest regard. The _Fictioplantus_[^1], as can be read below, is a very delicate plant from the Botanica Kingdom. It requires careful control of both temperature and humidity, as it will grow very poorly when conditions are not right.

![Fictionplantus, plant passport](../assets/images/plant.png)

The requirements for succesful growth are very particular, they are summarized in the table below.

**Temperature**|**Humidity**|**Growth**
:-----:|:-----:|:-----:
below 25&deg;C|below 70&percnt;|no
above 25&deg;C|above 70&percnt;|no
below 25&deg;C|above 70&percnt;|yes
above 25&deg;C|below 70&percnt;|yes

[^1]:The Fictioplantus acts as a simplified plant example in our case, although principles learned in this project can be applied to real plant monitoring.

Classifying inputs like the temperature and humidity is a little more difficult than classifying simple logic gates. The reason behind this is the case of linear and non-linear separability[^2]. Separability refers to the property of a dataset or set of points (in this case our inputs) where it is possible to draw a straight line that can completely separate the points into different classes (below/above 25&deg; or below/above 70% humidity in our case). The problem proposed above is such a non-linearly separable problem. To overcome this, it is nescessary to introduce more neurons into the neural network.

[^2]:<https://en.wikipedia.org/wiki/Linear_separability>

---

![FCNN with weights](../assets/images/nn_2-2-1_weights.png)

The network from the [previous section](network_connections.md) is used here. Weights are defined as seen. For the activation function, the step function from [Chapter 1](../chapter1/logic_gates.md) is used again. Note how in this example, negative weights are also possible, and we introduce it to weight the first input of the output neuron.

$$ 
f(x) =
\begin{cases} 
      0 & \text{if } x < 0.5\\
     1 & \text{if } x \geq  0.5
\end{cases}
$$

$$
\displaylines{
\text{weight 1}=0.3\\
\text{weight 2}=-0.5\\
\text{weight 3}=-0.6\\
\text{weight 4}=0.4\\
\text{weight 5}=0.7\\
\text{weight 6}=0.5\\
}
$$

In order to process the inputs correctly, some pre-proccessing of the measurements needs to take place. The temperature and humidity will both be set around null and their inputs divided by 10: $temp_{in} = (temperature - 25) / 10$ and $humid_{in} = (humidity - 70) / 10$. This is done in order to make calculations easier, and to keep weights managable (in this case within ranges -1 and 1). In complicated neural networks, this pre-processing can be part of the network, in a so called Convolution step[^3].

[^3]:<https://en.wikipedia.org/wiki/Layer_(deep_learning)>

Calculating the outputs for some possible input combinations is now a little more complicated than in the previous chapter. As inputs, a few values above and below the threshold are chosen: $22$&deg;C and $30$&deg;C for temperature, $40$&percnt; and $85$&percnt; for humidity. In the calculations below, first the pre-processing of the values is done, then the repective outputs are calculated. Remember that because the activation function used is still a step function, the output will always be either $0$ or $1$ (signifying poor and good growing conditions respectively).

$$
\displaylines{
\text{input(22&deg;C)}=(22 - 25) / 10 = -0.3\\
\text{input(30&deg;C)}=(30 - 25) / 10 = 0.5\\
\text{input(40&percnt;)}=(40 - 70) / 10 = -3\\
\text{input(80&percnt;)}=(80 - 70) / 10 = 1\\
}
$$

$$
\displaylines{
\text{output(-0.3, -3)}=f(f(-0.3*0.3+-3*-0.5)*0.7+f(-0.3*-0.6+-3*0.4)*0.5)=0\\
\text{output(-0.3, 1)}=f(f(-0.3*0.3+1*-0.5)*0.7+f(-0.3*-0.6+1*0.4)*0.5)=1\\
\text{output(0.5, -3)}=f(f(0.5*0.3+-3*-0.5)*0.7+f(0.5*-0.6+-3*0.4)*0.5)=1\\
\text{output(0.5, 1)}=f(f(0.5*0.3+1*-0.5)*0.7+f(0.5*-0.6+1*0.4)*0.5)=0\\
}
$$

<!-- TODO: add tweaking of weights calculation -->

<!-- Now the inputs $1,1$ give the incorrect output of $1$, so again the weights need to be tweaked. Compared to the neuron in the last chapter, tweaking becomes more complicated in this network. Breaking down the calculation into small steps to see where the error occurs is a good way to start. -->

<!-- $$
\displaylines{
\text{output_hidden1}=f(1*0.2+1*0.3)=f(0.5)=1\\
\text{output_hidden2}=f(1*0.5+1*0.6)=f(1.1)=1\\
\text{output}=f(1*-0.4+1*0.9)=f(0.5)=1\\
}
$$ -->

<!-- To ensure the correct output of $0$, the output neuron calculation for needs to result in a value less than $0.5$ (as our activation-function $f(x)$ steps at $0.5$). If the weight $-0.4$ is tweaked to a value of $-0.5$, the activation function will not output $1$ anymore, since the result of the sum is $(1*-0.4 + 1*0.9)=0.4$. -->

<!-- TODO: add interactive tweaking of weights here, with some pointers to get it right -->

Now program this into a simple Python script. The weights of the network will be stored inside of an array. The inputs for temperature and humidity can be either input manually, or fetched from an external API that supplies weather data, such as the [Buienradar API](https://www.buienradar.nl/overbuienradar/gratis-weerdata).

[![Open In Colab](../assets/images/colab-badge.svg)](https://colab.research.google.com/drive/1n0ICeDesHq-a74yKYkdi2NV9295TgGCH#scrollTo=kK0VsuHfyz7M)

```python title="plant_monitoring.py"
# import the libraries to fetch weather data from an API
import requests
import json

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

# formulate the API request
response = requests.get('https://data.buienradar.nl/2.0/feed/json')

# get the temperature and humidity from the Buienradar API
# the location is currently set to De Bilt in the Netherlands
temperature = response.json()['actual']['stationmeasurements'][3]['temperature']
humidity = response.json()['actual']['stationmeasurements'][3]['humidity']
print(f"Temperature: {temperature}°C, Humidity: {humidity}%")

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

=> "Temperature: 16.7°C, Humidity: 66.0%"
=> "Growing conditions are good"
```

In the next section, the network will be deployed to the TinySpark development board, utilising the on-board environmental sensor.