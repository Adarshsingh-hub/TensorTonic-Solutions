import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """

    y_left = np.asarray(y_left)
    y_right = np.asarray(y_right)

    def gini(y):
        n = len(y)
        if n == 0:
            return 0.0
        
        _, counts = np.unique(y, return_counts=True)
        p = counts / n
        return 1.0 - np.sum(p ** 2)

    n_left = len(y_left)
    n_right = len(y_right)
    n_total = n_left + n_right

    if n_total == 0:
        return 0.0

    g_left = gini(y_left)
    g_right = gini(y_right)

    weighted_gini = (n_left / n_total) * g_left + (n_right / n_total) * g_right

    return float(weighted_gini)