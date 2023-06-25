def reverse_value(value, func):
    if value == 0:
        value = 1
    else:
        value = 0
    func(value)
    return value