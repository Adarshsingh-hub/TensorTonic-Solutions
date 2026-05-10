def moving_median(values, window_size):
    result = []
    n = len(values)

    for i in range(n - window_size + 1):
        window = sorted(values[i:i + window_size])
        mid = window_size // 2

        if window_size % 2 == 1:
            median = float(window[mid])
        else:
            median = (window[mid - 1] + window[mid]) / 2.0

        result.append(median)

    return result