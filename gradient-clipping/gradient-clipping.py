import numpy as np

def clip_gradients(g, max_norm):
    g = np.array(g, dtype=float)
    if max_norm <= 0:
        return g

    norm = np.linalg.norm(g)

    if norm == 0 or norm <= max_norm:
        return g

    scale = max_norm / norm
    return g * scale