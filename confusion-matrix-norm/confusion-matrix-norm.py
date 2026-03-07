import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    
    y_true = np.asarray(y_true, dtype=np.int64)
    y_pred = np.asarray(y_pred, dtype=np.int64)

    if num_classes is None:
        if y_true.size == 0 and y_pred.size == 0:
            K = 0
        else:
            K = int(max(y_true.max(), y_pred.max()) + 1)
    else:
        K = int(num_classes)

    # handle empty case properly
    if y_true.size == 0:
        cm = np.zeros((K, K), dtype=int)
    else:
        idx = y_true * K + y_pred
        cm = np.bincount(idx, minlength=K*K).reshape(K, K)

    if normalize == 'none':
        return cm

    cm = cm.astype(float)
    eps = 1e-12

    if normalize == 'true':
        cm /= (cm.sum(axis=1, keepdims=True) + eps)

    elif normalize == 'pred':
        cm /= (cm.sum(axis=0, keepdims=True) + eps)

    elif normalize == 'all':
        cm /= (cm.sum() + eps)

    else:
        raise ValueError("Invalid normalize mode")

    return cm