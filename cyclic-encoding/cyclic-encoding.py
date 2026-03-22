import numpy as np

def cyclic_encoding(values, period):
    values = np.array(values, dtype=float)
    theta = (2 * np.pi * values) / period  # ✅ correct division

    sin_vals = np.sin(theta)
    cos_vals = np.cos(theta)

    return [[float(s), float(c)] for s, c in zip(sin_vals, cos_vals)]