def simple_moving_average(values, window_size):
    result = []
    
    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        avg = sum(window) / window_size
        result.append(avg)
    
    return result