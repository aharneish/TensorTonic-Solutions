def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    return [[v ** d for d in range(0, degree + 1)] for v in values]