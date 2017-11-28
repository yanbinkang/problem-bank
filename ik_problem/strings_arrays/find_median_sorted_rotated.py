"""
1. Find value of minimum index element
2. Use formula
    a) index = ((idx_min + size/2) % size) to find median index and return element when list is even
    b) index = ((((idx_min + size/2) % size) + ((idx_min + size/2 + 1) % size)) // 2) to find median index and return element when list is odd
"""
def find_min_index(a_list):
    first = 0
    size = len(a_list)
    last = size - 1

    if last < first:
        return a_list.index(a_list[0])

    if last == first:
        return a_list.index(a_list[first])

    mid = (first + last) // 2

    if a_list[mid + 1] < a_list[mid]:
        return a_list.index(a_list[mid + 1])

    if a_list[mid] < a_list[mid - 1]:
        return a_list.index(a_list[mid])

    if a_list[last] > a_list[mid]:
        return find_min_index(a_list[:mid])

    return find_min_index(a_list[mid+1:])

def find_median(a_list):
    size = len(a_list)
    idx_min = find_min_index(a_list)

    if size % 2 != 0:
        index = (idx_min + size/2) % size
        return a_list[index]

    if size % 2 == 0:
        index = (((idx_min + size/2) % size) + ((idx_min + size/2 + 1) % size)) // 2
        return a_list[index]


arr_1 = [5, 1, 2, 3, 4]
arr_2 = [1, 2, 3, 4]
arr_3 = [2, 1]
a = [1, 2, 3, 4, 5, 6, 7]

print find_median(arr_2)
# print find_min_index(arr_1)
# print find_min_index(arr_2)
# print find_min_index(arr_3)
# print find_min_index(a)

