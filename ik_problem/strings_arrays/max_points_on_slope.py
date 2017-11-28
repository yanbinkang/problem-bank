# solution: http://yucoding.blogspot.com.br/2013/12/leetcode-question-max-points-on-line.html

def max_points(points):
    if len(points) <= 2:
        return len(points)

    maximum_points = 0 # result value
    for i in range(len(points)):
        d = {}
        dup = 1
        for j in range(len(points)):
            if (points[i][0] == points[j][0]) and points[i][1] == points[j][1] and i  != j:
                dup += 1
            elif i != j:
                if points[i][0] == points[j][0]: # vertical line
                    d['v'] = d.get('v', 0) + 1
                elif points[i][1] == points[j][1]: # horizontal line
                    d['h'] = d.get('h', 0) + 1
                else: # regular slope
                    slope = 1.0 * (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                    d[slope] = d.get(slope, 0) + 1
        if len(d) > 0:
            maximum_points = max(maximum_points, max(d.values()) + dup)
        else: # all points are duplicates, d is empty
            maximum_points = max(maximum_points, dup)
    return maximum_points

input = [[1, 0], [1, 2], [1, 3], [1, 7], [2, 6], [10, 0], [8, 1], [9, 1]]
print max_points(input)

print max_points([[0, 0], [1, 1], [1, -1]])

"""
alternative solution

def max_points(points):
    if len(points) <= 2:
        return len(points)

    maximum_points = 0

    prev_x, prev_y = points[0]
    d = {}
    dup = 1

    for curr_x, curr_y in points[1:]:

        if prev_x == curr_x and prev_y == curr_y:
            dup += 1
        else:
            if prev_x == curr_x: # vertical line
                d['v'] = d.get('v', 0) + 1
            elif prev_y == curr_y: # horizontal line
                d['h'] = d.get('h', 0) + 1
            else:
                slope = 1.0 * (prev_y - curr_y) / (prev_x - curr_x)
                d[slope] = d.get(slope, 0) + 1

        prev_x, prev_y = curr_x, curr_y

    if len(d) > 0:
        maximum_points = max(maximum_points, max(d.values()) + dup)
    else:
        maximum_points = max(maximum_points, dup)

    return maximum_points



input = [(1, 0), (1, 2), (1, 3), (1, 7), (2, 6), (10, 0), (8, 1), (9, 1)]

print max_points(input)

"""

