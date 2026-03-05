import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    Q = np.array(Q, dtype=float)

    # best next action value
    max_next_q = np.max(Q[s_next])

    # TD target
    target = r + gamma * max_next_q

    # update rule
    Q[s, a] = Q[s, a] + alpha * (target - Q[s, a])

    return Q