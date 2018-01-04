def total_num_of_ways(total, coin_list):
    m = len(coin_list)
    table = [[0 for i in range(total + 1)] for j in range(m)]

    for i in range(total + 1):
        table[0][i] = 1

    for i in range(1, len(table)):
        table[i][0] = 1

    for i in range(1, m):
        for j in range(1, total + 1):
            if j >= coin_list[i]:
                table[i][j] = table[i - 1][j] + table[i][j - coin_list[i]]
            else:
                table[i][j] = table[i - 1][j]

    return table[m - 1][total]


print total_num_of_ways(5, [1, 2, 3])
print total_num_of_ways(11, [5, 7])
