def max_value(length, prices):
    table = [[0 for i in range(length + 1)] for j in range(len(prices.keys()) + 1)]

    # keep this because first row changes for eg it's not all 1's
    for i in range(length + 1):
        table[0][i] = i

    for i in range(1, len(table)):
        table[i][0] = 0

    for i in range(1, len(prices.keys()) + 1):
        for j in range(1, length + 1):
            if j >= i:
                table[i][j] = max(table[i - 1][j], prices[i] + table[i][j - i])
            else:
                table[i][j] = table[i - 1][j]

    return table[len(prices.keys()) - 1][length]


print max_value(5, {1: 2, 2: 5, 3: 7, 4: 8})
print max_value(8, {1: 1, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20})
print max_value(8, {1: 3, 2: 5, 3: 8, 4: 9, 5: 10, 6: 17, 7: 17, 8: 20})


"""
# solution with tuples
def max_value(length, prices):
    table = [[0 for i in range(length + 1)] for j in range(len(prices) + 1)]

    for i in range(length + 1):
        table[0][i] = i

    for i in range(1, len(table)):
        table[i][0] = 0

    for i in range(1, len(prices) + 1):
        for j in range(1, length + 1):
            if j >= prices[i - 1][0]:
                table[i][j] = max(table[i - 1][j], prices[i - 1][1] + table[i][j - prices[i - 1][0]])
            else:
                table[i][j] = table[i - 1][j]

    return table[len(prices) - 1][length]

print max_value(5, [(1, 2), (2, 5), (3, 7), (4, 8)])
print max_value(8, [(1, 1), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17), (8, 20)])
print max_value(8, [(1, 3), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17), (8, 20)])

"""
