import numpy as np

def chi2_independence(C):
   
    
    C = np.array(C, dtype=float)

    row_totals = C.sum(axis=1)
    col_totals = C.sum(axis=0)
    total = C.sum()

    
    expected = np.outer(row_totals, col_totals) / total

  
    chi2 = np.sum((C - expected) ** 2 / expected)

    return float(chi2), expected