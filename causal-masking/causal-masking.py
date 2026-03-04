import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    scores = np.array(scores, dtype = float)

    T = scores.shape[-1]

    mask = np.triu(np.ones((T,T)), k = 1).astype(bool)

    scores[..., mask] = mask_value

    return scores