def merge_sort(a_list):
    if len(a_list) > 1:
        mid_point = len(a_list) // 2
        left_half = a_list[:mid_point]
        right_half = a_list[mid_point:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1

    return a_list

print merge_sort([0, -1, -2, 5, 4])
print merge_sort([17, -50, 21, 500, -10000, 17, 0])
print merge_sort([0, -1, -2, 5, 4])
