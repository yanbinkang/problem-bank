# def find_low_high_index(a_list, key):
#     indices = []

#     i = 0
#     while i < len(a_list):
#         if a_list[i] == key:
#             indices.append(i)
#         i += 1

#     if indices:
#         min_index = min(indices)
#         max_index = max(indices)
#         return "key: %s, Low: %s and High: %s" % (key, min_index, max_index)
#     else:
#         return -1
def find_low_index(arr, key):
    low = 0
    high = len(arr) - 1
    mid = high / 2

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if key <= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if arr[low] == key:
        return low

    return -1


def find_high_index(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if arr[high] == key:
        return high

    return -1


some_list = [1, 2, 2, 3, 5, 6, 7, 12, 23]
print find_low_index(some_list, 2)
print find_high_index(some_list, 2)
