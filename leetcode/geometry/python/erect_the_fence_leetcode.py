"""
https://leetcode.com/problems/erect-the-fence/description/

There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

algo: use Jarvis March Convex Hull

Convex hull or convex envelope of a set X of points in the Euclidean plane or in a Euclidean space
 (or, more generally, in an affine space over the reals) is the smallest convex set that contains X.

 Jarvis March is finding convex or gift wrapping algorithm.

 Time complexity O(nh)
    n - number of points
    h - number of points on the boundary.
    Worst case O(n^2)

 Space complexity O(n^2)

 Reference
 https://leetcode.com/problems/erect-the-fence/description/
 https://en.wikipedia.org/wiki/Convex_hull
 https://en.wikipedia.org/wiki/Gift_wrapping_algorithm
"""
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return str([self.x , self.y])

    def __repr__(self):
        return self.__str__()

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        start = points[0]

        for i in range(1, len(points)):
            if points[i].x < start.x:
                start = points[i]

        current = start

        # use set because this algorithm might try to insert duplicate points
        result = set()
        result.add(start)

        collinear_points = []

        while True:
            next_target = points[0]

            for i in range(1, len(points)):
                if points[i] == current:
                    continue

                val = self.crossProduct(current, next_target, points[i])

                """
                if val > 0 it means points[i] is on left of current -> nextTarget. Make him the nextTarget.
                """

                if val > 0:
                    next_target = points[i]
                    # reset collinear points because we now have a new nextTarget.
                    collinear_points = []
                elif val == 0:
                    """
                    if val is 0 then collinear current, nextTarget and points[i] are collinear.
                    if its collinear point then pick the further one but add closer one to list of collinear points.
                    """
                    if self.distance(current, next_target, points[i]) < 0:
                        collinear_points.append(next_target)
                        next_target = points[i]
                    else:
                        """
                        just add points[i] to collinearPoints list. If nextTarget indeed is the next point on
                        convex then all points in collinear points will be also on boundary.
                        """
                        collinear_points.append(points[i])

            # add all points in collinear_points to result
            for p in collinear_points:
                result.add(p)

            # if nextTarget is same as start it means we have formed an envelope and its done.
            if next_target == start:
                break

            # add next_target to result and set current to next_target
            result.add(next_target)
            current = next_target


        return list(result)

    def distance(self, a, b, c):
        y1 = a.y - b.y
        y2 = a.y - c.y
        x1 = a.x - b.x
        x2 = a.x - c.x

        # read about cmp: http://bit.ly/2ymqO49
        return cmp(y1 * y1 + x1 * x1, y2 * y2 + x2 * x2)

    def crossProduct(self, a, b, c):
        y1 = a.y - b.y
        y2 = a.y - c.y
        x1 = a.x - b.x
        x2 = a.x - c.x

        return (y2 * x1) - (y1 * x2)

if __name__ == '__main__':
    points1 = [Point(1,2), Point(2,2), Point(4,2)]
    points2 = [Point(1, 1), Point(2, 2), Point(2, 0), Point(2, 4), Point(3, 3), Point(4, 2)]
    s = Solution()
    print s.outerTrees(points1)
    print('\n')
    print s.outerTrees(points2)
