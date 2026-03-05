import numpy as np

def priority_replay_sample(priorities, alpha, beta):
    priorities = np.asarray(priorities, dtype=float)

    # Step 1: powered priorities
    p_alpha = priorities ** alpha

    # Step 2: probabilities
    probs = p_alpha / np.sum(p_alpha)

    # Step 3: importance weights
    N = len(priorities)
    weights = (N * probs) ** (-beta)

    # Step 4: normalize
    weights = weights / np.max(weights)

    return [probs.tolist(), weights.tolist()]