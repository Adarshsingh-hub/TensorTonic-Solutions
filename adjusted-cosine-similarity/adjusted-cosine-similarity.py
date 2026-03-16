import numpy as np

def adjusted_cosine_similarity(ratings_matrix, item_i, item_j):
    """
    Compute adjusted cosine similarity between two items.
    """

    R = np.array(ratings_matrix, dtype=float)

    # compute user means ignoring zeros
    user_means = []
    for row in R:
        rated = row[row != 0]
        if len(rated) == 0:
            user_means.append(0.0)
        else:
            user_means.append(np.mean(rated))
    user_means = np.array(user_means)

    numerator = 0.0
    denom_i = 0.0
    denom_j = 0.0

    for u in range(R.shape[0]):
        r_ui = R[u, item_i]
        r_uj = R[u, item_j]

        # only users who rated both
        if r_ui != 0 and r_uj != 0:
            diff_i = r_ui - user_means[u]
            diff_j = r_uj - user_means[u]

            numerator += diff_i * diff_j
            denom_i += diff_i ** 2
            denom_j += diff_j ** 2

    denom = np.sqrt(denom_i) * np.sqrt(denom_j)

    if denom == 0:
        return 0.0

    return numerator / denom