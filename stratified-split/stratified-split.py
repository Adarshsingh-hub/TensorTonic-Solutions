import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    X = np.asarray(X)
    y = np.asarray(y)

    if rng is None:
        rng = np.random.default_rng(42)

    train_idx = []
    test_idx = []

    classes = np.unique(y)

    for c in classes:
        idx = np.where(y == c)[0]
        idx = rng.permutation(idx)

        n = len(idx)
        n_test = int(round(n * test_size))

        if n_test >= n and n > 1:
            n_test = n - 1

        test_idx.extend(idx[:n_test])
        train_idx.extend(idx[n_test:])

    train_idx = np.sort(np.array(train_idx, dtype=int))
    test_idx = np.sort(np.array(test_idx, dtype=int))

    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]