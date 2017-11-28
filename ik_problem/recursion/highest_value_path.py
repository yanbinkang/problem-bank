"""
Given an MxN matrix with each cell having an integer value, find the highest-value path from top left corner to the bottom right.
"""

def best_path_recursion(matrix, m, n, i, j):
    if (i == m - 1) and (j == n - 1):
        return matrix[i][j]

    if (i == m - 1):
        return matrix[i][j] + best_path_recursion(matrix, m, n, i, j + 1)

    if (j == n - 1):
        return matrix[i][j] + best_path_recursion(matrix, m, n, i + 1, j)

    down = matrix[i][j] + best_path_recursion(matrix, m, n, i + 1, j)
    right = matrix[i][j] + best_path_recursion(matrix, m, n, i, j + 1)

    return max(down, right)

def best_path(a_list, m, n):
    return best_path_recursion(a_list, m, n, 0, 0)



arr_1 = [[9]]
arr_2 = [[1, 2, 3]]
arr_3 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

arr_4 = [[2, 2, 1, 1, 1],
         [1, 2, 1, 1, 1],
         [1, 2, 2, 1, 1],
         [1, 1, 2, 2, 1],
         [1, 1, 1, 2, 2]]


print best_path(arr_1, 1, 1)
print best_path(arr_2, 1, 3)
print best_path(arr_3, 3, 3)
print best_path(arr_4, 5, 5)
