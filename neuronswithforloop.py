import random

inputs = [1,2,4,2.5]

weights = [[0.1,0.8,-0.5,1.1],
           [0.5,-0.1,0.6,-0.5],
           [-0.46,-0.27,0.17,0.8]]
bias = [1,2,0.5]

for i in range(1, 101):
    inputs.append(round(random.uniform(-1, 1), 2))
    new_weights = [round(random.uniform(-1, 1), 2) for _ in range(i)]
    weights.append(new_weights)
    bias.append(round(random.uniform(-1, 1), 2))


#Output of current layer
layer_out=[]
#for each neuron
for neuron_weights, neuron_bias in zip(weights, bias):
    # zeroed output of given neuron
    neuron_out = 0
    #for each input and wieght to the neuron
    for input, weight in zip(inputs, neuron_weights):
        #multiply input by weight and add to output
        neuron_out += input * weight
    #add bias to output
    neuron_out += neuron_bias
    #putting neuron's result in the layer's output list
    layer_out.append(neuron_out)
    print(layer_out)
print(layer_out[-1])