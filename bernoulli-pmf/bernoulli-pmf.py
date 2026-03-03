import numpy as np

def bernoulli_pmf_and_moments(x, p):
    x = np.array(x, dtype = float)
    p = float(p)

    pmf = np.where(x == 1, p,
          np.where(x == 0, 1 - p, 0))

    mean = p
    var = p * (1-p)

    return (pmf, mean,var)