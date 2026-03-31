import numpy as np

def silhouette_score(X, labels):
    X = np.array(X)
    labels = np.array(labels)
    
    n = X.shape[0]

    diff = X[:, np.newaxis, :] - X[np.newaxis, :, :]
    D = np.sqrt(np.sum(diff**2, axis=2))
    
    unique_labels = np.unique(labels)
    
    a = np.zeros(n)
    b = np.full(n, np.inf)
    
    for label in unique_labels:
        mask = labels == label
        
        if np.sum(mask) > 1:
            intra_dist = D[mask][:, mask]
            a[mask] = (np.sum(intra_dist, axis=1) - 0) / (np.sum(mask) - 1)
        else:
            a[mask] = 0
        
        for other_label in unique_labels:
            if other_label == label:
                continue
                
            other_mask = labels == other_label
            inter_dist = D[mask][:, other_mask]
            mean_dist = np.mean(inter_dist, axis=1)
            
            b[mask] = np.minimum(b[mask], mean_dist)
    
    s = (b - a) / np.maximum(a, b)
    
    return np.mean(s)