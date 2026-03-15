def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """

    n = len(values)
    if n == 1:
        return [0.0]

    arr = sorted(values)

    # helper median function
    def median(lst):
        m = len(lst)
        mid = m // 2
        if m % 2 == 1:
            return float(lst[mid])
        else:
            return (lst[mid - 1] + lst[mid]) / 2.0

    med = median(arr)

    mid = n // 2
    if n % 2 == 0:
        lower = arr[:mid]
        upper = arr[mid:]
    else:
        lower = arr[:mid]
        upper = arr[mid+1:]

    q1 = median(lower)
    q3 = median(upper)

    iqr = q3 - q1

    result = []
    for v in values:
        if iqr == 0:
            result.append(float(v - med))
        else:
            result.append(float((v - med) / iqr))

    return result