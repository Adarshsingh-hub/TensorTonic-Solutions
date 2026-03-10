import numpy as np

def mean_average_precision(y_true_list, y_score_list, k=None):
    
    ap_list = []

    for y_true, y_score in zip(y_true_list, y_score_list):
        y_true = np.array(y_true)
        y_score = np.array(y_score)

        
        R = np.sum(y_true)

        if R == 0:
            ap_list.append(0.0)
            continue

        
        order = np.argsort(-y_score)
        y_true_sorted = y_true[order]

        
        if k is not None:
            y_true_sorted = y_true_sorted[:k]

        cumsum = np.cumsum(y_true_sorted)
        ranks = np.arange(1, len(y_true_sorted) + 1)

        precision = cumsum / ranks

        ap = np.sum(precision * y_true_sorted) / R

        ap_list.append(float(ap))

    map_value = float(np.mean(ap_list)) if ap_list else 0.0

    return map_value, ap_list