"""
https://leetcode.com/problems/island-perimeter/

https://discuss.leetcode.com/topic/68786/clear-and-easy-java-solution

https://discuss.leetcode.com/topic/68872/dfs-hashtable-are-you-kidding-me-java-one-pass-simpled-solution

https://discuss.leetcode.com/topic/68845/c-solution-with-explanation

O(n^2)
"""
def island_perimeter(grid):
    islands, neighbors = 0, 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                islands += 1

                # check right and down neighbors
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    neighbors += 1
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    neighbors += 1

    return (islands * 4) - (neighbors * 2)

# dfs
def island_perimeter_dfs(grid):
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4

                # check left and top neighbors
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter


if __name__ == '__main__':
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]

    print island_perimeter(grid)
    print('\n')
    print island_perimeter_dfs(grid)
