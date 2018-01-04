def lic(a_list):
    m = len(a_list)

    actual_solution = []

    # initial lis
    table = [1 for i in range(m)]

    # use this to print actual solution
    for i in range(m):
        actual_solution.append(i)

    i = 0
    while i < m:
        j = 0
        while j < i:
            if a_list[j] < a_list[i]:
                table[i] = max(table[i], table[j] + 1)
                actual_solution[i] = j
            j += 1
        i += 1

    print "table is", table
    print "actual solution array is", actual_solution

    # print actual solution
    new_t = table.index(max(table))
    while True:
        t = new_t
        print str(a_list[t]) + " "
        new_t = actual_solution[t]

        if t == new_t:
            break

    return "lic is %r" % max(table)

print lic([3, 4, -1, 0, 6, 2, 3])
# print lic([2, 5, 1, 8, 3])
# print lic([23,10,22,5,33,8,9,21,50,41,60,80,99, 22,23,24,25,26,27])
