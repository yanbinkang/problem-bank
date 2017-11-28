"""
http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
"""

def find_partition(arr):
    total = 0

    n = len(arr)

    for i in range(n):
        total += arr[i]

    if total % 2 != 0:
        return False

    table = [[None for i in range((total/2)+2)] for j in range(n)]

    for i in range(n+1):
        table[0][i] = True

    for i in range(1, total/2+1):
        table[i][0] = False

    for i in range(1, total/2+1):
        for j in range(1, n+1):
            table[i][j] = table[i][j-1]
            if i >= arr[j-1]:
                table[i][j] = table[i][j] or table[i - arr[j-1]][j-1]

    # for i in range(total/2+1):
    #     for j in range(n+1):
    #         print table[i][j]
    #     print "\n"

    # return table
    return table[total/2][n]


print find_partition([3, 1, 1, 2, 2, 1])
# print find_partition([1, 2, 11, 5])
print find_partition([5, 5, 4, 3])
print find_partition([3, 1, 1, 2, 2, 1, 2, 2])
print find_partition([2, 4, 7, 9])
