import numpy as np

def rotate_around_z(points, theta):
    pts = np.array(points, dtype=float)

    single = False
    if pts.ndim == 1:
        pts = pts.reshape(1, 3)
        single = True

    cos_t = np.cos(theta)
    sin_t = np.sin(theta)

    x = pts[:, 0]
    y = pts[:, 1]
    z = pts[:, 2]

    x_new = x * cos_t - y * sin_t
    y_new = x * sin_t + y * cos_t

    rotated = np.stack([x_new, y_new, z], axis=1)
    return rotated[0] if single else rotated