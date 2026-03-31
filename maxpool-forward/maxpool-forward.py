import numpy as np

def maxpool_forward(X, pool_size, stride):
    X = np.array(X)
    H, W = X.shape
    
    p = pool_size
    s = stride
    H_out = (H - p) // s + 1
    W_out = (W - p) // s + 1
    out = np.zeros((H_out, W_out))
    
    for i in range(H_out):
        for j in range(W_out):
            window = X[i*s:i*s+p, j*s:j*s+p]
            out[i, j] = np.max(window)
    
    return out.tolist()