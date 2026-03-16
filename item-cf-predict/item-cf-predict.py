def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """

    weighted_sum = 0.0
    similarity_sum = 0.0

    for i in range(len(user_ratings)):
        if i == target:
            continue
        
        rating = user_ratings[i]
        similarity = item_similarities[i]

        if similarity > 0 and rating != 0:
            weighted_sum += similarity * rating
            similarity_sum += similarity

    if similarity_sum == 0:
        return 0.0

    return weighted_sum / similarity_sum