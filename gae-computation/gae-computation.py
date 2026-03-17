def gae(rewards, values, gamma, lam):
    T = len(rewards)
    advantages = [0.0] * T
    gae = 0.0

    # Iterate backward
    for t in reversed(range(T)):
        delta = rewards[t] + gamma * values[t + 1] - values[t]
        gae = delta + gamma * lam * gae
        advantages[t] = gae

    return advantages