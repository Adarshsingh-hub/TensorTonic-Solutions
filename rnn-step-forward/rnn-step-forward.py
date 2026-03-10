import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    h_t = np.tanh(np.dot(x_t, Wx) + np.dot(h_prev, Wh) + b)

    return h_t