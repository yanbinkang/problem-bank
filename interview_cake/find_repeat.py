def find_repeat(the_array):
    floor = 1
    ceiling = len(the_array) - 1

    while floor < ceiling:
        midpoint = floor + ((ceiling - floor) / 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        items_in_lower_range = 0
        for item in the_array:
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = lower_range_ceiling - lower_range_floor + 1

        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            floor, ceiling = upper_range_floor, upper_range_ceiling

    return floor


my_list = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
arr_2 = [1, 7, 4, 3, 2, 7, 4]
print  find_repeat(my_list)
print  find_repeat(arr_2)
