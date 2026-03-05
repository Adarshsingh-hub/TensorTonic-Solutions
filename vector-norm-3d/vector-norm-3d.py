import numpy as np

def vector_norm_3d(v):
    v = np.asarray(v, dtype=float)

    if v.ndim == 1:  # single vector (3,)
        return np.sqrt(np.sum(v**2))
    else:  # batch (N,3)
        return np.sqrt(np.sum(v**2, axis=1))