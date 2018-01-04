# Write a function to find if a given integer x appears more than n/4 times in a sorted array of integers.

"""
Solution 1: Linearly search for first occurance of the element, once you find it (at index i), check element at index i + n/4. If element is present at i + n/4 then return True else return False.

Solution 2: Use binary search for find first occurance of the element, once you find it (at index i), check element at index i + n/4. If element is present at i + n/4 then return True else return False

In all cases make sure to check if i + n/4 is <= n.
"""

def find_majority_element(arr, x):
    first = 0
    size = len(arr)
    last = len(arr) - 1

    while first <= last:
        mid = (first + last) // 2
        if (mid == 0 or x >= arr[mid-1]) and (arr[mid] == x):
            # print mid
            if ((mid + size/4) <= size - 1) and arr[mid + size/4] == x:
                return True
            else:
                return False
        elif x < arr[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return -1

a_list_0 = [1, 2, 3, 3, 3, 10]
a_list_1 = [1, 2, 3, 4, 4, 4, 4, 11, 13, 14]
a_list_2 = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7]
print find_majority_element(a_list_0, 3)
print find_majority_element(a_list_1, 4)
print find_majority_element(a_list_2, 7)
