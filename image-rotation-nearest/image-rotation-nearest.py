import math

def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """

    H = len(image)
    W = len(image[0])

    theta = math.radians(angle_degrees)
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)

    cy = (H - 1) / 2.0
    cx = (W - 1) / 2.0

    output = [[0 for _ in range(W)] for _ in range(H)]

    for i in range(H):
        for j in range(W):

            dy = i - cy
            dx = j - cx

            src_y = cy + dy * cos_t + dx * sin_t
            src_x = cx - dy * sin_t + dx * cos_t

            src_y = int(round(src_y))
            src_x = int(round(src_x))

            if 0 <= src_y < H and 0 <= src_x < W:
                output[i][j] = image[src_y][src_x]
            else:
                output[i][j] = 0

    return output