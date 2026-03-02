import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    try:
        X = np.asarray(X, dtype=float)

        # Validate
        if X.size == 0 or X.ndim > 2:
            return None

        # If 1D → treat as vector
        if X.ndim == 1:
            xmin = np.min(X)
            xmax = np.max(X)
            denom = (xmax - xmin)
            denom = denom if denom > eps else eps
            return (X - xmin) / denom

        # 2D case
        xmin = np.min(X, axis=axis, keepdims=True)
        xmax = np.max(X, axis=axis, keepdims=True)

        denom = xmax - xmin
        denom = np.where(denom < eps, eps, denom)

        X_scaled = (X - xmin) / denom

        return X_scaled

    except Exception:
        return None