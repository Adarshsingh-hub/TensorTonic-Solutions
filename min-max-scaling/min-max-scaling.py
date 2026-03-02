import numpy as np

def min_max_scaling(X):
    try:
        X = np.asarray(X, dtype=float)

        # Validate
        if X.size == 0 or X.ndim > 2:
            return None

        # If 1D → treat as single column
        if X.ndim == 1:
            xmin = np.min(X)
            xmax = np.max(X)
            if xmax == xmin:
                return np.zeros_like(X, dtype=float).tolist()
            return ((X - xmin) / (xmax - xmin)).tolist()

        # 2D case → column-wise scaling
        xmin = np.min(X, axis=0, keepdims=True)
        xmax = np.max(X, axis=0, keepdims=True)

        # Avoid division by zero (constant columns)
        denom = xmax - xmin
        denom = np.where(denom == 0, 1.0, denom)

        X_scaled = (X - xmin) / denom

        return X_scaled.tolist()

    except Exception:
        return None