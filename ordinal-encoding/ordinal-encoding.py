def ordinal_encoding(values, ordering):
    mapping = {val: idx for idx, val in enumerate(ordering)}
    return [mapping[v] for v in values]