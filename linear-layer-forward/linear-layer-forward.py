def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    n_samples = len(X)
    d_out = len(W[0])

    # Initialize output
    Y = []

    for i in range(n_samples):
        row = []
        for j in range(d_out):
            val = 0
            for k in range(len(W)):  # d_in
                val += X[i][k] * W[k][j]
            val += b[j]
            row.append(val)
        Y.append(row)

    return Y