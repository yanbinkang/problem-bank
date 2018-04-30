"""
https://leetcode.com/problems/lonely-pixel-ii/?tab=Description#/description

Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels located at some specific row R and column C that align with all the following rules:

    1. Row R and column C both contain exactly N black pixels.

    2. For all rows that have a black pixel at column C, they should be exactly the same as row R

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.


Example:
Input:
[['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'B', 'W'],
 ['W', 'W', 'B', 'W', 'B', 'W']]

N = 3

Output: 6
Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
        0    1    2    3    4    5         column index
0    [['W', 'B', 'W', 'B', 'B', 'W'],
1     ['W', 'B', 'W', 'B', 'B', 'W'],
2     ['W', 'B', 'W', 'B', 'B', 'W'],
3     ['W', 'W', 'B', 'W', 'B', 'W']]
row index

Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels.
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.
"""
def find_black_pixel(picture, N):
    """
    :type picture: List[List[str]]
    :type N: int
    :rtype: int
    """
    n = len(picture)
    m = len(picture[0])
    count = 0

    row_count = [0 for _ in range(n)]
    col_count = [0 for _ in range(m)]

    for i in range(n):
        s = ''
        for j in range(m):
            if picture[i][j] == 'B':
                row_count[i] += 1
                col_count[j] += 1
            s += picture[i][j]


    print row_count
    print('\n')
    print col_count

    for i in range(n):
        for j in range(m):
            if picture[i][j] == 'B' and\
                row_count[i] == N and\
                col_count[j] == N and\
                row_count[i] == col_count[j]:
                    count += 1

    return count

if __name__ == '__main__':
    matrix = [['W', 'B', 'W', 'B', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'B', 'W'],
              ['W', 'B', 'W', 'B', 'B', 'W'],
              ['W', 'W', 'B', 'W', 'B', 'W']]

    matrix2 =  [['W', 'B', 'W', 'B', 'B', 'W'],
                ['B', 'W', 'B', 'W', 'W', 'B'],
                ['W', 'B', 'W', 'B', 'B', 'W'],
                ['B', 'W', 'B', 'W', 'W', 'B'],
                ['W', 'W', 'W', 'B', 'B', 'W'],
                ['B', 'W', 'B', 'W', 'W', 'B']]

    # print find_black_pixel(matrix, 3) #6
    print('\n')
    print find_black_pixel(matrix2, 3) #9
