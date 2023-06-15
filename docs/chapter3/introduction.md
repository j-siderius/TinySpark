# Chapter 3 - Training networks

The network shown in the last chapter was still relatively simple. Tuning the weights was still handled manually and by intuition. However, if networks become larger, calculating the optimal weights for each neuron is impossible. Through the use of mathematics, it is possible to calculate the influence of every weight in the network, and determine how to optimally change all weights to get the required output.

A walkthrough and explanation of the mathematics will be introduced first, then the calculations will be programmed so they can be performed automatically. Lastly, a model for classifying gestures will be trained using Python and subsequently deployed to the TinySpark development kit.