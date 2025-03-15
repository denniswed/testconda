# sigmoid function python code
import numpy as np

def sigmoid(z):
    """
    Compute the sigmoid function for the input z.
    The sigmoid function is defined as 1 / (1 + exp(-z)).
    """
    return 1.0 / (1 + np.exp(-z))

# Derivative of the sigmoid function
def sigmoid_prime(z):
    """
    Compute the derivative of the sigmoid function for the input z.
    The derivative is defined as sigmoid(z) * (1 - sigmoid(z)).
    """
    return sigmoid(z) * (1 - sigmoid(z))

# Tanh activation function
def tanh(z):
    """
    Compute the hyperbolic tangent (tanh) activation function for the input z.
    The tanh function is defined as (exp(z) - exp(-z)) / (exp(z) + exp(-z)).
    """
    return (np.exp(z) - np.exp(-z)) / (np.exp(z) + np.exp(-z))

# Derivative of the tanh function
def tanh_prime(z):
    """
    Compute the derivative of the tanh function for the input z.
    The derivative is defined as 1 - tanh(z)^2.
    """
    return 1 - np.power(tanh(z), 2)

# ReLU activation function
def relu(z):
    """
    Compute the Rectified Linear Unit (ReLU) activation function for the input z.
    The ReLU function is defined as max(0, z).
    """
    return np.max(0, z)

def relu_prime(z):
    """
    Compute the derivative of the ReLU function for the input z.
    The derivative is defined as 1 if z > 0, else 0.
    """
    return 1 if z > 0 else 0

def leaky_relu(z):
    alpha=0.1
    return z if z > 0 else alpha * z

def leaky_relu_prime(z):
    alpha=0.1
    return 1 if z > 0 else alpha

def softmax(z):
    """
    Compute the softmax activation function for the input z.
    The softmax function is defined as exp(z) / sum(exp(z)).
    """
    exp_z = np.exp(z - np.max(z))  # Subtract max for numerical stability
    return exp_z / np.sum(exp_z)

def softmax_prime(z):
    """
    Compute the derivative of the softmax function for the input z.
    The derivative is defined as softmax(z) * (1 - softmax(z)).
    """
    s = softmax(z)
    return s * (1 - s)

def softmax_cross_entropy_loss(y_true, y_pred):
    """
    Compute the softmax cross-entropy loss between true labels and predicted labels.
    The loss is defined as -sum(y_true * log(y_pred)).
    """
    # Ensure numerical stability by clipping predictions
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
    # Compute the loss
    loss = -np.sum(y_true * np.log(y_pred)) / y_true.shape[0]
    return loss