import math

def novelty_score(recommendations, item_counts, n_users):
    if not recommendations:
        return 0.0

    total_novelty = 0.0

    for item in recommendations:
        count = item_counts[item]
        popularity = count / n_users
        self_information = -math.log2(popularity)
        total_novelty += self_information

    return total_novelty / len(recommendations)