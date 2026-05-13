import numpy as np

def softmax(x, axis=-1):
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Compute multi-head attention.
    Returns an array of shape (batch_size, seq_len, d_model).
    """
    batch_size, seq_len, d_model = Q.shape
    d_k = d_model // num_heads

    # 1. Linear projections
    Q_proj = Q @ W_q
    K_proj = K @ W_k
    V_proj = V @ W_v

    # 2. Split into heads: (batch, seq_len, d_model) -> (batch, num_heads, seq_len, d_k)
    def split_heads(x):
        x = x.reshape(batch_size, seq_len, num_heads, d_k)
        return np.transpose(x, (0, 2, 1, 3))

    Q_heads = split_heads(Q_proj)
    K_heads = split_heads(K_proj)
    V_heads = split_heads(V_proj)

    # 3. Scaled dot-product attention
    scores = np.matmul(Q_heads, np.transpose(K_heads, (0, 1, 3, 2))) / np.sqrt(d_k)
    attn_weights = softmax(scores, axis=-1)
    head_outputs = np.matmul(attn_weights, V_heads)

    # 4. Concatenate heads: (batch, num_heads, seq_len, d_k) -> (batch, seq_len, d_model)
    head_outputs = np.transpose(head_outputs, (0, 2, 1, 3))
    concat = head_outputs.reshape(batch_size, seq_len, d_model)

    # 5. Output projection
    output = concat @ W_o

    return output