# Training networks

In the last chapters, neuron weights were intuitively tuned to produce precise predictions. The mathematical approach to tuning weights will be explained a little more methodically. The following network will be used to explain the training.

![Training NN](https://placehold.co/600x400?text=Training+NN+2x2x2)

The network is initialised with pseudo-random weight values. The inputs and expected outputs are also given. This time, a new type of activation function is used, namely the Sigmoid function[^1]. This function is often used in machine learning, since it constrains the output between $0$ and $1$. The formula for this function can be found below.

[^1]:<https://en.wikipedia.org/wiki/Sigmoid_function>

$$ 
f(x) = \frac{1}{1-e^{-x}}
$$

$$
\displaylines{
\text{weight 1}=0.1\\
\text{weight 2}=0.2\\
\text{weight 3}=0.3\\
\text{weight 4}=0.4\\
\text{weight 5}=0.5\\
\text{weight 6}=0.6\\
\text{weight 7}=0.7\\
\text{weight 8}=0.8\\
}
$$

$$
\displaylines{
\text{input 1}=0.1\\
\text{input 2}=0.5\\
\text{expected output 1}=0.05\\
\text{expected output 4}=0.95\\
}
$$

In order to calculate the needed changes to our network weights, first calculate the output.

$$
\displaylines{
\text{output_hidden1(0.1, 0.5)}=f((0.1*0.1)+(0.5*0.3))=0.60108\\
\text{output_hidden2(0.1, 0.5)}=f((0.1*0.2)+(0.5*0.4))=0.61538\\
\text{output_1(0.60108, 0.61538)}=f((0.60108*0.5)+(0.61538*0.7))=0.73492\\
\text{output_2(0.60108, 0.61538)}=f((0.60108*0.6)+(0.61538*0.8))=0.77955\\
}
$$

For each output, the error from the expected value can be calculated. This is done by using the following Error function.

$$
\displaylines{
\text{total_error}=\sum \frac{1}{2}(\text{expected - output})^2=\frac{1}{2}(0.05−0.73492)^2+\frac{1}{2}(0.95−0.77955)^2=0.24908
}
$$