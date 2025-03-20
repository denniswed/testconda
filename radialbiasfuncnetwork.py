import numpy as np

def rbf_gaussian(x, z, gamma):
    """
    Calculates the Radial Basis Function (RBF) with a Gaussian kernel.
    Parameters:
    x, z: numpy array of the same length representing two points in n-dimensional space
    gamma: a parameter of the RBF (must be greater than 0)
    
    Returns:
    The result of the RBF calculation
    """
    distance = np.linalg.norm(x-z)**2
    return np.exp(-gamma * distance)

# example usage
x = np.array([1, 2, 3])
z = np.array([4, 5, 6])
gamma = 0.1

print(rbf_gaussian(x, z, gamma))  
