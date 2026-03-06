import math

def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """

    H = len(image)
    W = len(image[0])

    result = []

    for i in range(new_h):
        row = []

        src_y = 0 if new_h == 1 else i * (H - 1) / (new_h - 1)
        y0 = int(math.floor(src_y))
        y1 = min(y0 + 1, H - 1)
        dy = src_y - y0

        for j in range(new_w):

            src_x = 0 if new_w == 1 else j * (W - 1) / (new_w - 1)
            x0 = int(math.floor(src_x))
            x1 = min(x0 + 1, W - 1)
            dx = src_x - x0

            v00 = image[y0][x0]
            v10 = image[y1][x0]
            v01 = image[y0][x1]
            v11 = image[y1][x1]

            val = (
                v00 * (1 - dy) * (1 - dx) +
                v10 * dy * (1 - dx) +
                v01 * (1 - dy) * dx +
                v11 * dy * dx
            )

            row.append(float(val))

        result.append(row)

    return result