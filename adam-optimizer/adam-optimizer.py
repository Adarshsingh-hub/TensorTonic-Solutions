import numpy as np

def adam_step(theta, grad, m, v, t, alpha=0.001, beta1=0.9, beta2=0.999, eps=1e-8):
    theta = np.asarray(theta, dtype=float)
    grad = np.asarray(grad, dtype=float)
    m = np.asarray(m, dtype=float)
    v = np.asarray(v, dtype=float)

    # update moments
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * (grad ** 2)

    # bias correction
    m_hat = m / (1 - beta1 ** t)
    v_hat = v / (1 - beta2 ** t)

    # parameter update
    theta = theta - alpha * m_hat / (np.sqrt(v_hat) + eps)

    return theta, m, v