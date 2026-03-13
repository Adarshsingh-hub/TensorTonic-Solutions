import math

def compute_monitoring_metrics(system_type, y_true, y_pred):

    metrics = []

    if system_type == "classification":

        TP = TN = FP = FN = 0

        for yt, yp in zip(y_true, y_pred):
            if yt == 1 and yp == 1:
                TP += 1
            elif yt == 0 and yp == 0:
                TN += 1
            elif yt == 0 and yp == 1:
                FP += 1
            elif yt == 1 and yp == 0:
                FN += 1

        n = len(y_true)

        accuracy = (TP + TN) / n

        precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0

        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0

        metrics = [
            ("accuracy", accuracy),
            ("precision", precision),
            ("recall", recall),
            ("f1", f1)
        ]

    elif system_type == "regression":

        n = len(y_true)

        mae = sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / n
        rmse = math.sqrt(sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n)

        metrics = [
            ("mae", mae),
            ("rmse", rmse)
        ]

    elif system_type == "ranking":

        pairs = list(zip(y_true, y_pred))
        pairs.sort(key=lambda x: x[1], reverse=True)

        top3 = pairs[:3]

        relevant_top3 = sum(yt for yt, _ in top3)

        precision_at_3 = relevant_top3 / 3

        total_relevant = sum(y_true)
        recall_at_3 = relevant_top3 / total_relevant if total_relevant > 0 else 0.0

        metrics = [
            ("precision_at_3", precision_at_3),
            ("recall_at_3", recall_at_3)
        ]

    return sorted(metrics)