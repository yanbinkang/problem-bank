"""
https://leetcode.com/problems/search-a-2d-matrix/#/description

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

O(log(m) + log(n)), or in other words, O(log(mn))

solution: https://discuss.leetcode.com/topic/10211/a-python-binary-search-solution-o-logn
"""

# Consider the matrix as a sorted array and apply the normal binary search
def search_matrix(matrix, target):
    if len(matrix) == 0 or len(matrix[0]) == 0: return False

    rows = len(matrix)
    cols = len(matrix[0])

    low = 0; high = rows * cols - 1

    while low <= high:
        mid = low + ((high - low) // 2)

        mid_value = matrix[mid / cols][mid % cols]

        if mid_value == target:
            return True
        elif target < mid_value:
            high = mid - 1
        else:
            low = mid + 1

    return False

# iterate through each row and do binary search
def search_matrix_2(matrix, target):
    n = len(matrix)

    for i in range(n):
        if find_target(matrix[i], target):
            return True

    return False

def find_target(a_list, target):
    first, last = 0, len(a_list) - 1


    while first <= last:
        mid = first + ((last - first) // 2)

        if a_list[mid] == target:
            return True
        elif target < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return False

if __name__ == '__main__':
    matrix = [[1,   3,  5,  7],
              [10, 11, 16, 20],
              [23, 30, 34, 50]]

    matrix2 = [[1]]

    matrix3 = [[1,3]]

    print search_matrix(matrix, 3)
    print('\n')
    print search_matrix(matrix2, 1)
    print('\n')
    print search_matrix(matrix3, 3)

    print('\n')

    print search_matrix_2(matrix, 3)
    print('\n')
    print search_matrix_2(matrix2, 1)
    print('\n')
    print search_matrix_2(matrix3, 3)
