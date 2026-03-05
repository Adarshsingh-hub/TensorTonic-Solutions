import math
from collections import Counter

def bleu_score(candidate, reference, max_n):
    if len(candidate) == 0:
        return 0.0

    precisions = []

    for n in range(1, max_n + 1):
        cand_ngrams = Counter(tuple(candidate[i:i+n]) for i in range(len(candidate)-n+1))
        ref_ngrams = Counter(tuple(reference[i:i+n]) for i in range(len(reference)-n+1))

        clipped = 0
        total = sum(cand_ngrams.values())

        if total == 0:
            return 0.0

        for ng in cand_ngrams:
            clipped += min(cand_ngrams[ng], ref_ngrams.get(ng, 0))

        p_n = clipped / total

        if p_n == 0:
            return 0.0

        precisions.append(p_n)

    
    c = len(candidate)
    r = len(reference)

    if c >= r:
        BP = 1.0
    else:
        BP = math.exp(1 - r / c)

    log_mean = sum(math.log(p) for p in precisions) / max_n

    bleu = BP * math.exp(log_mean)

    return bleu