def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if a_list[mid_point] == item:
            return mid_point
        elif item < a_list[mid_point]:
            last = mid_point - 1
        else:
            first = mid_point + 1
    return -1

print binary_search([1, 10, 20, 47, 59, 63, 75, 88, 99], 20)
print binary_search([1, 10, 20, 47, 59, 63, 75, 88, 99], 100)
