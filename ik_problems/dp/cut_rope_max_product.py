def max_product(num):
    table = [0 for i in range(num + 1)]

    table[0] = 1

    for i in range(1, num + 1):
        table[i] = i

    i = 2
    while i <= num:
        j = 1
        while j <= i:
            table[i] = max(table[i], table[j] * table[i - j])
            j += 1
        i += 1

    return table[num]

# print max_product(4)
# print max_product(10)
# print max_product(13)
print max_product(2)
# print max_product(65)


# def max_prod(n):
#     table = [None for i in range(n + 1)]

#     table[0] = table[1] = 0

#     i = 1

#     while i <= n:
#         max_val = 0
#         j = 1
#         while j <= i/2:
#             max_val = max(max_val, (i - j)*j, j * table[i - j])
#             j += 1
#         table[i] = max_val
#         i += 1
