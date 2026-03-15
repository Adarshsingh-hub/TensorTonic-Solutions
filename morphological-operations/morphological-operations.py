def morphological_op(image, kernel, operation):
    """
    Apply morphological erosion or dilation to a binary image.
    """

    H = len(image)
    W = len(image[0])

    kh = len(kernel)
    kw = len(kernel[0])

    pad_h = kh // 2
    pad_w = kw // 2

    # zero padding
    padded = [[0]*(W + 2*pad_w) for _ in range(H + 2*pad_h)]

    for i in range(H):
        for j in range(W):
            padded[i + pad_h][j + pad_w] = image[i][j]

    output = [[0]*W for _ in range(H)]

    for i in range(H):
        for j in range(W):

            if operation == "erode":
                val = 1
                for m in range(kh):
                    for n in range(kw):
                        if kernel[m][n] == 1:
                            if padded[i + m][j + n] != 1:
                                val = 0
                                break
                    if val == 0:
                        break
                output[i][j] = val

            elif operation == "dilate":
                val = 0
                for m in range(kh):
                    for n in range(kw):
                        if kernel[m][n] == 1 and padded[i + m][j + n] == 1:
                            val = 1
                            break
                    if val == 1:
                        break
                output[i][j] = val

            else:
                raise ValueError("operation must be 'erode' or 'dilate'")

    return output