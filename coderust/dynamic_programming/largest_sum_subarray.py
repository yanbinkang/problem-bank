def largest_sum_subarray(a_list):
    if len(a_list) < 1:
        return -1
    elif len(a_list) == 1:
        return a_list[0]

    global_sum = a_list[0]
    current_sum = a_list[0]

    i = 1
    while i < len(a_list) - 1:
        if current_sum < 0:
            current_sum = a_list[i]
        else:
            current_sum += a_list[i]

        if global_sum < current_sum:
            global_sum = current_sum
        i += 1


    return global_sum

print largest_sum_subarray([-4, 2, -5, 1, 2, 3, 6, -5, 1])
