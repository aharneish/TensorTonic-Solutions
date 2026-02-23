import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x_new=np.asarray(x)
    return np.where(x_new >= 0, x_new, alpha * x_new)
    