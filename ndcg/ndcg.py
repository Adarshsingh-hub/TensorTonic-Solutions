import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Limit k to available items
    k = min(k, len(relevance_scores))
    
    # Compute DCG
    dcg = 0.0
    for i in range(k):
        rel = relevance_scores[i]
        dcg += (2**rel - 1) / math.log2(i + 2)  # i+2 because index starts at 0
    
    # Compute IDCG (ideal ranking)
    sorted_rels = sorted(relevance_scores, reverse=True)
    
    idcg = 0.0
    for i in range(k):
        rel = sorted_rels[i]
        idcg += (2**rel - 1) / math.log2(i + 2)
    
    # Handle edge case
    if idcg == 0:
        return 0.0
    
    return dcg / idcg