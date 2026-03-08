import numpy as np

def dropout(x, p=0.5, rng=None):
    x = np.asarray(x, dtype=float)

    if rng is None:
        rand = np.random.random(x.shape)
    else:
        rand = rng.random(x.shape)

    keep = rand < (1 - p)            
    scale = 1.0 / (1.0 - p)

    dropout_pattern = keep.astype(float) * scale
    output = x * dropout_pattern

    return output, dropout_pattern