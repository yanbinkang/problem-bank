def start_end_indices_largest_subarray(a_list):
    if len(a_list) < 1:
        return -1
    elif len(a_list) == 1:
        return a_list[0]

    current_max = a_list[0]
    global_max = a_list[0]
    start_index, end_index = (0, 0)

    i = 1
    while i < len(a_list) - 1:
        if current_max < 0:
            current_max = a_list[i]
            start_index = i
        else:
            current_max += a_list[i]

        if global_max < current_max:
            global_max = current_max
            end_index = i
        i += 1

    return [start_index, end_index]

print start_end_indices_largest_subarray([-4, 2, -5, 1, 2, 3, 6, -5, 1])
