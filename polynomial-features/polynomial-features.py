import numpy as np

def polynomial_features(values, degree):
    values = np.array(values, dtype = float)
    features = []
    
    for x in values:
        row = []
        for d in range( degree + 1):
            row.append(x**d)
        features.append(row)

    return features