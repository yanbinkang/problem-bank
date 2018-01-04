"""
solution: http://codercareer.blogspot.com/2013/02/no-44-maximal-stolen-values.html
"""

def max_stolen_value(values):
    length = len(values)

    if length == 0:
        return 0

    value_1 = values[0]

    if length == 1:
        return value_1

    value_2 = max(values[0], values[1])

    if length == 2:
        return value_2

    i = 2
    while i < length:
        value = max(value_2, value_1 + values[i])
        value_1 = value_2
        value_2 = value
        i += 1

    return value

print max_stolen_value([6, 1, 2, 7])
print max_stolen_value([4, 6, 1, 2, 7])
print max_stolen_value([5, 1, 2, 3, 4, 5])
print max_stolen_value([4, 99, 99, 99])
