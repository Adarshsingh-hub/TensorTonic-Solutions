import numpy as np

def apply_homogeneous_transform(T, points):
    points = np.array(points)

    single = points.ndim == 1
    if single:
        points = points.reshape(1,3)

    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack((points, ones))

    transformed_h = (T @ points_h.T).T

    transformed = transformed_h[:, :3]

    return transformed[0] if single else transformed