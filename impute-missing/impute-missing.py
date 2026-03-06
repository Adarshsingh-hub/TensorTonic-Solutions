import numpy as np

def impute_missing(X, strategy='mean'):
    
    
    X = np.array(X, dtype=float, copy=True)

    
    if X.ndim == 1:
        if strategy == 'mean':
            val = np.nanmean(X)
        else:
            val = np.nanmedian(X)

        if np.isnan(val):
            val = 0

        X[np.isnan(X)] = val
        return X

    
    if strategy == 'mean':
        stats = np.nanmean(X, axis=0)
    else:
        stats = np.nanmedian(X, axis=0)

    
    stats = np.where(np.isnan(stats), 0, stats)

    
    inds = np.where(np.isnan(X))

    
    X[inds] = stats[inds[1]]

    return X