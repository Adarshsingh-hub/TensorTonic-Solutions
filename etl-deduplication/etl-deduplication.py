def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """

    def get_key(record):
        return tuple(record[col] for col in key_columns)

    def count_none(record):
        return sum(v is None for v in record.values())

    best_record = {}   # key -> selected record
    key_order = []     # preserves first appearance

    for record in records:
        key = get_key(record)

        # First time seeing this key
        if key not in best_record:
            best_record[key] = record
            key_order.append(key)
        else:
            if strategy == "first":
                continue  # keep existing

            elif strategy == "last":
                best_record[key] = record

            elif strategy == "most_complete":
                current_best = best_record[key]

                if count_none(record) < count_none(current_best):
                    best_record[key] = record
                # tie → keep first (do nothing)

    # Preserve order of first appearance
    return [best_record[key] for key in key_order]