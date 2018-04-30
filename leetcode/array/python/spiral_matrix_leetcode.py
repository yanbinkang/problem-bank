"""
https://leetcode.com/problems/spiral-matrix/description/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

solve next: https://leetcode.com/problems/spiral-matrix-ii/description/
"""
# https://discuss.leetcode.com/topic/3713/super-simple-and-easy-to-understand-solution
def spiral_order(matrix):
    result = []

    if len(matrix) == 0:
        return result

    row_begin, col_begin = 0, 0
    row_end = len(matrix) - 1
    col_end = len(matrix[0]) - 1


    while row_begin <= row_end and col_begin <= col_end:
        # traverse right
        for j in range(col_begin, col_end + 1):
            result.append(matrix[row_begin][j])

        row_begin += 1

        # traverse down
        for j in range(row_begin, row_end + 1):
            result.append(matrix[j][col_end])

        col_end -= 1

        if row_begin > row_end or col_begin > col_end:
            break


        # traverse left
        for j in reversed(range(col_begin, col_end + 1)):
            result.append(matrix[row_end][j])

        row_end -= 1

        # traverse up
        for j in reversed(range(row_begin, row_end + 1)):
            result.append(matrix[j][col_begin])

        col_begin += 1



    return result


# https://discuss.leetcode.com/topic/5729/simple-python-solution-by-mutating-the-matrix
def spiral_order_1(matrix):
    result = []

    while matrix:
        result += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix:
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    return result


if __name__ == '__main__':
    matrix = [
              [ 1, 2, 3 ],
              [ 4, 5, 6 ],
              [ 7, 8, 9 ]
             ]

    print spiral_order(matrix)
    print('\n')
    print spiral_order_1(matrix)
