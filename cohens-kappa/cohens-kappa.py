import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    r1 = np.array(rater1)
    r2 = np.array(rater2)
    
    n = len(r1)
    
    # Observed agreement
    p_o = np.sum(r1 == r2) / n
    
    # Get all unique labels
    labels = np.union1d(r1, r2)
    
    # Expected agreement
    p_e = 0
    for label in labels:
        p_r1 = np.sum(r1 == label) / n
        p_r2 = np.sum(r2 == label) / n
        p_e += p_r1 * p_r2
    
    # Handle degenerate case
    if p_e == 1:
        return 1.0
    
    # Cohen's Kappa
    kappa = (p_o - p_e) / (1 - p_e)
    
    return float(kappa)