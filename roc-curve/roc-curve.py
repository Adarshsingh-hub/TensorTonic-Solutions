import numpy as np

def roc_curve(y_true, y_score):
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    # thresholds: start with +inf so ROC starts at (0,0)
    thresholds = np.r_[np.inf, np.sort(np.unique(y_score))[::-1]]

    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    tpr = []
    fpr = []

    for thresh in thresholds:
        y_pred = y_score >= thresh

        TP = np.sum((y_pred == 1) & (y_true == 1))
        FP = np.sum((y_pred == 1) & (y_true == 0))

        TPR = TP / P if P > 0 else 0
        FPR = FP / N if N > 0 else 0

        tpr.append(TPR)
        fpr.append(FPR)

    return np.array(fpr), np.array(tpr), thresholds