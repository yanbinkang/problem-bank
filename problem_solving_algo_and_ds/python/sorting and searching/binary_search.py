def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        mid_point = (first + last) // 2
        if a_list[mid_point] == item:
            found = True
        else:
            if item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1

    return found
