import numpy as np

def adagrad_step(w, g, G, lr, eps):
    w = np.asarray(w, dtype=float)
    g = np.asarray(g, dtype=float)
    G = np.asarray(G, dtype=float)

    # accumulate squared gradients
    G = G + g**2

    # parameter update
    w = w - lr * g / np.sqrt(G + eps)

    return (w.tolist(), G.tolist())