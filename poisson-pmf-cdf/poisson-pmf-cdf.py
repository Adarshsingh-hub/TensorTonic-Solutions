import numpy as np
from scipy.special import gammaln

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF using stable log computations.
    """
    # PMF using log-space
    log_pmf = -lam + k * np.log(lam) - gammaln(k + 1)
    pmf = np.exp(log_pmf)

    # CDF: sum of PMFs from 0 to k (vectorized, no factorial loops)
    i = np.arange(0, k + 1)
    log_terms = -lam + i * np.log(lam) - gammaln(i + 1)
    cdf = np.sum(np.exp(log_terms))

    return float(pmf), float(cdf)