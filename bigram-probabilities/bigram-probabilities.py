from collections import defaultdict

def bigram_probabilities(tokens):
    counts = defaultdict(int)

    # count bigrams
    for i in range(len(tokens) - 1):
        w1 = tokens[i]
        w2 = tokens[i + 1]
        counts[(w1, w2)] += 1

    vocab = sorted(set(tokens))
    V = len(vocab)

    probs = {}

    for w1 in vocab:
        # denominator: sum of bigrams starting with w1
        total = sum(counts[(w1, w)] for w in vocab)

        for w2 in vocab:
            c = counts[(w1, w2)]
            probs[(w1, w2)] = (c + 1) / (total + V)

    return dict(counts), probs