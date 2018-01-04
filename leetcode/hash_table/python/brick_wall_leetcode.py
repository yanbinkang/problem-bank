"""
https://leetcode.com/problems/brick-wall/#/description

There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:
Input:
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2

Explanation: CHECK FROM URL

solution:
https://discuss.leetcode.com/topic/86151/i-don-t-think-there-is-a-better-person-than-me-to-answer-this-question

We want to cut from the edge of the most common location among all the levels, hence using a map to record the locations and their corresponding occurrence
"""
def least_bricks(wall):
    if len(wall) == 0: return 0
    count = 0

    dic = {}

    for row in wall:
        length = 0
        for i in range(len(row) - 1):
            length += row[i]
            dic[length] = dic.get(length, 0) + 1
            count = max(count, dic.get(length))

    return len(wall) - count

if __name__ == '__main__':
    wall = [[1,2,2,1],
             [3,1,2],
             [1,3,2],
             [2,4],
             [3,1,2],
             [1,3,1,1]]
    print least_bricks(wall)
