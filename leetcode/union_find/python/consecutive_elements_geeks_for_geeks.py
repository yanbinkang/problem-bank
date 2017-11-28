"""
http://www.geeksforgeeks.org/check-if-array-elements-are-consecutive/

Given an unsorted array of numbers, write a function that returns true if array consists of consecutive numbers.

Examples:
a) If array is {5, 2, 3, 1, 4}, then the function should return true because the array has consecutive numbers from 1 to 5.

b) If array is {83, 78, 80, 81, 79, 82}, then the function should return true because the array has consecutive numbers from 78 to 83.

c) If the array is {34, 23, 52, 12, 3 }, then the function should return false because the elements are not consecutive.
"""
from disjoint_set import *
def consecutive_elements(nums):
    ds = DisjointSet()

    for num in nums:
        ds.make_set(num)

        if num - 1 in ds.map:
            ds.union(num, num - 1)

        if num + 1 in ds.map:
            ds.union(num, num + 1)

    return ds.num_sets == 1

if __name__ == '__main__':
    print consecutive_elements([5, 2, 3, 1, 4])
    print('\n')
    print consecutive_elements([83, 78, 80, 81, 79, 82])
    print('\n')
    print consecutive_elements([34, 23, 52, 12, 3])
    print('\n')
    print consecutive_elements([-4, -3, -2, -1, 0, 1])
    print('\n')
    print consecutive_elements([-4, -3, -2, -1, 0, 3])
