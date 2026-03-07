import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    

    indices = np.arange(N)

    
    if shuffle:
        if rng is not None:
            indices = rng.permutation(indices)
        else:
            np.random.shuffle(indices)

    fold_sizes = np.full(k, N // k, dtype=int)
    fold_sizes[:N % k] += 1

    splits = []
    current = 0

    for fold_size in fold_sizes:
        start, stop = current, current + fold_size
        val_idx = indices[start:stop]

        train_idx = np.concatenate((indices[:start], indices[stop:]))

        splits.append((train_idx.astype(int), val_idx.astype(int)))

        current = stop

    return splits