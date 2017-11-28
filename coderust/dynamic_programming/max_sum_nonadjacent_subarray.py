def find_max_sum_nonadjacent(a_list):
    if len(a_list) < 1:
        return -1
    elif len(a_list) == 1:
        return a_list[0]

    return max(even_indices_largest_sum_subsequence(a_list), odd_indices_largest_sum_subsequence(a_list))

def even_indices_largest_sum_subsequence(a_list):
    current_max = a_list[0]
    global_max = a_list[0]

    i = 2

    while i < len(a_list) - 1:
        if current_max < 0:
            current_max = a_list[i]
        else:
            current_max += a_list[i]

        if global_max < current_max:
            global_max = current_max

        i += 2

    return global_max

def odd_indices_largest_sum_subsequence(a_list):
    current_max = a_list[1]
    global_max = a_list[1]
    i = 3

    while i < len(a_list) - 1:
        if current_max < 0:
            current_max = a_list[i]
        else:
            current_max += a_list[i]

        if global_max < current_max:
            global_max = current_max

        i += 2
    return global_max

print find_max_sum_nonadjacent([1, 6, 10, 14, -5, -1, 2, -1, 3])
print find_max_sum_nonadjacent([1, -1, 6, -4, 2, 2])
