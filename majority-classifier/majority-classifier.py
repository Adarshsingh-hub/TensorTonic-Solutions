import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Edge case: empty test set
    if len(X_test) == 0:
        return np.array([], dtype=int)
    
    # Count frequencies (preserve first occurrence order)
    freq = {}
    for y in y_train:
        if y not in freq:
            freq[y] = 0
        freq[y] += 1

    # Find majority with tie-breaking (first occurrence wins)
    max_count = -1
    majority = None
    for y in y_train:
        if freq[y] > max_count:
            max_count = freq[y]
            majority = y

    # Predict for all test samples
    return np.full(len(X_test), majority, dtype=int)