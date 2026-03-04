import numpy as np

def t_test_one_sample(x, mu0):
    x = np.array(x, dtype = float)
    n = len(x)

    x_mean =np.mean(x)
    s = np.std(x, ddof=1)
    t = (x_mean - mu0)/ (s/np.sqrt(n))

    return t
    