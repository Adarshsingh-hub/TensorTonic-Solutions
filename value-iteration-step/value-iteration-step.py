def value_iteration_step(values, transitions, rewards, gamma):
    num_states = len(values)
    new_values = []

    for s in range(num_states):
        action_values = []

        for a in range(len(transitions[s])):
            expected_value = 0.0

            for s_prime in range(num_states):
                expected_value += transitions[s][a][s_prime]*values[s_prime]

            q_value = rewards[s][a] + gamma * expected_value
            action_values.append(q_value)

        new_values.append(max(action_values))
    return new_values