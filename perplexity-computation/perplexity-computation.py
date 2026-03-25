import math

def perplexity(prob_distributions, actual_tokens):
    N = len(actual_tokens)
    log_sum = 0.0
    
    for i in range(N):
        prob = prob_distributions[i][actual_tokens[i]]
        log_sum += math.log(prob)
    
    return math.exp(-log_sum / N)