"""
https://leetcode.com/problems/search-a-2d-matrix-ii/#/description

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.

- Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

ref: https://discuss.leetcode.com/topic/20064/my-concise-o-m-n-java-solution

algorithm:
We start search the matrix from top right corner, initialize the current position to top right corner, if the target is greater than the value in current position, then the target can not be in entire row of current position because the row is sorted, if the target is less than the value in current position, then the target can not in the entire column because the column is sorted too. We can rule out one row or one column each time, so the time complexity is O(m+n)
"""
def search_matrix(matrix, target):
    if not matrix or len(matrix) < 1 or len(matrix[0]) < 1: return False

    col = len(matrix[0]) - 1
    row = 0

    while col >=0 and row <= len(matrix) - 1:
        if target == matrix[row][col]:
            return True
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1

    return False


if __name__ == '__main__':
    matrix = [[1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]

    print search_matrix(matrix, 5)
    print('\n')
    print search_matrix(matrix, 20)
