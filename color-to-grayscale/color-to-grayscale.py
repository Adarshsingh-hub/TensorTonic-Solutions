import numpy as np

def color_to_grayscale(image):
    image = np.array(image)  # convert list → numpy array

    R = image[:, :, 0]
    G = image[:, :, 1]
    B = image[:, :, 2]

    gray = 0.299 * R + 0.587 * G + 0.114 * B

    return gray.tolist()