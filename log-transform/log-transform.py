import math

def log_transform(values):
    return [math.log1p(x) for x in values]