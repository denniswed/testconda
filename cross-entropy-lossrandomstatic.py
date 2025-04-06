import math

# An example output from the output layer of the neural network

softmax_output = [0.5, 0.02, 0.3]

# Ground Truth
target_output = [1, 0, 1]

loss = -(math.log(softmax_output[0])*target_output[0] +
        math.log(softmax_output[1])*target_output[1] +
        math.log(softmax_output[2])*target_output[2])

print("Cross-Entropy Loss:", loss)