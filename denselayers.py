from  sklearn.datasets import make_classification
import numpy as np
import matplotlib.pyplot as plt

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

# Generate dataset
x, y = make_classification(n_samples=1000,
                            n_features=2,
                            n_informative=2,
                            n_redundant=0,
                            n_clusters_per_class=1,
                            class_sep=0.8,
                            random_state=42)

# Creae Dense Layer with 2 input features and 3 output neurons
dense1 = Layer_Dense(2, 3)

# Perform a forward pass of the training data through this layer
dense1.forward(x)

#print the output of the first five samples
print(dense1.output[:5])

#plot the spiral dataset
# plt.scatter(x[:,0], x[:, 1], c=y)
# plt.xlabel('Feaature 1')
# plt.ylabel('Feature 2')
# plt.title('Spiral Dataset')
# plt.show()