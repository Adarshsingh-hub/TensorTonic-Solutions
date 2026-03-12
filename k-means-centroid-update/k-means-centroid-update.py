def k_means_centroid_update(points, assignments, k):
    dim = len(points[0])
    sums = [[0.0] * dim for _ in range(k)]
    counts = [0] * k

   
    for point, cluster in zip(points, assignments):
        counts[cluster] += 1
        for d in range(dim):
            sums[cluster][d] += point[d]

    
    centroids = []
    for j in range(k):
        if counts[j] == 0:
            centroids.append([0.0] * dim)
        else:
            centroid = [sums[j][d] / counts[j] for d in range(dim)]
            centroids.append(centroid)

    return centroids
    