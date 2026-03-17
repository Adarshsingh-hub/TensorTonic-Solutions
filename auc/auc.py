import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    fpr = np.array(fpr)
    tpr = np.array(tpr)

    # Compute differences in FPR (widths)
    delta_fpr = fpr[1:] - fpr[:-1]

    # Compute average heights (TPR)
    avg_tpr = (tpr[1:] + tpr[:-1]) / 2.0

    # Trapezoidal sum
    area = np.sum(delta_fpr * avg_tpr)

    return float(area)