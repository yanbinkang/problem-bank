"""
https://leetcode.com/problems/pascals-triangle/#/description

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

solution: https://discuss.leetcode.com/topic/10131/a-simple-python-solution/2

explanation: using example generate(5) initially the result_set is

[
         [1],
        [1, 1],
      [1, 1, 1],
    [1, 1, 1, 1],
   [1, 1, 1, 1, 1]
]

the first two rows stay the same. Starting from the 3rd row, the first and last values in that row do not change (are always 1). The numbers between are changed based on the row above with the formular:

result_set[i][j] = result_set[i - 1][j - 1] + result_set[i - 1][j]

For example:

result_set[3][1] = result_set[2][0] + result_set[2][1]

result_set[3][2] = result_set[2][1] + result_set[2][2]

[1, 2, 1] = > [1, 3, 3, 1]
"""
def generate(num_rows):
    result_set = [[1] * (i + 1) for i in range(num_rows)]

    """
    we start from 1 in each iteration because we dont care about index 0 when generating the pascals-triangle. IT'S ALWAYS 1!
    """
    for i in range(1, num_rows):
        """
        If i = 2, we'll start updating from index 1. If i = 3, we'll start updating from index 2 etc. WE DON'T CARE ABOUT THE INDEX i IS ON BECAUSE ITS ALWAYS 1!
        """
        for j in range(1, i):
            result_set[i][j] = result_set[i - 1][j - 1] + result_set[i - 1][j]

    return result_set

if __name__ == '__main__':
    print generate(5)
