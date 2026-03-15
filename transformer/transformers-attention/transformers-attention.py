import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """

    # key dimension
    d_k = Q.size(-1)

    # Step 1: attention scores
    scores = torch.matmul(Q, K.transpose(-2, -1))

    # Step 2: scale
    scores = scores / math.sqrt(d_k)

    # Step 3: softmax
    attn_weights = F.softmax(scores, dim=-1)

    # Step 4: weighted sum of values
    output = torch.matmul(attn_weights, V)

    return output