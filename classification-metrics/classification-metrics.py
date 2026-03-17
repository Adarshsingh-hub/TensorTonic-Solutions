import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    accuracy = np.mean(y_true == y_pred)

    classes = np.unique(np.concatenate([y_true, y_pred]))

    tp, fp, fn, support = {}, {}, {}, {}

    for c in classes:
        tp[c] = np.sum((y_true == c) & (y_pred == c))
        fp[c] = np.sum((y_true != c) & (y_pred == c))
        fn[c] = np.sum((y_true == c) & (y_pred != c))
        support[c] = np.sum(y_true == c)

    def safe_div(a, b):
        return a / b if b != 0 else 0.0


    if average == "micro":
        TP = sum(tp.values())
        FP = sum(fp.values())
        FN = sum(fn.values())

        precision = safe_div(TP, TP + FP)
        recall = safe_div(TP, TP + FN)
        f1 = safe_div(2 * precision * recall, precision + recall)

  
    elif average == "macro":
        precisions, recalls, f1s = [], [], []

        for c in classes:
            p = safe_div(tp[c], tp[c] + fp[c])
            r = safe_div(tp[c], tp[c] + fn[c])
            f = safe_div(2 * p * r, p + r)

            precisions.append(p)
            recalls.append(r)
            f1s.append(f)

        precision = np.mean(precisions)
        recall = np.mean(recalls)
        f1 = np.mean(f1s)

    elif average == "weighted":
        total = len(y_true)
        precision, recall, f1 = 0.0, 0.0, 0.0

        for c in classes:
            weight = support[c] / total

            p = safe_div(tp[c], tp[c] + fp[c])
            r = safe_div(tp[c], tp[c] + fn[c])
            f = safe_div(2 * p * r, p + r)

            precision += weight * p
            recall += weight * r
            f1 += weight * f
            
    elif average == "binary":
        c = pos_label

        TP = tp.get(c, 0)
        FP = fp.get(c, 0)
        FN = fn.get(c, 0)

        precision = safe_div(TP, TP + FP)
        recall = safe_div(TP, TP + FN)
        f1 = safe_div(2 * precision * recall, precision + recall)

    else:
        raise ValueError("Invalid average type")

    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1),
    }