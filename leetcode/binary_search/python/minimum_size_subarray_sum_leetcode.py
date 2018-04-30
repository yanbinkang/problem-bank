"""
https://leetcode.com/problems/minimum-size-subarray-sum/#/description

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2, 3, 1, 2, 4, 3] and s = 7,
the subarray [4, 3] has the minimal length under the problem constraint.
"""
def min_subarray_len(s, nums):
    i, j, imin = 1, len(nums), 0

    while i <= j:
        mid = (i + j) / 2

        if window_exist(mid, nums, s):
            j = mid - 1
            imin = mid
        else:
            i = mid + 1

    return imin

def window_exist(mid, nums, s):
    total = 0

    for i in range(len(nums)):
        if i >= mid:
            total -= nums[i - mid]
        total += nums[i]

        if total >= s: return True

    return False



if __name__ == '__main__':
    print min_subarray_len(7, [2, 3, 1, 2, 4, 3])
