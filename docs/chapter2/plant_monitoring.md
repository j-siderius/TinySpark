# Plant monitoring

In the first chapter, Logic gates were introduced. The mini-project programmed an OR gate in Python, and later implemented it onto the TinySpark development board.

During this mini-project, plant care is of highest regard. The _Fictioplantus_[^1], as can be read below, is a very delicate plant from the Botanica Kingdom. It requires careful control of both temperature and humidity, as it will grow very poorly when conditions are not right.

![Fictionplantus, plant passport](../assets/images/plant.png)

The requirements for succesful growth are very particular, they are summarized in the table below.

**Temperature**|**Humidity**|**Growth**
:-----:|:-----:|:-----:
below 25&deg;C|below 70&percnt;|no
above 25&deg;C|above 70&percnt;|no
below 25&deg;C|above 70&percnt;|yes
above 25&deg;C|below 70&percnt;|yes

[^1]:The Fictioplantus acts as a simplified plant example in this case, although principles learned in this project can be applied to real plant monitoring.

Classifying inputs like the temperature and humidity is more difficult than classifying simple logic gates. The reason behind this is the case of linear and non-linear separability[^2]. Separability refers to the property of a dataset or set of points (in this case the inputs) where it is possible to draw a straight line that can completely separate the points into different classes (below/above 25&deg; or below/above 70% humidity in this case). The problem proposed above is such a non-linearly separable problem. To overcome this, it is nescessary to introduce more neurons into the neural network.

[^2]:<https://en.wikipedia.org/wiki/Linear_separability>

---

![FCNN with weights](../assets/images/nn_2-2-1_weights.png)

The network from the [previous section](network_connections.md) is used here. Weights are defined as seen. For the activation function, the step function from [Chapter 1](../chapter1/logic_gates.md) is used again. Note how in this example, negative weights are also possible in order to give inputs negative influences as well.

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

In order to process the inputs correctly, some pre-proccessing of the measurements needs to take place. This is done in order to make calculations easier, and to keep weights managable (in this case within ranges -1 and 1). The calculation is described below. In complicated neural networks, this pre-processing can be part of the network, in a so called Convolution step[^3].

$$
\displaylines{
temp_{in} = (temperature - 25) / 10\\
humid_{in} = (humidity - 70) / 10\\
}
$$

[^3]:<https://en.wikipedia.org/wiki/Layer_(deep_learning)>

Calculating the outputs for some possible input combinations is now more complicated than in the previous chapter. As inputs, a few values above and below the threshold are chosen: $22$&deg;C and $30$&deg;C for temperature, $40$&percnt; and $85$&percnt; for humidity. In the calculations below, first the pre-processing of the values is done, then the respective outputs are calculated. Remember that because the activation function used is still a step function, the output will always be either $0$ or $1$ (signifying poor and good growing conditions respectively).

$$
\displaylines{
\text{input(22&deg;C)}=(22 - 25) / 10 = -0.3\\
\text{input(30&deg;C)}=(30 - 25) / 10 = 0.5\\
\text{input(40&percnt;)}=(40 - 70) / 10 = -3\\
\text{input(80&percnt;)}=(80 - 70) / 10 = 1\\
}
$$

??? info "Network calculation results"

    For the weights above, the calculated predictions for the network can be found below. 

    $$
    \displaylines{
    \text{output(-0.3, -3)}=f(f(-0.3*0.3+-3*-0.5)*0.7+f(-0.3*-0.6+-3*0.4)*0.5)=0\\
    \text{output(-0.3, 1)}=f(f(-0.3*0.3+1*-0.5)*0.7+f(-0.3*-0.6+1*0.4)*0.5)=1\\
    \text{output(0.5, -3)}=f(f(0.5*0.3+-3*-0.5)*0.7+f(0.5*-0.6+-3*0.4)*0.5)=1\\
    \text{output(0.5, 1)}=f(f(0.5*0.3+1*-0.5)*0.7+f(0.5*-0.6+1*0.4)*0.5)=0\\
    }
    $$

Using the interactive visualisation below, try to tune the weights so that the prediction is correct for the given inputs. The weights given above can be used as guidance, however there are many different possible combinations of weights to be found that will lead to the desired output. _Note that this tuning is meant more as a exercise to see what effects weights have in a neural network. It is expected to be very difficult to find correct weights by hand._

<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.6.0/p5.js"></script>
<script>
let img;

function preload() {
    img = loadImage('https://j-siderius.github.io/TinySpark/assets/images/nn_2-2-1.png')
}

let slider1;
let weights = [
  0,0,0,0,0,0
];
  
function setup() {
  const canvas = createCanvas(600, 400);
  canvas.parent('sketch-holder');

  slider1 = select('#weight1');
  slider2 = select('#weight2');
  slider3 = select('#weight3');
  slider4 = select('#weight4');
  slider5 = select('#weight5');
  slider6 = select('#weight6');
  
  sliderT = select('#temp');
  sliderH = select('#humid');
}

function draw() {
  clear();

  image(img, -50, -30);
  
  weights[0] = slider1.value();
  weights[1] = slider2.value();
  weights[2] = slider3.value();
  weights[3] = slider4.value();
  weights[4] = slider5.value();
  weights[5] = slider6.value();
  
  temperature = sliderT.value();
  humidity = sliderH.value();
  
  fill(0, 128, 128);
  textSize(18);
  text('w1 = '+ weights[0], 175, 80);
  text('w2 = '+ weights[1], 225, 160);
  text('w3 = '+ weights[2], 225, 230);
  text('w4 = '+ weights[3], 175, 320);
  text('w5 = '+ weights[4], 400, 150);
  text('w6 = '+ weights[5], 400, 250);
  
  text('Temperature: ' + temperature + 'C', 50, 30);
  text('Humidity: ' + humidity + '%', 225, 30);
  
  let hidden1 = (((temperature-25)/10)*weights[0] + ((humidity-70)/10)*weights[1])>=0.5 ? 1 : 0;
  let hidden2 = (((temperature-25)/10)*weights[2] + ((humidity-70)/10)*weights[3])>=0.5 ? 1 : 0;
  let output = ((hidden1)*weights[3] + (hidden2)*weights[4])>=0.5 ? 1 : 0;
  
  text('Output: ' + output, 510, 200);
}
</script>
<div>
    <div id="sketch-holder"></div>
    <label for="weight1">Weight 1</label>
    <input type="range" id="weight1" name="weight1" min="-1" max="1" value="0" step="0.1"><br>
    <label for="weight2">Weight 2</label>
    <input type="range" id="weight2" name="weight2" min="-1" max="1" value="0" step="0.1"><br>
    <label for="weight3">Weight 3</label>
    <input type="range" id="weight3" name="weight3" min="-1" max="1" value="0" step="0.1"><br>
    <label for="weight4">Weight 4</label>
    <input type="range" id="weight4" name="weight4" min="-1" max="1" value="0" step="0.1"><br>
    <label for="weight5">Weight 5</label>
    <input type="range" id="weight5" name="weight5" min="-1" max="1" value="0" step="0.1"><br>
  <label for="weight6">Weight 6</label>
    <input type="range" id="weight6" name="weight6" min="-1" max="1" value="0" step="0.1"><br>
  
  <label for="temp">Temperature</label>
    <input type="range" id="temp" name="temp" min="20" max="30" value="23" step="1"><br>
  <label for="humid">Humidity</label>
    <input type="range" id="humid" name="humid" min="20" max="90" value="40" step="5">
</div>

Now program the found weights (of the pre-given ones) into a simple Python script. The weights of the network will be stored inside of an array. The inputs for temperature and humidity can be either input manually, or fetched from an external API[^4] that supplies weather data, such as the Dutch weather forecast [Buienradar API](https://www.buienradar.nl/overbuienradar/gratis-weerdata).

[^4]:<https://en.wikipedia.org/wiki/API>

[![Open In Colab](../assets/images/colab-badge.svg)](https://colab.research.google.com/drive/1n0ICeDesHq-a74yKYkdi2NV9295TgGCH#scrollTo=kK0VsuHfyz7M)

```python title="plant_monitoring.py"
# import the libraries to fetch weather data from an API
import requests
import json

# store the weights
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

# Alternatively, input the temperature and humidity manually
# temperature = 23
# humidity = 65

# Print the inputs
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
```

In the next section, the network will be deployed to the TinySpark development board, utilising the on-board environmental sensor.