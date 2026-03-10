def jaccard_similarity(items_a, items_b):
    set_a = set(items_a)
    set_b = set(items_b)

    intersection = len(set_a & set_b)
    union = len(set_a | set_b)

    return intersection / union if union !=0 else 0.0