"""
https://leetcode.com/problems/number-of-islands-ii/#/description

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0

Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0

Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0

Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0

Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

algorithm: Every position is an new land (we make set which increases the number of sets by one) and we check its four neigbouring cells. If the new land connect two islands a and b, we combine them to form a whole (union - the number of disjoint sets reduces by one). The answer is then the number of the disjointed sets.
"""
from disjoint_set import *
def num_islands_2(m, n, positions):
    result = []

    grid = [[0 for i in range(n)] for j in range(m)]

    ds = DisjointSet()

    for i, j in positions:
        helper(grid, i, j, result, ds)

    return result

def helper(grid, i, j, result, ds):

    grid[i][j] = '1'

    cell = (i, j)

    ds.make_set(cell)

    # go up
    if i > 0 and grid[i - 1][j] == '1':
        ds.union(cell, (i - 1, j))

    # go down
    if i < len(grid) - 1 and grid[i + 1][j] == '1':
        ds.union(cell, (i + 1, j))

    # go left
    if j > 0 and grid[i][j - 1] == '1':
        ds.union(cell, (i, j - 1))

    #go right
    if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
        ds.union(cell, (i, j + 1))

    result.append(ds.num_sets)




if __name__ == '__main__':
    print num_islands_2(3, 3, [[0,0], [0,1], [1,2], [2,1]])
    print num_islands_2(1, 2, [[0,1], [0,0]])
    print num_islands_2(3, 3, [[0,1], [1,2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]])

