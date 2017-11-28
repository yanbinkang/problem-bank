"""
https://leetcode.com/problems/number-of-islands/#/description

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
11110
11010
11000
00000

Answer: 1

Example 2:
11000
11000
00100
00011

Answer: 3
"""

"""
Use disjoint sets.

If grid value is 0 continue. Else save the cell value in a tuple and make set with the cell. Then append each cell to cells array. Now for each grid value of 1, go left and up and check if these grid values are also 1. If so union these two cells.

Declare a dict. Iterate over each cell in cells and find its set representative. Make the set rep the key and append its children.

The answer is the number of set reps we can find. This will be the length of the dict's keys.

Alternate better solution: everytime we see land, we make a set. then we check left and up. If the new land connects another land, we combine them (union). Make set increases number of sets by one. And union decreases the number of sets by one. The answer is then the number of the disjointed sets
"""
from disjoint_set import *
# from collections import defaultdict
def num_islands_union_find(grid):
    ds = DisjointSet()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '0':
                continue

            cell = (i, j)

            ds.make_set(cell)

            # when cells are connected they are undirected so we can just go left and up.

            # go left
            if j > 0  and grid[i][j - 1] == '1':
                ds.union(cell, (i, j - 1))

            # go up
            if i > 0 and grid[i - 1][j] == '1':
                ds.union(cell, (i - 1, j))

            # you can also do right and down. you just need to make a set out of all the 1's in the grid before.
    return ds.num_sets


"""
https://discuss.leetcode.com/topic/13248/very-concise-java-ac-solution

DFS

very similar to word search backtracking problem. For each cell, go up, down, left and right.

Marks the given site as visited, then checks adjacent sites.

Or, Marks the given site as water, if land, then checks adjacent sites.

Or, Given one coordinate (i,j) of an island, obliterates the island from the given grid, so that it is not counted again.

O(MN) time and space
"""
def num_islands(grid):
    count = 0

    if len(grid) == 0: return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs_marking(grid, i, j)
                count += 1

    return count

def dfs_marking(grid, i, j):
    # Check for invalid indices and for sites that aren't land
    if i < 0 or j < 0 or\
        i >= len(grid) or j >= len(grid[0]) or\
            grid[i][j] != '1':
                return

    # Mark the site as visited
    grid[i][j] = '0'

    dfs_marking(grid, i + 1, j)
    dfs_marking(grid, i - 1, j)
    dfs_marking(grid, i, j + 1)
    dfs_marking(grid, i, j - 1)

"""
BFS
"""


if __name__ == '__main__':
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]

    grid_1 = [['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '1']]

    grid_2 = [['1', '1', '0', '0', '0'],
              ['0', '1', '0', '0', '1'],
              ['1', '0', '0', '1', '1'],
              ['0', '0', '0', '0', '0'],
              ['1', '0', '1', '0', '1']]

    grid_3 = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]

    grid_4 = [['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '1']]

    grid_5 = [['1', '1', '0', '0', '0'],
              ['0', '1', '0', '0', '1'],
              ['1', '0', '0', '1', '1'],
              ['0', '0', '0', '0', '0'],
              ['1', '0', '1', '0', '1']]


    print num_islands(grid)
    print('\n')
    print num_islands(grid_1)
    print('\n')
    print num_islands(grid_2)
    print('\n')
    print num_islands_union_find(grid_3) #1
    print('\n')
    print num_islands_union_find(grid_4) #3
    print('\n')
    print num_islands_union_find(grid_5) #6



