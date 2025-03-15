import numpy as np

inputs = [1, 2, 3]
weights = [0.2,0.8,-0.5]
bias = 1
outputs = np.dot(weights, inputs) + bias
print(outputs)

inputs = [1,2,4,2.5]

weights = [[0.1,0.8,-0.5,1.1],
           [0.5,-0.1,0.6,-0.5],
           [-0.46,-0.27,0.17,0.8]]
bias = [1,2,0.5]

layer_out = np.dot(weights, inputs) + bias
print(layer_out)

inputs = [[1,2,4,2.5],[1,0,0,1],[1,3,8,6]]
weights = [[0.1,0.8,-0.5,1.1],
           [0.5,-0.1,0.6,-0.5],
           [-0.46,-0.27,0.17,0.8]]
bias = [1,2,0.5]
layer_out = np.dot(inputs, np.array(weights).T) + bias
print(layer_out)

print(inputs)
transpose_inputs = np.array(inputs).T
print(transpose_inputs)


#adding that "hidden" layer
weights2 = [[.11,.18,-0.15],[.5,-0.7,0.9],[-0.4,-0.7,.19]]
bias2 = [-1,2,.2]

layer1_out = np.dot(inputs, np.array(weights).T) + bias #this is a repeat from above    
layer2_out = np.dot(layer1_out, np.array(weights2).T) + bias2
print(layer2_out)