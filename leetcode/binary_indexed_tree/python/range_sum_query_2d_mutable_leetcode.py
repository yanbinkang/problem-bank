"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10

Note:

    1) The matrix is only modifiable by the update function.

    2)You may assume the number of calls to update and sumRegion function is distributed evenly.

    3)You may assume that row1 <= row2 and col1 <= col2.

TIME COMPLEXITY:
    1) Initialize the BIT takes: O(mn * logm * logn)
    2) Both update() and prefix_sum() takes: O(logm * logn)
"""
class Fenwick2D(object):
    def __init__(self, matrix):
        if not matrix: return

        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.matrix = [[0 for i in range(self.cols)] for j in range(self.rows)]

        self.tree = [[0 for i in range(self.cols + 1)] for j in range(self.rows + 1)]

        for i in range(self.rows):
            for j in range(self.cols):
                self.update(i, j, matrix[i][j])

    def get_parent(self, child):
        return (child - (child & -child))

    def get_next(self, index):
        return (index + (index & -index))

    def update(self, row, col, item):
        current = self.matrix[row][col]
        self.matrix[row][col] = item
        item = item - current

        row += 1
        col += 1

        while i <= self.rows:
            j = col
            while j <= self.cols:
                self.tree[i][j] += item

                j += j & -j    # same as: j = self.get_next(j)
            i += i & -i        # same as: i = self.get_next(i)

    def prefix_sum(self, row, col):
        total = 0

        i = row + 1

        while i > 0:
            j = col + 1
            while j > 0:
                total += self.tree[i][j]
                j -= j & -j   # same as: j = self.get_parent(j)
            i -= i & -i       # same as: i = self.get_parent(i)

        return total

    def range_sum(self, row1, col1, row2, col2):
        return self.prefix_sum(row2, col2) +\
                self.prefix_sum(row1 - 1, col1 - 1) -\
                self.prefix_sum(row1 - 1, col2) -\
                self.prefix_sum(row2, col1 - 1)

        """
        [
          [None, None, None, None, None, None],
          [None, None, None, None, None, None],
          [None,  B  , None, None,  C  , None],
          [None, None, None, None, None, None],
          [None,  D  , None, None,  A  , None],
          [None,  D  , None, None,  A  , None]
        ]

        (A + B) - (C - D) or A + B - C + D
        """


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.bit = Fenwick2D(matrix)



    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.bit.update(row, col, val)



    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.bit.range_sum(row1, col1, row2, col2)



if __name__ == '__main__':
    matrix = [
              [3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]
            ]

    tree = NumMatrix(matrix)
    print tree.sumRegion(2, 1, 4, 3) # -> 8
    tree.update(3, 2, 2)
    print tree.sumRegion(2, 1, 4, 3) # -> 10
