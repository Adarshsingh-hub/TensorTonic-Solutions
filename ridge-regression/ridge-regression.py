import numpy as np

def ridge_regression(X, y, lam):
    try:
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)
        lam = float(lam)

        # Validate inputs
        if X.ndim != 2:
            return None
        if y.ndim not in (1, 2):
            return None
        if X.shape[0] != y.shape[0]:
            return None
        if lam < 0:
            return None

        n_features = X.shape[1]

        # Identity matrix
        I = np.eye(n_features)

        # Closed-form ridge solution
        XtX = X.T @ X
        A = XtX + lam * I

        # Solve linear system instead of explicit inverse (more stable)
        w = np.linalg.solve(A, X.T @ y)

        # Ensure output shape (flatten to 1D if single target)
        if w.ndim == 2 and w.shape[1] == 1:
            w = w.reshape(-1)

        return w.tolist()

    except Exception:
        return None