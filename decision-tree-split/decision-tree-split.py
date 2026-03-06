import numpy as np

def decision_tree_split(X, y):
    
    X = np.array(X)
    y = np.array(y)
    n_samples, n_features = X.shape

    def gini(labels):
        if len(labels) == 0:
            return 0
        _, counts = np.unique(labels, return_counts=True)
        probs = counts / len(labels)
        return 1 - np.sum(probs ** 2)

    parent_gini = gini(y)

    best_gain = -1
    best_feature = None
    best_threshold = None

    for f in range(n_features):
        values = np.sort(np.unique(X[:, f]))

        
        thresholds = (values[:-1] + values[1:]) / 2

        for t in thresholds:
            left_mask = X[:, f] <= t
            right_mask = X[:, f] > t

            y_left = y[left_mask]
            y_right = y[right_mask]

            gini_left = gini(y_left)
            gini_right = gini(y_right)

            w_left = len(y_left) / n_samples
            w_right = len(y_right) / n_samples

            gini_split = w_left * gini_left + w_right * gini_right
            gain = parent_gini - gini_split

            if (gain > best_gain or
               (gain == best_gain and 
                (best_feature is None or f < best_feature or
                 (f == best_feature and t < best_threshold)))):
                
                best_gain = gain
                best_feature = f
                best_threshold = t

    return [best_feature, float(best_threshold)]