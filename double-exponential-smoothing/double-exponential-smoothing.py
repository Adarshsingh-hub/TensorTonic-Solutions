def double_exponential_smoothing(series, alpha, beta):
    n = len(series)
    level = series[0]
    trend = series[1] - series[0]
    
    levels = [float(level)]
    
    for t in range(1, n):
        prev_level = level
        level = alpha * series[t] + (1 - alpha) * (level + trend)
        trend = beta * (level - prev_level) + (1 - beta) * trend
        levels.append(float(level))
    
    return levels