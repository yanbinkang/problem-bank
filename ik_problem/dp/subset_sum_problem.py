def subset_sum_problem(a_list, total):
    table = [[None for i in range(total + 1)] for j in range(len(a_list) + 1)]

    for i in range(total + 1):
        table[0][i] = i

    for i in range(1, len(a_list)):
        table[i][0] = True

    return table


print subset_sum_problem([2, 3, 7, 8, 10], 11)
