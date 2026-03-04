def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0):

    if warmup_steps > 0 and step < warmup_steps:
        return (step * initial_lr) / warmup_steps

    if total_steps == warmup_steps:
        return final_lr

    if step <= total_steps:
        return final_lr + (initial_lr - final_lr) * ((total_steps - step) / (total_steps - warmup_steps))

    return final_lr