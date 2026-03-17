def seasonal_average(series, period):
    n = len(series)
    
 
    sums = [0.0] * period
    counts = [0] * period


    for i in range(n):
        p = i % period   
        sums[p] += series[i]
        counts[p] += 1

    result = []
    for p in range(period):
        result.append(sums[p] / counts[p])

    return result