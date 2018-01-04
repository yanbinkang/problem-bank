"""
You are given an array and two elements, find the minimum distance between the elements in the array. The array may have duplicates.
For example, if the array is (1, 5, 3, 7, 2, 8, 4, 5, 9, 9, 3, 1, 3, 2, 9)
Min Distance (4, 7): 4. Note that the order of elements can be anything.
Min Distance (9, 3): 1.
Min Distance (9, 9): 1.
Min Distance (9, 11): -1.
If either of the elements does not exist, then return -1.
There is no need to report the indices. Just print out the minimum distances.
solution: http://www.geeksforgeeks.org/find-the-minimum-distance-between-two-numbers/
"""
# O(n) time
def min_distance(a_list, x, y):
    if x not in a_list or y not in a_list:
        return -1

    i = 0
    n = len(a_list)
    min_dist = 9223372036854775807
    prev = None

    # find the first occurance of any of two numbers (x or y) and store the index if this occurance in prev
    while i < n:
        if a_list[i] == x or a_list[i] == y:
            prev = i
            break
        i += 1

    # traverse after the first occurance
    while i < n:
        if a_list[i] == x or a_list[i] == y:
            # if the current element matches with any of the two then check if current element and prev element are different
            # also check if this difference between current element index and prev is smaller than minimum distance so far
            if a_list[prev] != a_list[i] and (i - prev) < min_dist:
                min_dist = i - prev
                prev = i
            else:
                prev = i
        i += 1

    return min_dist

arr = [1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9]
arr_1 = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]

print min_distance(arr, 4, 7)
print min_distance(arr_1, 3, 6)


"""
# O(n^2)
def min_distance(a_list, x, y):
    i = 0
    n = len(a_list)
    min_dist = 9223372036854775807
    while i < n:
        j = i + 1
        while j < n:
            if (x == a_list[i] and y == a_list[j] or \
                y == a_list[i] and x == a_list[j]) and \
                min_dist > abs(i - j):
                min_dist = abs(i - j)
            j += 1
        i += 1

    return min_dist

arr = [1, 5, 3, 7, 2, 8, 3, 4, 5, 9, 9, 3, 1, 3, 2, 9]
print min_distance(arr, 4, 7)
print min_distance(arr, 9, 3)

"""

