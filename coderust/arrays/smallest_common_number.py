def smallest_common_number(a, b, c):
    i, j, k= 0, 0, 0

    while i < len(a) and j < len(b) and k < len(c):
        # found the smallest common number
        if a[i] == b[j] and b[j] == c[k]:
            return a[i]

        if a[i] <= b[j] and a[i] <= c[k]:
            i += 1
        elif b[j] <= a[i] and b[j] <= c[k]:
            j += 1
        elif c[k] <= a[i] and c[k] <= b[j]:
            k += 1

    return -1

def smallest_common_number_1(list_1, list_2, list_3):
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

print smallest_common_number_1(list_one, list_two, list_three)
print smallest_common_number(list_one, list_two, list_three)
