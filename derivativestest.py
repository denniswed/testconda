import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the complex function
def complex_function(x, y):
    return np.sin(x) + np.cos(y)

# Define the partial derivatives (gradients) of the complex function
def partial_derivative_x(x, y):
    return np.cos(x)

def partial_derivative_y(x, y):
    return -np.sin(y)

# Define the range of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# create a grid of x and y values
X, Y = np.meshgrid(x, y)

# Calculate the Z values for the complex function
Z = complex_function(X, Y)

# find the lowest point using the partial derivatives
lowest_point_indicies = np.unravel_index(np.argmin(Z), Z.shape)
lowest_point_x = X[lowest_point_indicies]
lowest_point_y = Y[lowest_point_indicies]
lowest_point_z = Z[lowest_point_indicies]

# Plot the complex function and the lowest point in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.scatter(lowest_point_x, lowest_point_y, lowest_point_z, color='red', s=50, label='Lowest Point')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Complex Function and its Lowest Point')
ax.legend()
plt.show()