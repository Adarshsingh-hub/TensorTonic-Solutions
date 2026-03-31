import numpy as np

def one_hot(y, num_classes=None):
    y = np.array(y, dtype=int)
    
    if num_classes is None:
        num_classes = np.max(y) + 1

    if np.any(y >= num_classes) or np.any(y < 0):
        raise ValueError("Labels out of range")
    
    N = y.shape[0]
    one_hot_matrix = np.zeros((N, num_classes), dtype=float)
    
    one_hot_matrix[np.arange(N), y] = 1.0
    
    return one_hot_matrix