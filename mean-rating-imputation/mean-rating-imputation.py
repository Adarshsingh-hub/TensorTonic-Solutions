def mean_rating_imputation(ratings_matrix, mode):
    rows = len(ratings_matrix)
    cols = len(ratings_matrix[0])

    result = [row[:] for row in ratings_matrix]

    if mode == "user":
        for i in range(rows):
            
            values = [v for v in ratings_matrix[i] if v != 0]
            
            if len(values) == 0:
                continue  

            mean = sum(values) / len(values)

            for j in range(cols):
                if result[i][j] == 0:
                    result[i][j] = float(mean)

    elif mode == "item":
        for j in range(cols):
            values = [ratings_matrix[i][j] for i in range(rows) if ratings_matrix[i][j] != 0]
            
            if len(values) == 0:
                continue  

            mean = sum(values) / len(values)

            for i in range(rows):
                if result[i][j] == 0:
                    result[i][j] = float(mean)

    else:
        raise ValueError("mode must be 'user' or 'item'")

    return result