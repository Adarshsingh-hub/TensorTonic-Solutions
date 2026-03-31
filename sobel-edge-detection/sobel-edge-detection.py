import numpy as np

def sobel_edges(image):
    image = np.array(image, dtype=float)
    h, w = image.shape
    
    Kx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    
    Ky = np.array([[-1, -2, -1],
                   [ 0,  0,  0],
                   [ 1,  2,  1]])
    
    
    padded = np.pad(image, ((1, 1), (1, 1)), mode='constant')
    
    output = np.zeros((h, w))
    
    for i in range(h):
        for j in range(w):
            region = padded[i:i+3, j:j+3]
            
            Gx = np.sum(region * Kx)
            Gy = np.sum(region * Ky)
            
            output[i, j] = np.sqrt(Gx**2 + Gy**2)
    
    return output.tolist()