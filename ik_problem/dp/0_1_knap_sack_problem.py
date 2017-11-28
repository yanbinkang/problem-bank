# tuples contain (weight, value)
def zero_one_knap_sack(total_weight, capacity):
    m = len(capacity)
    table = [[0 for i in range(total_weight + 1)] for j in range(m)]

    for i in range(1, total_weight + 1):
        table[0][i] = 1

    for i in range(1, m):
        for j in range(1, total_weight + 1):
            if j < capacity[i][0]:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(capacity[i][1] + table[i - 1][j - capacity[i][0]], table[i - 1][j])

    return table[m - 1][total_weight]

print zero_one_knap_sack(7, [(1, 1), (3, 4), (4, 5), (5, 7)])
