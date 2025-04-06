import numpy as np

# Probabilities of 3 samples from the softmax output
softmax_outputs = np.array([
    [0.7, 0.2, 0.1],  # Sample 1: Class 0 has the highest probability
    [0.5, 0.1, 0.4],  # Sample 2: Class 1 has the highest probability
    [0.02, 0.9, 0.08]   # Sample 3: Class 2 has the highest probability
])

# Target (ground-truth) labels for the 3 samples
class_targets = np.array([[0, 1, 1]])

# Caclulate values along the second axis (axis of index 1)
predictions = np.argmax(softmax_outputs, axis=1)

# If Targets are one-hot encoded, convert them to class indices
if len(class_targets.shape) == 2:
    class_targets = np.argmax(class_targets, axis=1)

# True evaluates to 1, False evaluates to 0
accuracy = np.mean(predictions == class_targets)
print('Accuracy:', accuracy)

# Calculate accuracy from output of activation2 and targets
# Calcuate values along the first axis
activation2_output = np.array([[0.1, 0.2, 0.7],
                              [0.9, 0.1, 0.0],
                              [0.3, 0.4, 0.3]
                              ] )

y = np.array([[1, 0, 0],
              [0, 0, 1],
              [0, 1, 0]
              ])

predictions = np.argmax(activation2_output, axis=1)

if len(y.shape) == 2:
    y = np.argmax(y, axis=1)

accuracy = np.mean(predictions == y)
print('Accuracy from activation2 output:', accuracy)