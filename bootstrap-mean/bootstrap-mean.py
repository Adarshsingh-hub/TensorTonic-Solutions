import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    x = np.asarray(x)
    n = len(x)
    if rng is None:
        rng = np.random.default_rng()
    indices = rng.integers(0, n, size=(n_bootstrap, n))

    samples = x[indices]
    boot_means = samples.mean(axis=1)
    alpha = 1 - ci
    lower = np.quantile(boot_means, alpha / 2)
    upper = np.quantile(boot_means, 1 - alpha / 2)
    
    return boot_means, lower, upper