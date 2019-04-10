"""
https://leetcode.com/problems/spiral-matrix-ii/description/

Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    i = 0
    matrix = [[None for _ in range(n)] for _ in range(n)]

    row_start, col_start = 0, 0
    row_end, col_end = n - 1, n - 1

    while row_start <= row_end and col_start <= col_end:
        for j in range(col_start, col_end + 1):
            i += 1
            matrix[row_start][j] = i

        row_start += 1

        for j in range(row_start, row_end + 1):
            i += 1
            matrix[j][col_end] = i

        col_end -= 1

        if row_start > row_end or col_start > col_end:
            break

        for j in reversed(range(col_start, col_end + 1)):
            i += 1
            matrix[row_end][j] = i

        row_end -= 1

        for j in reversed(range(row_start, row_end + 1)):
            i += 1
            matrix[j][col_start] = i

        col_start += 1

    return matrix


if __name__ == "__main__":
    print(generateMatrix(3))
