def normalize_value(value, min, max):
    """make sure value is in <min, max>, return normalized value"""
    if value > max:
        value = max
    if value < min:
        value = min
    return value
