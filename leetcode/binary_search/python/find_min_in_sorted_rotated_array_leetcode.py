"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.


Algo ref: https://discuss.leetcode.com/topic/4100/compact-and-clean-c-solution

Classic binary search problem.

Looking at subarray with index [start, end]. We can find out that if the first member is less than the last member, there's no rotation in the array. So we could directly return the first element in this subarray.

If the first element is larger than the last one, then we compute the element in the middle, and compare it with the first element.

If value of the element in the middle is larger than the first element, we know the rotation is at the second half of this array. Else, it is in the first half in the array.

ANOTHER EXPLANATION: ref: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/48499/4ms-simple-C++-code-with-explanation?orderBy=oldest_to_newest

In this problem, we have only three cases.

Case 1. The leftmost value is less than the rightmost value in the list: This means that the list is not rotated.
e.g> [1 2 3 4 5 6 7 ]

Case 2. The value in the middle of the list is greater than the leftmost and rightmost values in the list.
e.g> [ 4 5 6 7 0 1 2 3 ]

Case 3. The value in the middle of the list is less than the leftmost and rightmost values in the list.
e.g> [ 5 6 7 0 1 2 3 4 ]

As you see in the examples above, if we have case 1, we just return the leftmost value in the list. If we have case 2, we just move to the right side of the list. If we have case 3 we need to move to the left side of the list.
"""


def find_min(nums):
    lo, hi = 0, len(nums) - 1  # uses index

    while lo < hi:
        if nums[lo] < nums[hi]:
            return nums[lo]

        # we know array is rotated, do binary search
        mid = (lo + hi) // 2

        if nums[lo] <= nums[mid]:
            lo = mid + 1
        else:
            hi = mid

    return nums[lo]


if __name__ == '__main__':
    print find_min(
        [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    print find_min([4, 5, 6, 7, 0, 1, 2])
    print find_min([1])
