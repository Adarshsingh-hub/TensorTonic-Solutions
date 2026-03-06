def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """

    n = len(series)
    mean = sum(series) / n

    # total variance
    gamma0 = sum((x - mean) ** 2 for x in series)

    # constant series case
    if gamma0 == 0:
        return [1.0] + [0.0] * max_lag

    result = []

    for k in range(max_lag + 1):
        cov = 0
        for t in range(n - k):
            cov += (series[t] - mean) * (series[t + k] - mean)

        result.append(cov / gamma0)

    return result