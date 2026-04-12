def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    result = []

    for row in matrix:
        # Get non-zero ratings
        non_zero = [x for x in row if x != 0]

        # If no ratings, keep row as is (all zeros)
        if not non_zero:
            result.append([0.0] * len(row))
            continue

        # Compute mean
        mean = sum(non_zero) / len(non_zero)

        # Normalize row
        normalized_row = []
        for x in row:
            if x != 0:
                normalized_row.append(float(x - mean))
            else:
                normalized_row.append(0.0)

        result.append(normalized_row)

    return result