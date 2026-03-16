import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """

    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)

    # ensure 2D
    if X_train.ndim == 1:
        X_train = X_train.reshape(-1, 1)
    if X_test.ndim == 1:
        X_test = X_test.reshape(-1, 1)

    n_train = X_train.shape[0]
    n_test = X_test.shape[0]

    # compute pairwise distances using broadcasting
    diff = X_test[:, None, :] - X_train[None, :, :]
    distances = np.sqrt(np.sum(diff ** 2, axis=2))

    # sort indices by distance
    sorted_idx = np.argsort(distances, axis=1)

    # handle k > n_train
    k_eff = min(k, n_train)
    neighbors = sorted_idx[:, :k_eff]

    if k > n_train:
        pad = np.full((n_test, k - n_train), -1, dtype=int)
        neighbors = np.concatenate([neighbors, pad], axis=1)

    return neighbors.astype(int)