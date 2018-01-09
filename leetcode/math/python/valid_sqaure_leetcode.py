"""
https://leetcode.com/problems/valid-square/#/description

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

    1 .All the input integers are in the range [-10000, 10000].
    2. A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    3. Input points have no order.

https://discuss.leetcode.com/topic/89985/c-3-lines-unordered_set

solution: If we calculate all distances between 4 points, 4 smaller distances should be equal (sides), and 2 larger distances should be equal too (diagonals). As an optimization, we can compare squares of the distances, so we do not have to deal with the square root and precision loss.

Therefore, our set will only contain 2 unique distances in case of square (beware of the zero distance though).

NB: Since we have only 4 points combination of all distances is:

list(itertools.combinations(range(1, 5) , 2))

# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

where 1, 2, 3, 4 are p1, p2, p3, p4 respectively!
"""
def validSquare(p1, p2, p3, p4):

    s = set( [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)] )

    return not list(s).count(0) and len(s) == 2

def dist(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

if __name__ == '__main__':
    print validSquare([0, 0], [1, 1], [1, 0], [0, 1])
    print validSquare([0, 0], [1, 1], [1, 0], [1, 1])
