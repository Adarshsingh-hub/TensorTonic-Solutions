def conv2d(image, kernel, stride=1, padding=0):
    """
    Apply 2D convolution to a single-channel image.
    """

    H = len(image)
    W = len(image[0])
    kh = len(kernel)
    kw = len(kernel[0])

    # Step 1: pad image
    padded = [[0]*(W + 2*padding) for _ in range(H + 2*padding)]

    for i in range(H):
        for j in range(W):
            padded[i + padding][j + padding] = image[i][j]

    # Step 2: output size
    H_out = ((H + 2*padding - kh) // stride) + 1
    W_out = ((W + 2*padding - kw) // stride) + 1

    output = [[0.0 for _ in range(W_out)] for _ in range(H_out)]

    # Step 3: convolution
    for i in range(H_out):
        for j in range(W_out):

            val = 0.0

            for m in range(kh):
                for n in range(kw):
                    val += padded[i*stride + m][j*stride + n] * kernel[m][n]

            output[i][j] = float(val)

    return output