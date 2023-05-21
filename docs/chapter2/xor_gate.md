# Fully-connected Neural Network

In the first chapter, Logic gates were introduced. The mini-project programmed a OR gate in Python, and later implemented it onto the TinySpark development board.

There are several more complex logic gates in electronics, such as the XOR gate [^1]. The XOR gate will only activate whenever one of it's inputs reads HIGH (or 1 in our case). The gate will however not activate if both inputs read HIGH (1) or LOW (0).

[^1]:https://en.wikipedia.org/wiki/XOR_gate

The logic table for an XOR gate looks like this:

**Input**||** Output**
:-----:|:-----:|:-----:
0|0|0
0|1|1
1|0|1
1|1|0

---

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
\text{output_hidden1}=f(0*0.2+1*0.3)=0
\text{output_hidden2}=f(0*0.5+1*0.6)=1
\text{output}=f(0*0.8+1*0.9)=1
}
$$

Calculating the outputs for all input combinations looks a lot more complicated than in the previous chapter:

$$
\displaylines{
\text{output(0,0)}=f(f(0*0.2+0*0.3)*0.8+f(0*0.5+0*0.6)*0.9)=0
\text{output(0,1)}=f(f(0*0.2+1*0.3)*0.8+f(0*0.5+1*0.6)*0.9)=1
\text{output(1,0)}=f(f(1*0.2+0*0.3)*0.8+f(1*0.5+0*0.6)*0.9)=1
\text{output(1,1)}=f(f(1*0.2+1*0.3)*0.8+f(1*0.5+1*0.6)*0.9)=1
}
$$

Now the inputs $1,1$ give the incorrect output of 1, so again the weights need to be tweaked. In the last chapter, the weight tweaking was performed through intuition, however in this more complicated network, this becomes harder. If the networks grow even bigger, intuitively determining the change in weights needed to achieve the correct outputs turns into an impossible task.

That's why in the next chapter, a new mathematical approach will be introduced to compute the needed changes to all weights.

**TODO: change text to still manually adjust, this chapter is just to introduce MLPs / FCNNs**