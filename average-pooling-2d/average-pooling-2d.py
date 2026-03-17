def average_pooling_2d(X, pool_size):
    H = len(X)
    W = len(X[0])

    H_out = H//pool_size
    W_out = W//pool_size

    output = [[0.0 for _ in range(W_out)] for _ in range(H_out)]

    for i in range(H_out):
        for j in range(W_out):
            total = 0.0

            for a in range(pool_size):
                for b in range(pool_size):
                    total += X[i * pool_size + a][j * pool_size + b]

            # Compute average
            output[i][j] = total / (pool_size * pool_size)

    return output