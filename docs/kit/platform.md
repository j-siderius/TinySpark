# TinySpark platform

This page gives a quick overview of the the TinySpark platform (this webpage), how it functions, how to use it and where to find help if you need it.

---

The TinySpark platform is divided into several chapters:

- [Chapter 1: Introduction to neurons]
- [Chapter 2: Networks and structures]
- [Chapter 3: Training networks]
- [Chapter 4: Large models and Input shaping]
- [Chapter 5: Datatypes and more Projects]

<!-- sources -->
[Chapter 1: Introduction to neurons]:../chapter1/introduction.md
[Chapter 2: Networks and structures]:../chapter2/introduction.md
[Chapter 3: Training networks]:../index.md
[Chapter 4: Large models and Input shaping]:../index.md
[Chapter 5: Datatypes and more Projects]:../index.md

These chapters will introduce various concepts within (Tiny) Machine Learning in an engaging, interactive and project-based way. They can be accessed by clicking on the chapters here, or on the navigation bar at the top of the page.

![Navigation bar](../assets/images/navigation_bar.png)

The TinySpark platform uses several methods to teach, for example using textual explanation, formulas, code snippets and interactive applications.

Python code snippets will be introduced like this:

[![Open In Colab](../assets/images/colab-badge.svg)](https://colab.research.google.com/drive/1AoRa8GUn_qJEkL_W6yFm9ECDFSHOD0yD)

```python title="test_code.py"
# This is some Python code
a = 1
b = 2
c = a + b

print(c)

=> 3
```

The source code will be displayed on the page, with the option to open the code in [Google Colaboratory], a online code environment for Python notebooks. Any Python code that can be run on a PC (so no TinyML Development Kit code) will be available for testing and playing around on Colab; just click the link and a new notebook will open. If you want to interact this with the code, you need a Google account.

[Google Colaboratory]:https://colab.research.google.com/

TinyML development board code snippets will be introduced in the following manner:

[![Open In Github](../assets/images/github-badge.svg)]()

```python title="test_code_micro.py"
# This is some Python code for the TinyML development board
import board
import time
from digitalio import DigitalInOut, Direction

# LED setup
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

print("Hello from TinyML development board")

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.7)


=> "Hello from TinyML development board"
```

TinyML development board code is hosted on Github, since there is no online platform available for running this code. All TinyML code should be uploaded to the development board, as described in a later section.

Interactive applications will be shown as follows:

<script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.6.0/p5.js"></script>
<script>
let slider1;
let weights = [
  0.2,
  0.3,
  0.5,
  0.6,
  -0.4,
  0.9
];

function setup() {
  createCanvas(400, 400);
  
  slider1 = select('#weight5')
}

function draw() {
  background(220);
  
  weights[4] = slider1.value();
  
  fill(0, 102, 153);
  text('weight 1: ' + weights[0], 10, 30);
  text('weight 2: ' + weights[1], 10, 40);
  text('weight 3: ' + weights[2], 10, 50);
  text('weight 4: ' + weights[3], 10, 60);
  text('weight 5: ' + weights[4], 10, 70);
  text('weight 6: ' + weights[5], 10, 80);
  
  let outputs = [
    (((0*weights[0]+0*weights[1])>=0.5 ? 1 : 0)*weights[4] + ((0*weights[2]+0*weights[3])>=0.5 ? 1 : 0)*weights[5])>=0.5 ? 1 : 0,
    (((0*weights[0]+1*weights[1])>=0.5 ? 1 : 0)*weights[4] + ((0*weights[2]+1*weights[3])>=0.5 ? 1 : 0)*weights[5])>=0.5 ? 1 : 0,
    (((1*weights[0]+0*weights[1])>=0.5 ? 1 : 0)*weights[4] + ((1*weights[2]+0*weights[3])>=0.5 ? 1 : 0)*weights[5])>=0.5 ? 1 : 0,
    (((1*weights[0]+1*weights[1])>=0.5 ? 1 : 0)*weights[4] + ((1*weights[2]+1*weights[3])>=0.5 ? 1 : 0)*weights[5])>=0.5 ? 1 : 0,
  ];
    
  text('[0,0] = ' + outputs[0], 10, 100);
  text('[0,1] = ' + outputs[1], 10, 110);
  text('[1,0] = ' + outputs[2], 10, 120);
  text('[1,1] = ' + outputs[3], 10, 130);
}
</script>
<div>
  <label for="weight5">Weight 5</label>
  <input type="range" id="weight5" name="weight5" min="-1" max="1" value="-0.4" step="0.1">
</div>

To interact, click on the interactive window and start changing values, clicking on points etc. The animation will change and explain concepts in a tangible way.

In the next section, the TinyML Development Kit will be introduced.