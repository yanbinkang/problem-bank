# solution: http://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/

# alternative solution: https://leetcode.com/discuss/37444/my-220ms-divide-and-conquer-solution-in-python-o-nlogn
def find_skyline(a_skyline):
    # base case
    if a_skyline == []:
        return []

    # base case
    if len(a_skyline) == 1:
        return [(a_skyline[0][0], a_skyline[0][1]), (a_skyline[0][2], 0)]

    mid = len(a_skyline) // 2
    left_half = a_skyline[:mid]
    right_half = a_skyline[mid:]

    left = find_skyline(left_half)
    right = find_skyline(right_half)

    return merge(left, right)

def merge(left, right):
    res = []
    h1 = None
    h2 = None
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x1 = left[i][0]
            h1 = left[i][1]
            new = (x1, max(h1, h2))

            # check for redundant strip, a strip is redundant if it has same height or left as previous
            if res == [] or res[-1][1] != new[1]:
                res.append(new)
            i += 1
        else:
            x2 = right[j][0]
            h2 = right[j][1]
            new = (x2, max(h1, h2))

            if res == [] or res[-1][1] != new[1]:
                res.append(new)
            j += 1


    while i < len(left):
        if res == [] or res[-1][1] != left[i][1]:
            res.append(left[i])
        i += 1

    while j < len(right):
        if res == [] or res[-1][1] != right[j][1]:
            res.append(right[j])
        j += 1

    return res

s_line = [(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25), (19, 18, 22), (23, 13, 29), (24, 4, 28)]

# s_line = [(1, 11, 5)]

print find_skyline(s_line)
