def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """

    result = values.copy()
    n = len(result)

    i = 0
    while i < n:
        if result[i] is None:
            left = i - 1

            # find right boundary
            j = i
            while j < n and result[j] is None:
                j += 1
            right = j

            v_left = result[left]
            v_right = result[right]

            gap = right - left

            # fill the gap
            for k in range(left + 1, right):
                result[k] = v_left + (k - left) / gap * (v_right - v_left)

            i = right
        else:
            i += 1

    return result