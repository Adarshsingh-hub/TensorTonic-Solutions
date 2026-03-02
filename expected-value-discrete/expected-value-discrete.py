import numpy as np

def expected_value_discrete(values, probs):
    values = np.asarray(values, dtype=float)
    probs = np.asarray(probs, dtype=float)

    if values.size == 0 or probs.size == 0 or values.shape != probs.shape:
        return None

    if np.any(probs < 0) or not np.isclose(np.sum(probs), 1.0):
        raise ValueError("Invalid probability distribution")

    ev = np.sum(values * probs)

    return float(ev)