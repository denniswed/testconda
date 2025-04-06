import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# ReLU activation function
class Activation_ReLU:
    # Forward pass
    def forward(self, inputs):
        # Apply ReLU function: replace negative values with 0
        self.output = np.maximum(0, inputs)
        return self.output

# Softmax activation function
class Activation_Softmax:
    # Forward pass
    def forward(self, inputs):
        # Apply softmax function to normalize the inputs into probabilities
            # Subtracting the maximum value for numerical stability
        exp_values = np.exp(inputs - np.max(inputs))
        # Normalize them for each sample
        probabilities = exp_values / np.sum(exp_values)
        self.output = probabilities
        return self.output

# Dense Layer
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        """
        Initialize the Layer_Dense class with given number of input and output neurons.
        Initialize the weights with random values and biases with zeros.
        """
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        """
        Perform a forward pass through the layer by multiplying the inputs with the weights, adding the biases, and storing the result
        in the <output> attribute.
        """
        self.output = np.dot(inputs, self.weights) + self.biases
        return self.output

# Generate dataset
x, y = make_classification(n_samples=1000000,
                            n_features=2,
                            n_informative=2,
                            n_redundant=0,
                            n_clusters_per_class=1,
                            class_sep=0.8,
                            random_state=42)

# Create Dense Layer with 2 input features and 3 output neurons
dense1 = Layer_Dense(2, 3)

# Apply ReLI activation function to input data
relu_activation = Activation_ReLU()
dense1_relu_output = relu_activation.forward(dense1.forward(x))

# Apply Softmax activation function to input data
softmax_activation = Activation_Softmax()
dense1_softmax_output = softmax_activation.forward(dense1_relu_output)

# Print the first five samples
print(dense1_softmax_output[:5])

# Plotting the outputs
# plt.figure(figsize=(12,6))
# plt.subplot(1, 2, 1)
# plt.plot(x, y, label='Input')
# plt.plot(x, dense1_relu_output, label='ReLU Output')
# plt.legend()
# plt.title('ReLU Activation Function')

# plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Input')
# plt.plot(x, dense1_softmax_output, label='Softmax Output')
# plt.legend()
# plt.title('Softmax Activation Function')

# plt.show()