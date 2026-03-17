import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x, dtype=float)
    p = np.array(p, dtype=float)
    
    # Validate inputs
    if x.shape != p.shape:
        raise ValueError("x and p must have the same shape")
    
    # Optional: ensure probabilities sum to 1 (useful for interviews)
    if not np.isclose(p.sum(), 1):
        raise ValueError("Probabilities must sum to 1")
    
    # Expected value = sum(x * p)
    return float(np.sum(x * p))