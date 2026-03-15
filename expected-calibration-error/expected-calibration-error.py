import numpy as np

def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    n = len(y_true)
    bin_counts = np.zeros(n_bins)
    bin_conf = np.zeros(n_bins)
    bin_acc = np.zeros(n_bins)

    # Assign predictions to bins
    for y, p in zip(y_true, y_pred):
        if p == 1.0:
            b = n_bins - 1
        else:
            b = int(p * n_bins)

        bin_counts[b] += 1
        bin_conf[b] += p
        bin_acc[b] += y

    ece = 0.0

    for b in range(n_bins):
        if bin_counts[b] > 0:
            acc = bin_acc[b] / bin_counts[b]
            conf = bin_conf[b] / bin_counts[b]
            weight = bin_counts[b] / n

            ece += weight * abs(acc - conf)

    return float(ece)