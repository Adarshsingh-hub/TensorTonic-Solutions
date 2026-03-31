import numpy as np

def histogram_equalize(image):
    img = np.array(image, dtype=int)
    flat = img.flatten()
    hist = np.bincount(flat, minlength=256)
    cdf = np.cumsum(hist)
    cdf_min = cdf[np.nonzero(cdf)][0]
    
    total_pixels = flat.size
    if total_pixels == cdf_min:
        return np.zeros_like(img).tolist()
    new_vals = np.round((cdf - cdf_min) / (total_pixels - cdf_min) * 255).astype(int)
    equalized = new_vals[flat].reshape(img.shape)
    
    return equalized.tolist()