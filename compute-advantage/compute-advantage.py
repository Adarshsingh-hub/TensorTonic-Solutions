import numpy as np

def compute_advantage(states, rewards, V, gamma):
    T = len(rewards)
    G = np.zeros(T)
    A = np.zeros(T)

    # Step 1: Compute returns (backward)
    G[-1] = rewards[-1]
    for t in reversed(range(T - 1)):
        G[t] = rewards[t] + gamma * G[t + 1]

    # Step 2: Compute advantage
    for t in range(T):
        A[t] = G[t] - V[states[t]]

    return A
    
