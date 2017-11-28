def min_number_coins(coin_list, total):
    m = len(coin_list)
    table = [[0 for i in range(total+1)] for j in range(m)]

    # fill first row since it's trivial
    for i in range(1, total + 1):
        table[0][i] = i

    for i in range(1, m):
        for j in range(1, total + 1):
            if j >= coin_list[i]:
                table[i][j] = min(table[i - 1][j], 1 + table[i][j - coin_list[i]])
            else:
                table[i][j] = table[i - 1][j]
    # print table
    return table[m - 1][total]


print min_number_coins([1, 5, 6, 8], 11)
