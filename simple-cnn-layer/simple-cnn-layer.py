import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    x = np.array(x, dtype=float)
    W = np.array(W, dtype=float)
    b = np.array(b, dtype=float)
    
    N, C_in, H, W_in = x.shape
    C_out, _, KH, KW = W.shape
    
    # Output dimensions
    H_out = H - KH + 1
    W_out = W_in - KW + 1
    
    # Output tensor
    y = np.zeros((N, C_out, H_out, W_out))
    
    # Convolution
    for n in range(N):
        for c_out in range(C_out):
            for i in range(H_out):
                for j in range(W_out):
                    
                    # Extract patch
                    patch = x[n, :, i:i+KH, j:j+KW]
                    
                    # Element-wise multiply + sum + bias
                    y[n, c_out, i, j] = np.sum(patch * W[c_out]) + b[c_out]
    
    return y