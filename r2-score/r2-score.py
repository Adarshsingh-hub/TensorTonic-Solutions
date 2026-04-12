import numpy as np

def r2_score(y_true, y_pred) -> float:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)

    if np.all(y_true == y_true[0]):
        return 1.0 if np.allclose(y_true, y_pred) else 0.0

    y_mean = np.mean(y_true)

    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_mean) ** 2)

    return float(1 - (ss_res / ss_tot))