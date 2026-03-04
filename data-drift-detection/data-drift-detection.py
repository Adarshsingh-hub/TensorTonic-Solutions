import numpy as np

def detect_drift(ref_counts, prod_counts, threshold):
    ref = np.array(ref_counts, dtype=float)
    prod = np.array(prod_counts, dtype=float)

    # normalize
    p = ref / np.sum(ref)
    q = prod / np.sum(prod)

    # compute TVD
    tvd = 0.5 * np.sum(np.abs(p - q))

    return {
        "score": float(tvd),
        "drift_detected": bool(tvd > threshold)
    }