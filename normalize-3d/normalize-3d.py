import numpy as np

def normalize_3d(v):
    v = np.array(v, dtype=float)

    # If input is a single vector
    if v.ndim == 1:
        norm = np.linalg.norm(v)
        if norm == 0:
            return v
        return v / norm

    # If input is a matrix
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    norms[norms == 0] = 1   # avoid division by zero
    return v / norms