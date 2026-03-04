import numpy as np
from collections import Counter

def tfidf_vectorizer(documents):
    
    tokenized_docs = [doc.lower().split() for doc in documents]

    
    vocab = sorted(set(word for doc in tokenized_docs for word in doc))
    vocab_index = {word: i for i, word in enumerate(vocab)}

    N = len(documents)
    V = len(vocab)

    tf = np.zeros((N, V))
    df = np.zeros(V)

    
    for i, doc in enumerate(tokenized_docs):
        counts = Counter(doc)
        total_terms = len(doc)

        for word, count in counts.items():
            j = vocab_index[word]
            tf[i, j] = count / total_terms
            df[j] += 1

    
    idf = np.log(N / df)

    
    tfidf = tf * idf

    return tfidf, vocab