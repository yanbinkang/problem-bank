"""
solution: http://www.geeksforgeeks.org/maximum-difference-between-two-elements/
"""
def max_diff(a_list):
    n = len(a_list)
    max_dif = a_list[1] - a_list[0]
    min_element = a_list[0]

    i = 1
    while i < n:
        if a_list[i] - min_element > max_dif:
            max_dif = a_list[i] - min_element
        if a_list[i] < min_element:
            min_element = a_list[i]

        i += 1

    if max_diff > 0:
        return max_dif

    return -1


print max_diff([2, 3, 10, 2, 4, 8, 1])
print max_diff([7, 9, 5, 6, 3, 2])
