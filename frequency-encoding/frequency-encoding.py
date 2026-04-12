def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    total = len(values)

    # Count frequencies
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1

    # Convert to proportions
    for key in freq:
        freq[key] = freq[key] / total

    # Replace values with their frequency
    return [float(freq[v]) for v in values]