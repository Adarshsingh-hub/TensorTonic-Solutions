import math

def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    limit = math.sqrt(6.0 / fan_in)

    result = []
    for row in W:
        scaled_row = []
        for x in row:
            # Map x from [0, 1] to [-limit, limit]
            scaled_row.append(x * 2 * limit - limit)
        result.append(scaled_row)

    return result