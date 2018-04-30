"""
https://leetcode.com/problems/the-skyline-problem/#/description

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B)


The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment.

IMPORTANT!!!!

Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height.


Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

    * The number of buildings in any input list is guaranteed to be in the range [0, 10000].

    * The input list is already sorted in ascending order by the left x position Li.

    * The output list must be sorted by the x position.

    * There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

solution: https://leetcode.com/discuss/37444/my-220ms-divide-and-conquer-solution-in-python-o-nlogn
"""

"""
If there is a strip in the result that already has the same height as the current strip we're trying to add, we skip the current strip. In the code, this is handled by doing:

        if result == [] or result[-1][1] != strip[1]:
            result.append(strip)

Also, given input: [[1, 5, 11]]

ouput is: [[1, 11], [5, 0]]. Can someone explain how [5, 0] is in the answer?

The output points are used to define a skyline. [5, 0] is part of the output because immediately after 5, the height drops to 0 and the skyline ends.
"""
def get_skyline(buildings):
    if len(buildings) == 0:
        return []

    if len(buildings) == 1:
        return [ [ buildings[0][0], buildings[0][2] ],
                  [buildings[0][1], 0]
                ]

    mid = len(buildings) // 2

    left_half = buildings[:mid]
    right_half = buildings[mid:]

    left = get_skyline(left_half)
    right = get_skyline(right_half)

    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    h1, h2 = None, None
    result = []

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x1 = left[i][0]
            h1 = left[i][1]
            new = [x1, max(h1, h2)]

            if result == [] or result[-1][1] != new[1]:
                result.append(new)
            i += 1
        elif left[i][0] > right[j][0]:
            x2 = right[j][0]
            h2 = right[j][1]
            new = [x2, max(h1, h2)]

            if result == [] or result[-1][1] != new[1]:
                result.append(new)
            j += 1
        else:
            """
            equal Li points, get max of the heights involved and just pick one Li point
            eg. see this example [[0, 2, 3], [2, 5, 3]]
            => left = [0, 3], [2, 0]
            => right = [2, 3], [5, 0]

            => [0, 3], [5, 0]
            """
            h1 = left[i][1]
            h2 = right[j][1]
            new = [right[j][0], max(h1, h2)]

            if result == [] or result[-1][1] != new[1]:
                result.append(new)
            i += 1
            j += 1

    # more elements in right added to result. Just add the rest of left
    while i < len(left):
        if result == [] or result[-1][1] != left[i][1]:
            result.append(left[i])
        i += 1

    # more elements in left added to result. Just add the rest of right
    while j < len(right):
        if result == [] or result[-1][1] != right[j][1]:
            result.append(right[j])
        j += 1

    return result

if __name__ == '__main__':
    print get_skyline([ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])
    print get_skyline([ [0, 2, 3], [2, 5, 3] ])
