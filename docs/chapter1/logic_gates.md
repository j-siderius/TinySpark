# Logic gates

A logic gate (in electronics), is a device which performs logical operations using binary logic. Logic gates are the fundaments of modern processors, enabling chips to store data using Latches[^1], perform binary calculations using Arithmic Logic Units[^2] and much more.

[^1]:https://en.wikipedia.org/wiki/Flip-flop_(electronics)
[^2]: https://en.wikipedia.org/wiki/Arithmetic_logic_unit

In this first Mini-project, we will build a single-neuron 'network' to replicate the behaviour of an OR logic gate[^3]. The OR gate will activate whenever either of it's inputs reads HIGH (or 1 in our case).

[^3]: https://en.wikipedia.org/wiki/OR_gate

The logic table for an OR gate looks like this:

**Input**||** Output**
:-----:|:-----:|:-----:
0|0|0
0|1|1
1|0|1
1|1|1

---

In order to make writing our equations a bit easier, let's combine the sum and activation function:

$$
\text{output}=f(\sum\text{inputs}*\text{weights})
$$

Now try if the neuron from the [previous section](neuron.md) does the trick:

$$
\displaylines{
\text{input 1}=0\\
\text{input 2}=0\\
\text{weight 1}=0.3\\
\text{weight 2}=0.9\\
}
$$

$$
\text{output}=f(0*0.3+0*0.9)=0
$$

That looks promising, let's try the other input combinations:

$$
\displaylines{
\text{output}=f(0*0.3+1*0.9)=1 \\
\text{output}=f(1*0.3+0*0.9)=0 \\
\text{output}=f(1*0.3+1*0.9)=1 \\
}
$$

We are almost there, however with the inputs $1,0$ we get the wrong output of $0$, which should be $1$ (according to our logic table above).

How can we change this behaviour? <br> We need to change the weights!

Let's take a closer look at the wrong output:

$$
\text{sum}=\text{input 1}*\text{weight 1}+\text{input 2}+\text{weight 2}\\
=1*0.3+0*0.9=0.3
$$

Indeed, if we run this through our activation function, we get:

$$
f(0.3)=0
$$

Which is not what we want. Out sum output of $0.3$ is too low to trigger the activation function. If we intuitively look at the sum above, we can conclude a couple of things:

- the inputs cannot be changed
- the weights could be changed
- the activation function could be changed

In neural networks, we normally want to change the weights, and only change the activation function if we get totally wrong outputs for all inputs (which is not the case here).

In order to trigger the activation function, the sum for inputs $1,0$ needs to be higher than or equal to 0.5 in order to trigger $f(x)$. If we increase $\text{weight 1}=0.5$ for example, let's recalculate all outputs and see if our 'network' is correct.

$$
\displaylines{
\text{output}=f(0*0.5+0*0.9)=0 \\
\text{output}=f(0*0.5+1*0.9)=1 \\
\text{output}=f(1*0.5+0*0.9)=1 \\
\text{output}=f(1*0.5+1*0.9)=1 \\
}
$$

Let's program this into a simple Python script. To make sure that we cover all possible inputs our OR-gate might receive, we will store those inside of an array. We will then loop over all possible inputs and create an output for each.

```python title="single_neuron_OR_gate.py"
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
weight1 = 0.5
weight2 = 0.9

for input in inputs:
    sum = (input[0] * weight1) + (input[1] * weight2)
    if sum >= 0.5:
        activation = 1
    else:
        activation = 0
    
    print(input, activation)

=> [0, 0]   0
=> [0, 1]   1
=> [1, 0]   1
=> [1, 1]   1
```

You hand-programmed your first neuron-network!