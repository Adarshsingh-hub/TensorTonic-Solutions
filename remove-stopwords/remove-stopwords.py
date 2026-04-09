def remove_stopwords(tokens, stopwords):
    stopword_set = set(stopwords)
    filtered = [token for token in tokens if token not in stopword_set]
    return filtered