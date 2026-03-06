def _dot(a, b):
    """Dot product of two vectors."""
    return sum(x * y for x, y in zip(a, b))


def lbfgs_direction(grad, s_list, y_list):
    """
    Compute the L-BFGS search direction using the two-loop recursion.
    """

    m = len(s_list)
    n = len(grad)

    # rho values
    rho = [1.0 / _dot(y_list[i], s_list[i]) for i in range(m)]

    # backward loop
    q = grad[:]
    alpha = [0.0] * m

    for i in reversed(range(m)):
        alpha[i] = rho[i] * _dot(s_list[i], q)
        q = [qj - alpha[i] * yij for qj, yij in zip(q, y_list[i])]

    # initial scaling (H0)
    s_last = s_list[-1]
    y_last = y_list[-1]

    gamma = _dot(s_last, y_last) / _dot(y_last, y_last)

    r = [gamma * qi for qi in q]

    # forward loop
    for i in range(m):
        beta = rho[i] * _dot(y_list[i], r)
        r = [
            rj + s_list[i][j] * (alpha[i] - beta)
            for j, rj in enumerate(r)
        ]

    # descent direction
    direction = [-ri for ri in r]

    return direction