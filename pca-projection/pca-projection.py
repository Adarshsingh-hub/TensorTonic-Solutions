import numpy as np

def pca_projection(X, k):
    try:
        X = np.asarray(X, dtype=float)
        k = int(k)

        # Validate
        if X.ndim != 2 or X.size == 0:
            return None
        n, d = X.shape
        if k <= 0 or k > d or n < 2:
            return None
        mean = np.mean(X, axis=0, keepdims=True)
        Xc = X - mean

        # 2) Covariance matrix (d x d), sample covariance (n-1)
        C = (Xc.T @ Xc) / (n - 1)

        # 3) Eigen decomposition (symmetric matrix → eigh is stable)
        eigvals, eigvecs = np.linalg.eigh(C)

        # 4) Sort by descending eigenvalues and take top-k eigenvectors
        idx = np.argsort(eigvals)[::-1][:k]
        W = eigvecs[:, idx]  # (d x k)

        # 5) Project data
        X_proj = Xc @ W  # (n x k)

        return X_proj.tolist()

    except Exception:
        return None
    # Write code here