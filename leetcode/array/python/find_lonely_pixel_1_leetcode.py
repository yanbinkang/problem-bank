"""
https://leetcode.com/problems/lonely-pixel-i/?tab=Description

Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input:
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.

Note:
The range of width and height of the input 2D array is [1,500].

O(nm) time O(n + m) space.
"""
def find_lonely_pixel(picture):
    n = len(picture)
    m = len(picture[0])

    row_count = [0 for _ in range(n)]
    col_count = [0 for _ in range(m)]

    count = 0

    for i in range(n):
        for j in range(m):
            if picture[i][j] == 'B':
                row_count[i] += 1
                col_count[j] += 1


    for i in range(n):
        for j in range(m):
            if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                count += 1

    return count

if __name__ == '__main__':
    picture =   [['W', 'W', 'B'],
                 ['W', 'B', 'W'],
                 ['B', 'W', 'W']]

    print find_lonely_pixel(picture)
