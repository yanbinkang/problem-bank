def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list)-1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point-1)
        quick_sort_helper(a_list, split_point+1, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last

    stop = False

    while not stop:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark += 1

        while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            stop = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp

    return right_mark

my_list = [55, 23, 26, 2, 25]
quick_sort(my_list)
print my_list
