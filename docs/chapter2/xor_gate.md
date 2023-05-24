# XOR gates

In the first chapter, Logic gates were introduced. The mini-project programmed a OR gate in Python, and later implemented it onto the TinySpark development board.

There are several more complex logic gates in electronics, such as the XOR gate [^1]. The XOR gate will only activate whenever one of it's inputs reads HIGH (or 1 in our case). The gate will however not activate if both inputs read HIGH (1) or LOW (0).

[^1]:<https://en.wikipedia.org/wiki/XOR_gate>

The logic table for an XOR gate looks like this:

**Input**||** Output**
:-----:|:-----:|:-----:
0|0|0
0|1|1
1|0|1
1|1|0

---

![FCNN](../assets/images/nn_2-2-1.png)

Defining the weights for the given network

$$
\displaylines{
\text{weight 1}=0.2\\
\text{weight 2}=0.3\\
\text{weight 3}=0.5\\
\text{weight 4}=0.6\\
\text{weight 5}=0.8\\
\text{weight 6}=0.9\\
}
$$

To calculate the output of the network with the given weights and inputs $0,1$, the calculation can be broken down into the following steps.

$$
\displaylines{
\text{output_hidden1}=f(0*0.2+1*0.3)=0\\
\text{output_hidden2}=f(0*0.5+1*0.6)=1\\
\text{output}=f(0*0.8+1*0.9)=1\\
}
$$

Calculating the outputs for all input combinations is now a little more complicated than in the previous chapter:

$$
\displaylines{
\text{output(0,0)}=f(f(0*0.2+0*0.3)*0.8+f(0*0.5+0*0.6)*0.9)=0\\
\text{output(0,1)}=f(f(0*0.2+1*0.3)*0.8+f(0*0.5+1*0.6)*0.9)=1\\
\text{output(1,0)}=f(f(1*0.2+0*0.3)*0.8+f(1*0.5+0*0.6)*0.9)=1\\
\text{output(1,1)}=f(f(1*0.2+1*0.3)*0.8+f(1*0.5+1*0.6)*0.9)=1\\
}
$$

Now the inputs $1,1$ give the incorrect output of $1$, so again the weights need to be tweaked. Compared to the neuron in the last chapter, tweaking becomes more complicated in this network. Breaking down the calculation into small steps to see where the error occurs is a good way to start.

$$
\displaylines{
\text{output_hidden1}=f(1*0.2+1*0.3)=1\\
\text{output_hidden2}=f(1*0.5+1*0.6)=1\\
\text{output}=f(1*0.8+1*0.9)=1\\
}
$$

To ensure the correct output of $0$, the final calculation for $output$ needs to result in a value less than $0.5$ (as our activation-function $f(x)$ steps at $0.5$).

Now program this into a simple Python script. The weights of the network will be stored inside of an array (ensure correct indexing).

**TODO: add more explanation**

[![Open In Colab](../assets/images/colab-badge.svg)](https://colab.research.google.com/drive/1n0ICeDesHq-a74yKYkdi2NV9295TgGCH#scrollTo=yqEmxnavsPhb)

```python title="small_network_XOR_gate.py"
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
weights = [
    0.2,
    0.3,
    0.5,
    0.6,
    0.8,
    0.9
]

def activation(x):
    if x >= 0.5:
        return 1
    else:
        return 0

for input in inputs:
    neuron1 = activation( (input[0] * weights[0]) + (input[1] * weights[1]) )
    neuron2 = activation( (input[0] * weights[2]) + (input[1] * weights[3]) )
    output = activation( (neuron1 * weights[4]) + (neuron2 * weights[5]) )

    print(input, output)

=> [0, 0]   0
=> [0, 1]   1
=> [1, 0]   1
=> [1, 1]   1
```

<!-- Now the inputs $1,1$ give the incorrect output of 1, so again the weights need to be tweaked. In the last chapter, the weight tweaking was performed through intuition, however in this more complicated network, this becomes harder. If the networks grow even bigger, intuitively determining the change in weights needed to achieve the correct outputs turns into an impossible task.

That's why in the next chapter, a new mathematical approach will be introduced to compute the needed changes to all weights.

**TODO: change text to still manually adjust, this chapter is just to introduce MLPs / FCNNs** -->