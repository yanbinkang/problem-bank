from math import sqrt
from sys import maxint

"""
Given coordinates of points find closest pair points distance.
https://www.youtube.com/watch?v=_pSl90jq-m0
"""

# utility function to find distance between two points
def dist(p1, p2):
    return sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) +
                (p1[1] - p2[1]) * (p1[1] - p2[1])
                )


# a brute force method to return the smallest distance between two points
def brute_force(points):
    n = len(points)
    min_val = maxint
    for i in range(n):
        for j in range(i+1, n):
            dist_calculated = dist(points[i], points[j])
            # print dist_calculated
            if dist_calculated < min_val:
                min_val = dist_calculated

    return min_val

"""
A utility function to find the distance between the closeset points of strip of given size. All points in strip are sorted according to y coordinates. They all have upper bound of minimum distance as d.
Note that this methid seems to be O(n^2) method, but it's a O(n) method as the inner method rns at least 6 times.
"""
def strip_closest(strip_points, d):
    min_dist = d

    size = len(strip_points)
    _strip_points = sorted(strip_points, key=lambda x:x[1])

    i = 0
    while i < size:
        j = i + 1
        while j < size and _strip_points[j][1] - _strip_points[i][1] < min_dist:
            dist_calculated = dist(_strip_points[i], _strip_points[j])
            print dist_calculated
            if dist_calculated < min_dist:
                min_dist = dist_calculated
            j += 1
        i += 1

    return min_dist

"""
a recursive function to find the smallest distance. The array points contains all points sorted according to x coordinates
"""
def closeset_util(points):
    n = len(points)
    if n <= 3:
        return brute_force(points)

    # find the middle point
    mid = n // 2
    mid_point = points[mid]

    # consider the vertical line passing through the middle point
    # calculate the smallest distance dl on left of middle point and dr on right of middle point
    dl = closeset_util(points[:mid])
    dr = closeset_util(points[mid:])

    d = min(dl, dr)

    #build an array strip that contains points close (closer than d) to the line passing though the middle point
    strip = []
    for i in range(n):
        if abs(points[i][0] - mid_point[0]) < d:
            strip.append(points[i])

    res = strip_closest(strip, d)

    return min(d, res)

# main function
def closest(points):
    sorted_points = sorted(points, key=lambda x:x[0])

    return closeset_util(sorted_points)

if __name__ == '__main__':
    given_points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]

    print "The smallest distance is %s " % closest(given_points)
