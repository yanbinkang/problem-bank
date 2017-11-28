def merge_arrays(my_array, alices_array):
    result = [None] * (len(my_array) + len(alices_array))

    i= 0
    j = 0
    k = 0

    while i < len(my_array) and j < len(alices_array):
        if my_array[i] < alices_array[j]:
            result[k] = my_array[i]
            i = i + 1
        else:
            result[k] = alices_array[j]
            j = j + 1
        k = k + 1

    while i < len(my_array):
        result[k] = my_array[i]
        i = i + 1
        k = k + 1

    while j < len(alices_array):
        result[k] = alices_array[j]
        j = j + 1
        k = k + 1

    return result

my_array = [3, 4, 6, 10, 11, 15]
alices_array = [1, 5, 8, 12, 14, 19]

print(merge_arrays(my_array, alices_array))
