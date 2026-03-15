def policy_gradient_loss(log_probs, rewards, gamma):
    
    T = len(rewards)

   
    returns = [0.0] * T
    G = 0.0
    for t in reversed(range(T)):
        G = rewards[t] + gamma * G
        returns[t] = G

    
    mean_return = sum(returns) / T

    
    advantages = [g - mean_return for g in returns]

   
    loss = 0.0
    for lp, adv in zip(log_probs, advantages):
        loss += lp * adv

    loss = -loss / T

    return float(loss)