def count_trees(num_keys):
    if num_keys <= 1:
        return 1
    else:
        root = 1
        total = 0
        while root <= num_keys:
            left = count_trees(root - 1)
            right = count_trees(num_keys - root)

            total += left * right

            root += 1

    return total

# def count_trees(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1

#     total = 2 * count_trees(n - 1)

#     i = 1

#     while i < n -1:
#         total += count_trees(i) * count_trees(n - 1 - i)
#         i += 1

#     return total


print count_trees(1)
print count_trees(2)
print count_trees(3)
print count_trees(4)
