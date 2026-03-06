import numpy as np

def gaussian_naive_bayes(X_train, y_train, X_test):
    
    X_train = np.array(X_train, dtype=float)
    y_train = np.array(y_train)
    X_test = np.array(X_test, dtype=float)

    epsilon = 1e-9
    classes = np.unique(y_train)
    n_samples = len(X_train)

    priors = {}
    means = {}
    variances = {}

    for c in classes:
        X_c = X_train[y_train == c]
        priors[c] = len(X_c) / n_samples
        means[c] = np.mean(X_c, axis=0)
        variances[c] = np.var(X_c, axis=0) + epsilon

    predictions = []

    for x in X_test:
        log_posteriors = []

        for c in classes:
            prior = np.log(priors[c])
            mean = means[c]
            var = variances[c]

            log_likelihood = np.sum(
                -0.5 * np.log(2 * np.pi * var)
                - ((x - mean) ** 2) / (2 * var)
            )

            log_posteriors.append(prior + log_likelihood)

        predictions.append(classes[np.argmax(log_posteriors)])

    return list(predictions)