def discount_returns(rewards, gamma):
    n = len(rewards)
    discounted = [0] * n
    
    running_sum = 0
    
    for i in reversed(range(n)):
        running_sum = rewards[i] + gamma * running_sum
        discounted[i] = running_sum
        
    return discounted