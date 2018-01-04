"""
https://leetcode.com/problems/number-of-boomerangs/

Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
import math
def number_of_boomerangs(points):
    result = 0

    for i in range(len(points)):
        hash_map = {}

        for j in range(len(points)):
            if i != j:
                dt = pow(points[i][0] - points[j][0], 2) + pow(points[i][1] - points[j][1], 2)

                result += hash_map.get(dt, 0)
                hash_map[dt] = hash_map.get(dt, 0) + 1


    return result * 2

def find_distance(x, y):
    return pow(x[0] - y[0], 2) + pow(x[1] - y[1], 2)

def number_of_boomerangs_1(points):
    hash_map = {}
    result = 0

    for i in range(len(points)):
        for j in range(len(points)):
            if i != j:
                dist = find_distance(points[i], points[j])

                hash_map[dist] = hash_map.get(dist, 0) + 1

        for value in hash_map.values():
            result += value * (value - 1)

        hash_map.clear()

    return result

if __name__ == '__main__':
    # print find_distance([4, 6], [1, 2])
    print number_of_boomerangs([[0,0],[1,0],[2,0]])
    print number_of_boomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
    print('\n')
    print number_of_boomerangs_1([[0,0],[1,0],[2,0]]s)
    print number_of_boomerangs_1([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
