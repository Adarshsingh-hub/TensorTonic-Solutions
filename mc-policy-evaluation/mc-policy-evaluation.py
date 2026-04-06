import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    returns_sum = np.zeros(n_states)
    returns_count = np.zeros(n_states)

    for episode in episodes:
        visited = set()
        G = 0
        
        # Compute returns backward
        returns = [0] * len(episode)
        for t in reversed(range(len(episode))):
            state, reward = episode[t]
            G = reward + gamma * G
            returns[t] = G
        
        # First-visit logic
        for t, (state, _) in enumerate(episode):
            if state not in visited:
                returns_sum[state] += returns[t]
                returns_count[state] += 1
                visited.add(state)

    # Avoid division by zero
    V = np.zeros(n_states)
    for s in range(n_states):
        if returns_count[s] > 0:
            V[s] = returns_sum[s] / returns_count[s]

    return V