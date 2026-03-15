import numpy as np

def naive_bayes_bernoulli(X_train, y_train, X_test):
    """
    Compute log-likelihood P(y|x) for Bernoulli Naive Bayes.
    """

    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)

    n_train, d = X_train.shape
    classes = np.sort(np.unique(y_train))
    n_classes = len(classes)

    log_posteriors = np.zeros((X_test.shape[0], n_classes))

    for idx, c in enumerate(classes):

        # select samples of class c
        X_c = X_train[y_train == c]
        n_y = X_c.shape[0]

        # class prior
        log_prior = np.log(n_y / n_train)

        # Laplace smoothing
        theta = (np.sum(X_c, axis=0) + 1) / (n_y + 2)

        log_theta = np.log(theta)
        log_1_theta = np.log(1 - theta)

        # compute log likelihood for all test samples
        log_likelihood = X_test @ log_theta + (1 - X_test) @ log_1_theta

        log_posteriors[:, idx] = log_prior + log_likelihood

    return log_posteriors