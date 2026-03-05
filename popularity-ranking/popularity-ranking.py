import numpy as np

def popularity_ranking(items, min_votes, global_mean):
    items = np.asarray(items, dtype=float)

    R = items[:, 0]  # ratings
    v = items[:, 1]  # vote counts

    m = float(min_votes)
    C = float(global_mean)

    WR = (v / (v + m)) * R + (m / (v + m)) * C

    return WR.tolist()