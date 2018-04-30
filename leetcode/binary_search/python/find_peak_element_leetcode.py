"""
https://leetcode.com/problems/find-peak-element/description/

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -INF.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

solution: https://leetcode.com/articles/find-peak-element/
"""
def find_peak_element(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) / 2

        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1

    return l

if __name__ == '__main__':
    print find_peak_element([1, 2, 3, 1])
