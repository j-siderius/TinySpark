<style> .md-footer__link--next:not([hidden]) { display: none } </style>

# Going futher with TinyML

This chapter will be used to give some closing remarks, recommendations for further learning and project ideas to get started on your own TinyML powered projects.

---

## Closing remarks

I hope that through the TinySpark platform and development kit, you have been able to lift the 'black box' that is often associated with machine learning (and subsequently TinyML). Through the step-by-step explanation of concepts and the mini-projects, you should have gained a better understanding of the mathematics and logic behind (Tiny) machine learning, as well its applicatoin areas. While there are certainly many more nuances to be learned regarding machine learning, and deployment to TinyML capable devices, you should have a solid basis to start from.

---

## Further learning

As could already be seen in the [previous chapter](../chapter3/gesture_recognition_training.md), there are quite some calculations involved with the training and deployment of neural networks. As there is much mathematics involved, it can quickly become quite overwhelming and opaque again. If you plan on further developing more extensive neural networks using the techniques learned here, it is recommended to write a Python library or at least a class for handeling all of the bookkeeping and calculations. Good starting points include the tutorial by [Déborah Mesquita on Real Python](https://realpython.com/python-ai-neural-network/#creating-the-neural-network-class), the tutorial by [Dr. Michael J. Garbade on KDnuggets](https://www.kdnuggets.com/2018/10/simple-neural-network-python.html) and the video series by [Andrej Karpathy called Zero to AI Hero](https://karpathy.ai/zero-to-hero.html). 

Alternatively, open source libraries such as [Tensorflow](https://www.tensorflow.org/) and [PyTorch](https://pytorch.org/) can be used to setup and train neural networks. These Python libraries support many more advanced features, and are maintained and updated regularly. For deploying models trained by Tensorflow, you can use the [Tensorflow Lite Micro](https://www.tensorflow.org/lite/microcontrollers) framework, that is very easily integrated into normal Tensorflow code. Specific examples that can be used on the TinySpark development kit can be found on the [Espressif TFLite Micro examples page](https://github.com/espressif/tflite-micro-esp-examples/tree/master). _Be aware that these machine learning frameworks produce neural networks that are not easily viewed or edited, as they are often deployed as compressed C code._

To learn more about TinyML in general, the [TinyML foundation](https://www.tinyml.org/) hosts regular (online) talks with industry experts. Harvard University heads the [Tiny Machine Learning Open Education Initiative](https://tinyml.seas.harvard.edu/) which includes many resources from (free) courses, online tutorials, code repositories and much more. Lastly, the [MIT HAN lab](https://hanlab.mit.edu/) has interesting examples and explanations on the compression and acceleration of neural networks and models.

---

## Project ideas

If you want to continue and develop your own TinyML powered projects using the TinySpark development board, here are some project ideas:

- Vibration detection by analysing time series data from the Inertial Motion sensor
- Wake word detection using the on-board Microphone
- Weather change prediction using the Pressure sensor
- Game intelligence such as Tic-Tac-Toe or Snake
- Package handeling analysis using the data from the Inertial Motion sensor
- Sentiment analysis from the pitch of voices using the Microphone
- Advanced plant monitoring using the Environmental sensor and Light sensor
- Infrared decoding of transmission signals using the on-board IR receiver
- Morse code decoding by time interval measurement
- Food quality prediction using the Environmental sensor
- Fall detection by analysing impact data from the Inertial Motion sensor
- Motor malfunction detection using the Hall effect sensor

By connecting some external sensors using the Expansion header or Stemma QT / Qwiic connector, some more interesting projects could be made:

- Perfect al-dente pasta cooking through temperature measurement
- Pulse monitoring and fatigue detection using a pulse-oximeter
- Leak detection using flow sensing valves
- Navigational aid using LIDAR sensing
- Fruit ripeness detection by using a colour sensor
- Soil condition determination by measuring moisture and acidity

---

## Featured projects

If you made an interesting project and want it displayed here, please contact me via [j-siderius@GitHub](https://github.com/j-siderius/)!

- 