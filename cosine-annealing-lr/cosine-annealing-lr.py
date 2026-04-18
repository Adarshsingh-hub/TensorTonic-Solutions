import math

def cosine_annealing_schedule(base_lr, min_lr, total_steps, current_step):
    """
    Compute the learning rate using cosine annealing.
    """
    cosine_decay = math.cos((current_step / total_steps) * math.pi)
    lr = min_lr + 0.5 * (base_lr - min_lr) * (1 + cosine_decay)
    return lr