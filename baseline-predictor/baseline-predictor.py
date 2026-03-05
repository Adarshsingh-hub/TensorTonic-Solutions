import numpy as np

def baseline_predict(ratings_matrix, target_pairs):
    R = np.array(ratings_matrix, dtype=float)

    # global mean (ignore zeros)
    nonzero = R[R != 0]
    mu = np.mean(nonzero)

    # user means ignoring zeros
    user_bias = []
    for row in R:
        vals = row[row != 0]
        if len(vals) > 0:
            user_bias.append(np.mean(vals) - mu)
        else:
            user_bias.append(0.0)

    # item means ignoring zeros
    item_bias = []
    for col in R.T:
        vals = col[col != 0]
        if len(vals) > 0:
            item_bias.append(np.mean(vals) - mu)
        else:
            item_bias.append(0.0)

    # predictions
    preds = []
    for u, i in target_pairs:
        preds.append(mu + user_bias[u] + item_bias[i])

    return preds