"""
https://leetcode.com/problems/max-points-on-a-line/

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

ref: http://yucoding.blogspot.com.br/2013/12/leetcode-question-max-points-on-line.html

O(n ^ 2) time
"""
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def max_points(points):
    if len(points) <= 2:
        return len(points)

    maximum_points = 0

    for i in range(len(points)):
        points_hash = {}
        dup = 1

        for j in range(len(points)):
            # duplicate
            if points[i].x == points[j].x and\
               points[i].y == points[j].y and\
               i != j:
                    dup += 1
            elif i != j:
                if points[i].x == points[j].x: # vertical line
                    points_hash['v'] = points_hash.get('v', 0) + 1
                elif points[i].y == points[j].y: # horizontal line
                    points_hash['h'] = points_hash.get('h', 0) + 1
                else:
                    slope = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    points_hash[slope] = points_hash.get(slope, 0) + 1


        if len(points_hash) > 0:
            maximum_points = max(maximum_points, max(points_hash.values()) + dup)
        else: # all points are duplicates, points_hash is empty
            maximum_points = max(maximum_points, dup)

    return maximum_points

if __name__ == '__main__':
    points = [Point(1, 0), Point(1, 2), Point(1, 3), Point(1, 7), Point(2, 6), Point(10, 0), Point(8, 1), Point(9, 1)]
    points_2 = [Point(0, 0), Point(1, 1), Point(1, -1)]
    points3 = [Point(0, 0), Point(94911151, 94911150), Point(94911152, 94911151)]

    print max_points(points)
    print('\n')
    print max_points(points_2)
    print('\n')
    print max_points(points3) # fix me!
