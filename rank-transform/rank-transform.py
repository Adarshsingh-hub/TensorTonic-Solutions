import numpy as np

def rank_transform(values):
    values = np.array(values, dtype=float)
    n = len(values)

    ranks = np.zeros(n)

    sorted_indices = np.argsort(values)
    sorted_values = values[sorted_indices]

    i = 0
    while i < n:
        j = i
        while j < n and sorted_values[j] == sorted_values[i]:
            j += 1

        
        avg_rank = (i + 1 + j) / 2

        for k in range(i, j):
            ranks[sorted_indices[k]] = avg_rank

        i = j

    return ranks.tolist()