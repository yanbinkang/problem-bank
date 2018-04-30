"""
https://leetcode.com/problems/rotate-image/#/description

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

https://discuss.leetcode.com/topic/6796/a-common-method-to-rotate-the-image

  clockwise rotate
  first reverse up to down, then swap the symmetry indices

  [ symmetry indices are (0, 0); (0, 1) and (1, 0); (0, 2) and (2, 0); (2, 2); (1, 2) and (2, 1); (1, 3) and (3, 1) etc ]. Notice the pattern? Symmetry points become exactly like the other if you flip it.

  1 2 3     7 8 9     7 4 1
  4 5 6  => 4 5 6  => 8 5 2
  7 8 9     1 2 3     9 6 3
"""
def rotate(matrix):
    start = 0; end = len(matrix) - 1

    # matrix.reverse()
    while start < end:
        temp = matrix[start]
        matrix[start] = matrix[end]
        matrix[end] = temp

        start += 1
        end -= 1

    for i in range(len(matrix)):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

"""
anticlockwise rotate
  first reverse left to right, then swap the symmetry. i.e for every row, reverse the element in the row, then swap the symmetry
  1 2 3     3 2 1     3 6 9
  4 5 6  => 6 5 4  => 2 5 8
  7 8 9     9 8 7     1 4 7
"""
def anti_rotate(matrix):
    for i in range(len(matrix)):
        # matrix[i].reverse()
        start = 0; end = len(matrix[0]) - 1
        while start < end:
            temp = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = temp

            start += 1
            end -= 1

    for i in range(len(matrix)):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


if __name__ == '__main__':
    matrix = [['X', 'X', 'O'],
              ['X', 'X', 'O'],
              ['O', 'O', 'O']]

    print('before rotate matrix is %s') % matrix
    rotate(matrix)
    print('\n')
    print('after rotate matrix is %s') % matrix

    # print('\n')

    # matrix2 = [[1, 2],
    #            [3, 4]]

    # print('before rotate matrix2 is %s') % matrix2
    # rotate(matrix2)
    # print('\n')
    # print('after rotate matrix2 is %s') % matrix2

    # print('\n')
    # matrix3 = [[1, 2, 3],
    #            [4, 5, 6],
    #            [7, 8, 9]]

    # print('before rotate matrix3 is %s') % matrix3
    # rotate(matrix3)
    # print('\n')
    # print('after rotate matrix3 is %s') % matrix3

    # print('\n')
    # matrix4 = [[1, 2, 3],
    #            [4, 5, 6],
    #            [7, 8, 9]]

    # print('before rotate matrix4 is %s') % matrix4
    # anti_rotate(matrix4)
    # print('\n')
    # print('after rotate matrix4 is %s') % matrix4
