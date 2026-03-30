def target_encoding(categories, targets):
    # Step 1: store sum and count
    sums = {}
    counts = {}

    for cat, target in zip(categories, targets):
        if cat not in sums:
            sums[cat] = 0
            counts[cat] = 0
        sums[cat] += target
        counts[cat] += 1

    # Step 2: compute means
    means = {}
    for cat in sums:
        means[cat] = sums[cat] / counts[cat]

    # Step 3: replace categories with mean
    result = []
    for cat in categories:
        result.append(means[cat])

    return result