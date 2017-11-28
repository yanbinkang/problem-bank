def smallest_common_number(list_1, list_2, list_3):
    common_numbers = []
    for num in list_1:
        if num  in list_2 and num in list_3:
            common_numbers.append(num)
    if common_numbers:
        return min(common_numbers)
    else:
        return None

list_one = [6, 7, 10, 25, 30, 63, 64]
list_two = [-1, 4, 5, 6, 7, 8, 50]
list_three = [1, 6, 10, 14, 7]

print smallest_common_number(list_one, list_two, list_three)
