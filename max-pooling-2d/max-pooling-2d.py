import numpy as np

def max_pooling_2d(X, pool_size):
    X = np.array(X)
    H, W = X.shape
    
    p = pool_size
    
    H_out = H // p
    W_out = W // p
    
    out = np.zeros((H_out, W_out))
    
    for i in range(H_out):
        for j in range(W_out):
            window = X[i*p:(i+1)*p, j*p:(j+1)*p]
            out[i, j] = np.max(window)
    
    return out.tolist()