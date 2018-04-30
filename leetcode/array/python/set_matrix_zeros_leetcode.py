"""
https://leetcode.com/problems/set-matrix-zeroes/#/description

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""

"""
O(m * n) time, O(1) space
https://discuss.leetcode.com/topic/27265/o-1-java-straightforward-idea

Use the first column and the first row as marker:

1. first scan through the whole matrix, and if one row i has zero, label matrix[i][0] = 0, if column j has zero, then label matrix[0][j] = 0.

If we find the first row has zero, then mark a boolean row = true, if the first column has zeros, mark a boolean col = true

2. By the markers on the first row and first col, set the other columns and rows to zeros. (first row and first column already contain zeros)

3. According to booleans row and col, decide whether to set first row and column to zeros
"""
def set_zeroes(matrix):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0: return

    rows, cols = len(matrix), len(matrix[0])

    row, col = False, False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

                if i == 0: row = True

                if j == 0: col = True

    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, cols):
                matrix[i][j] = 0

    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0

    if row:
        for j in range(cols):
            matrix[0][j] = 0

    if col:
        for i in range(rows):
            matrix[i][0] = 0

def set_zeroes_2(matrix):
    col_0 = False
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        if matrix[i][0] == 0:
            col_0 = True
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0

    for i in reversed(range(rows)):
        for j in reversed(range(1, cols)):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

        if col_0:
            matrix[i][0] = 0

if __name__ == '__main__':
    matrix = [[1, 2, 0, 3],
              [2, 3, 4, 5],
              [9, 5, 6, 7]]

    print 'matrix before set zeros: %s' % matrix
    set_zeroes(matrix)
    print 'matrix after set zeros: %s' % matrix
