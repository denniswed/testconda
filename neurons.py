inputs = [1,2,4,2.5]
weights1 = [0.1,0.8,-0.5,1.1]
weights2 = [0.5,-0.1,0.6,-0.5]
weights3 = [-0.46,-0.27,0.17,0.8]
bias1 = 1
bias2 = 2
bias3 = 0.5

outputs = [
    #neuron1
    sum([inputs[i] * weights1[i] for i in range(len(inputs))]) + bias1,
    #neuron2
    sum([inputs[i] * weights2[i] for i in range(len(inputs))]) + bias2,
    #neuron3
    sum([inputs[i] * weights3[i] for i in range(len(inputs))]) + bias3
]
print(outputs)