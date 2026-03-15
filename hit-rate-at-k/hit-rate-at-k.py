def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    if len(recommendations) == 0:
        return 0.0

    hits = 0
    total_users = len(recommendations)

    for recs, truth in zip(recommendations, ground_truth):
        top_k = recs[:k]
        if any(item in top_k for item in truth):
            hits += 1

    return hits / total_users