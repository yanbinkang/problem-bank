"""
http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/
You can only traverse right and down for this problem.
The only difference between this problem and the one from the URL is that you can also traverse diagonal. So on line 26 you'll have to add temp[i - 1][j - 1] when finding min.
"""
def minimum_cost_path(matrix):
    m = len(matrix[0])
    n = len(matrix)
    temp = [[0 for i in range(m)] for j in range(n)]

    # first value in temp is first value in matrix
    temp[0][0] = matrix[0][0]

    # calculate cost of first row
    for i in range(1, m):
        temp[0][i] = temp[0][i - 1] + matrix[0][i]

    # calculate cost of first column
    for i in range(1, n):
        temp[i][0] = temp[i - 1][0] + matrix[i][0]

    # calculate cost from (1, 1) to (m-1, n-1)
    # find minimum of top and left of temp plus actual matrix value
    for i in range(1, n):
        for j in range(1, m):
            temp[i][j] = min(temp[i -1][j], temp[i][j - 1]) + matrix[i][j]

    return temp[n-1][m-1]

matrix_1 = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
matrix_2 = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
print minimum_cost_path(matrix_1)
print minimum_cost_path(matrix_2)
