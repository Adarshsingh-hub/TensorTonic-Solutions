import numpy as np

def user_based_cf_prediction(similarities, ratings):
    
    similarities = np.array(similarities)
    ratings = np.array(ratings)
    
    mask = similarities > 0
    
    sims = similarities[mask]
    rats = ratings[mask]
    
    if len(sims) == 0:
        return 0.0
    
    denominator = np.sum(sims)
    
    if denominator == 0:
        return 0.0
    
    numerator = np.sum(sims * rats)
    
    return float(numerator / denominator)