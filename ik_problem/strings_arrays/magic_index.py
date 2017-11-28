"""
Array A, sorted, distinct, arbitrary length

Find element which has the same index.

-1,0,1,3,5. Magic index is 3.
"""

def magic_index(a_list):
    first = 0
    last = len(a_list) - 1

    while first < last:
        mid_point = (first + last) // 2
        if a_list[mid_point] == mid_point:
            return mid_point
        elif mid_point > a_list[mid_point]:
            first = mid_point + 1
        else:
            last = mid_point - 1

print magic_index([-1, 0, 1, 3, 5])
