def weighted_moving_average(values, weights):
    n = len(values)
    k = len(weights)
    weight_sum = sum(weights)

    result = []

    for i in range(n - k + 1):
        weighted_sum = 0
        for j in range(k):
            weighted_sum += weights[j] * values[i + j]
        
        result.append(weighted_sum / weight_sum)

    return result