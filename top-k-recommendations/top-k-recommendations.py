def top_k_recommendations(scores, rated_indices, k):
    unrated = [(i, score) for i, score in enumerate(scores) if i not in rated_indices]
    unrated.sort(key=lambda x: x[1], reverse=True)
    top_items = unrated[:k]
    return [i for i, _ in top_items]