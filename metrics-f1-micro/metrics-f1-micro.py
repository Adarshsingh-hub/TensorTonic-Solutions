def f1_micro(y_true, y_pred) -> float:
    if len(y_true) == 0:
        return 0.0
    
    tp = 0
    n = len(y_true)
    
    for yt, yp in zip(y_true, y_pred):
        if yt == yp:
            tp += 1
    
    return tp / n