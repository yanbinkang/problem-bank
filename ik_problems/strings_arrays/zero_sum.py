def zero_sum(a_list):
    h = {}
    total = 0
    res = []
    i = 0

    while i < len(a_list):
        total += a_list[i]

        if total in h.keys():
            sub_set = a_list[h[total]+1:i+1]
            res.append(sub_set)
            if len(sub_set) > 2 and 0 in sub_set:
                res.append(sub_set[sub_set.index(0)+1:])
        else:
            h[total] = i

        i += 1

    if res:
        for sub in res:
            print sub



arr_1 = [6, 0, 1, 2, 3, 4, -10]
arr_2 = [1, 0]
arr_3 = [4, 0, 1, 2, -3]
arr_4 = [3, 1, 2, 3]

zero_sum(arr_1)
zero_sum(arr_2)
zero_sum(arr_3)
zero_sum(arr_4)
