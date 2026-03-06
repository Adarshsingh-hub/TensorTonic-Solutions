import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    
    X = np.array(X)
    y = np.array(y)
    
    N = len(X)

    if rng is None:
        rng = np.random.default_rng()

    perm = rng.permutation(N)

    X_shuffled = X[perm]
    y_shuffled = y[perm]


    for i in range(0, N, batch_size):
        end = i + batch_size

        if end > N and drop_last:
            break

        yield X_shuffled[i:end], y_shuffled[i:end]