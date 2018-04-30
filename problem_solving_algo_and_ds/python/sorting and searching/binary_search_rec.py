def binary_search(a_list, item):
    # end = len(a_list) - 1
    if len(a_list) == 0:
        return False
    else:
        mid_point = len(a_list) // 2
        if a_list[mid_point] == item:
            return True
        else:
            if item < a_list[mid_point]:
                # slice is O(k). Uncomment to achieve logn
                # mid_point = mid_point - 1
                # return binary_search(a_list[0:mid_point], item)
                return binary_search(a_list[:mid_point], item)
            else:
                # mid_point = mid_point + 1
                # return binary_search(a_list[mid_point:end], item)
                return binary_search(a_list[mid_point+1:], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
