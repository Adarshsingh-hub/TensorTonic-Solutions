import numpy as np

def random_forest_vote(predictions):
    predictions = np.array(predictions)

    T,N = predictions.shape
    result = []

    for i in range(N):
        votes = predictions[:,i]
        values, counts = np.unique(votes, return_counts = True)

        max_count = np.max(counts)

        candidates = values[counts == max_count]

        result.append(np.min(candidates))

    return np.array(result).tolist()