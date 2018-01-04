"""
You are given a matrix N x M filled with positive numbers and -1s.  We're looking for the best path in that matrix. A path is a series of cells. Path-sum is the sum of all numbers in the cells of the path. Best path is the path with maximum path-sum. Write a recursive method, to find the best path in such a matrix.

1. A path always starts from top left and ends with bottom right
2. You can walk downwards and to the right, but you cannot walk to the diagonal cell. You also cannot move up or left.
3. You cannot walk on the cell that has -1

Input: N x M matrix filled with positive numbers and some -1s. You can represent the matrix in a two-dimensional array.
Output:  Best path, and it's sum. You can represent a path with pairs of (row,col).

(This problem does not have test-cases, in order to let you define your input flexibly in your main method)


Examples:

1 2 8
7 20 8
95 -1 8

Best Path: 1->7->20->8->8
Path Sum: 44

1 2 8
7 -1 8
5 3 8

Best Path: 1->2->8->8->8
Path Sum: 27
"""
# O(m + n) space
# O(2^m+n) time
def best_paths(arr, m, n):
    return best_path_recursion(arr, m, n, 0, 0)


def best_path_recursion(array, m, n, i, j):
    if ((i == m - 1) and (j == n - 1)):
        return array[i][j]


    if (i == m - 1):
        best_path = best_path_recursion(array, m, n, i, j + 1)
        if best_path == -1:
            return -1
        return array[i][j] + best_path


    if (j == n - 1):
        best_path = best_path_recursion(array, m, n, i + 1, j)
        if best_path == -1:
            return -1
        return array[i][j] + best_path

    best_path = best_path_recursion(array, m, n, i + 1, j)

    down = -1 if best_path == -1 else array[i][j] + best_path

    best_path = best_path_recursion(array, m, n, i, j + 1)

    right = -1 if best_path == -1 else array[i][j] + best_path

    return max(down, right)


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
arr_5 = [[-1]]
arr_6 = [[1, 2, 3],
         [4, 5, 6],
         [7, -1, 9]]
arr_7 = [[1, 2, 3],
         [4, 5, -1],
         [7, 8, 9]]
arr_8 = [[2, 2, 1, 1, 1],
         [1, -1, 1, 1, 1],
         [1, 2, -1, 1, 1],
         [1, 1, 2, -1, 1],
         [1, 1, 1, 2, 2]]
arr_9 = [[1, 2, 8],
         [7, 20, 8],
         [95, -1, 8]]
arr_10 = [[1, 2, 8],
         [7, -1, 8],
         [5, 3, 8]]

# print best_paths(arr_1, 1, 1)
# print best_paths(arr_2, 1, 3)
# print best_paths(arr_3, 3, 3)
# print best_paths(arr_4, 5, 5)
# print best_paths(arr_5, 1, 1)
# print best_paths(arr_6, 3, 3)
# print best_paths(arr_7, 3, 3)
# print best_paths(arr_8, 5, 5)
print best_paths(arr_9, 3, 3)
# print best_paths(arr_10, 3, 3)

