import numpy as np

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    """

    y = np.asarray(y)
    split_mask = np.asarray(split_mask)

    def entropy(labels):
        if labels.size == 0:
            return 0.0
        _, counts = np.unique(labels, return_counts=True)
        p = counts / counts.sum()
        return float(-(p * np.log2(p)).sum())

    # Parent entropy
    H_parent = entropy(y)

    # Split
    y_left = y[split_mask]
    y_right = y[~split_mask]

    n = y.size
    n_left = y_left.size
    n_right = y_right.size

    # If one side empty → IG = 0
    if n_left == 0 or n_right == 0:
        return 0.0

    # Child entropies
    H_left = entropy(y_left)
    H_right = entropy(y_right)

    # Weighted entropy
    weighted_entropy = (n_left / n) * H_left + (n_right / n) * H_right

    # Information Gain
    return float(H_parent - weighted_entropy)