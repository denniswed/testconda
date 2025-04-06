import numpy as np
from sklearn.datasets import make_classification

#cross-entropy loss function
class Loss_CategoricalCrossentropy:
    # Forward pass
    def forward(self, y_pred, y_true):
        # number of samples in batch
        samples = len(y_pred)
        # Clip data to prevent division by 0
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
        # Probabbilities for target values
        if (len(y_true.shape) == 1):
            correct_confidences = y_pred_clipped[range(samples), y_true]
        # Mask values for one-hot encoded labels
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
        # Losses
        negative_log_likelihoods = -np.log(correct_confidences)
        return negative_log_likelihoods
    
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
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True)) # for numerical stability
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True) # Normalize for each sample
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
x, y = make_classification(
    n_samples=10000000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    class_sep=0.8,
    random_state=42
    )

# Create Dense Layer with 2 input features and 3 output neurons
dense1 = Layer_Dense(2, 3)

# Apply ReLU activation function to input data
relu_activation = Activation_ReLU()
dense1_relu_output = relu_activation.forward(dense1.forward(x))

# Apply Softmax activation function to input data
softmax_activation = Activation_Softmax()
dense1_softmax_output = softmax_activation.forward(dense1_relu_output)

# Create loss instance
loss = Loss_CategoricalCrossentropy()

# Calculate loss
loss_value = np.mean(loss.forward(dense1_softmax_output, y))

# print the loss value
print("Cross-Entropy Loss:", loss_value)
