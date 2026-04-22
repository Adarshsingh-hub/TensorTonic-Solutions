def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    if not values:
        return []

    ema = [values[0]]  # Initialize with first value

    for i in range(1, len(values)):
        current_ema = alpha * values[i] + (1 - alpha) * ema[-1]
        ema.append(current_ema)

    return ema