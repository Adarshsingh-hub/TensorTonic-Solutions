import numpy as np

def get_alpha_bar(betas: np.ndarray) -> np.ndarray:
    """
    Compute cumulative product of (1 - beta).
    """
    alphas = 1.0 - betas
    alpha_bar = np.cumprod(alphas)
    return alpha_bar
def forward_diffusion(
    x_0: np.ndarray,
    t: int,
    betas: np.ndarray
) -> tuple:
    """
    Sample x_t from q(x_t | x_0).
    """
    alpha_bar = get_alpha_bar(betas)
    
    # Get ᾱ_t (careful with indexing)
    alpha_bar_t = alpha_bar[t]
    
    # Sample noise
    epsilon = np.random.randn(*x_0.shape)
    
    # Compute x_t
    x_t = (
        np.sqrt(alpha_bar_t) * x_0 +
        np.sqrt(1 - alpha_bar_t) * epsilon
    )
    
    return x_t, epsilon
