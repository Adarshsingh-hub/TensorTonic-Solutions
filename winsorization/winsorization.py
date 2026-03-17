def winsorize(values, lower_pct, upper_pct):
    n = len(values)
    sorted_vals = sorted(values)
    def percentile(p):
        if n == 1:
            return float(sorted_vals[0])
        
        k = (n - 1) * p / 100.0
        f = int(k)
        c = min(f + 1, n - 1)
        
        if f == c:
            return float(sorted_vals[f])
        
        return sorted_vals[f] + (k - f) * (sorted_vals[c] - sorted_vals[f])

    lower_bound = percentile(lower_pct)
    upper_bound = percentile(upper_pct)
    result = []
    for v in values:
        if v < lower_bound:
            result.append(float(lower_bound))
        elif v > upper_bound:
            result.append(float(upper_bound))
        else:
            result.append(float(v))

    return result