def matrix_factorization_sgd_step(U, V, r, lr, reg):
    """
    Perform one SGD step for matrix factorization.
    """
    # Predicted rating (dot product)
    pred = sum(u * v for u, v in zip(U, V))
    
    # Error
    error = r - pred
    
    # Copy of U (important!)
    U_old = U.copy()
    
    # Update U
    for i in range(len(U)):
        U[i] += lr * (error * V[i] - reg * U[i])
    
    # Update V (use old U)
    for i in range(len(V)):
        V[i] += lr * (error * U_old[i] - reg * V[i])
    
    return U, V