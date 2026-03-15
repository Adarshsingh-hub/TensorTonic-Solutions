import numpy as np

def epsilon_greedy(q_values, epsilon, rng=None):
    """
    Returns: action index (int)
    """

    q_values = np.asarray(q_values)

    if rng is None:
        rng = np.random

    n_actions = len(q_values)

    
    if rng.random() < epsilon:
        action = rng.integers(n_actions) if hasattr(rng, "integers") else rng.randint(n_actions)
    else:
        
        action = int(np.argmax(q_values))

    return int(action)