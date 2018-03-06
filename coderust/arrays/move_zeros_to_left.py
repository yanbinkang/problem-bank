def move_zeros_to_left(a_list):
    insert_pos = len(a_list) - 1

    for i in reversed(range(len(a_list))):
        if a_list[i] != 0:
            a_list[insert_pos] = a_list[i]
            insert_pos -= 1

    while insert_pos >= 0:
        a_list[insert_pos] = 0
        insert_pos -= 1

    return a_list

print move_zeros_to_left([1, 10, 20, 0, 59, 63, 0, 88, 0])
