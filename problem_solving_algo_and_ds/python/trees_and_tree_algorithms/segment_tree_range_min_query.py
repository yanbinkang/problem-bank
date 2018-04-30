from sys import maxint

"""
ref: https://www.youtube.com/watch?v=ZBHKZF5w4YU
"""

def create_segment_tree(input):
    next_pow_of_two = next_power_of_2(len(input))

    segment_tree = [None] * (next_pow_of_two* 2 -1)

    for i in range(len(segment_tree)):
        segment_tree[i] = maxint

    construct_min_segment_tree(segment_tree, input, 0, len(input)-1, 0)

    return segment_tree

def mininum_query(segment_tree, qlow, qhigh, length):
    return range_min_query(segment_tree, 0, length-1, qlow, qhigh, 0)

def range_min_query(segment_tree, low, high, qlow, qhigh, pos):
    if qlow <= low and qhigh >= high:
        return segment_tree[pos]

    if qlow > high or qhigh < low:
        return maxint

    mid = (low + high) // 2

    return min(
        range_min_query(segment_tree, low, mid, qlow, qhigh, 2 * pos + 1),
        range_min_query(segment_tree, mid + 1, high, qlow, qhigh, 2 * pos + 2))

def construct_min_segment_tree(segment_tree, input, low, high, pos):
    if (low == high):
        segment_tree[pos] = input[low]
        return

    mid = (low + high) // 2

    construct_min_segment_tree(segment_tree, input, low, mid, 2 * pos + 1)
    construct_min_segment_tree(segment_tree, input, mid + 1, high, 2 * pos + 2)

    segment_tree[pos] = min(segment_tree[2 * pos + 1], segment_tree[2 * pos + 2])

"""
ref:http://www.geeksforgeeks.org/next-power-of-2/
"""
def next_power_of_2(num):
    p = 1
    if (num and not (num and (num-1))):
        return num

    while p < num:
        p <<= 1

    return p


if __name__ == '__main__':
    a_list = [0, 3, 4, 2, 1, 6, -1]
    seg_tree = create_segment_tree(a_list)

    print mininum_query(seg_tree, 0, 3, len(a_list))
    print mininum_query(seg_tree, 1, 5, len(a_list))
    print mininum_query(seg_tree, 1, 6, len(a_list))
