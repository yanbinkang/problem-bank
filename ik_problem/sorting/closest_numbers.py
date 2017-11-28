def closest_numbers(a_list):
    hash_map = {}
    res = []
    i = 1
    a_list.sort()
    while i < len(a_list):
        diff = a_list[i] - a_list[i - 1]
        hash_map[(a_list[i-1], a_list[i])] = diff

        i += 1

    min_diff = min(hash_map.values())
    for k, v in hash_map.items():
        if v == min_diff:
            res.extend(list(k))
    res.sort()

    for elem in res:
        print(elem),
    print("\n")


inp_1 = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]

inp_2 = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]

inp_3 = [5, 4, 3, 2]

closest_numbers(inp_1)
closest_numbers(inp_2)
closest_numbers(inp_3)
