import numpy as np

def entropy_node(labels):
    labels = np.asarray(labels, dtype=int)

    counts = np.bincount(labels)

    probs = counts[counts > 0] / len(labels)

    entropy = -np.sum(probs * np.log2(probs))

    return float(entropy)