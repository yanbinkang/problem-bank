"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

ref: https://discuss.leetcode.com/topic/28388/only-two-more-lines-code-on-top-of-the-solution-for-part-i
"""

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lo, hi = 0, len(nums) - 1

    # if nums[lo] == nums[hi], remove the duplicate
    while lo < hi and nums[lo] == nums[hi]:
        hi -= 1

    while lo < hi:
        if nums[lo] < nums[hi]:
            return nums[lo]

        mid = (lo + hi) / 2

        if nums[mid] >= nums[lo]:
            lo = mid + 1
        else:
            hi = mid

    return nums[lo]


if __name__ == '__main__':
    print findMin([1, 2, 1])
    print findMin([10, 1, 10, 10, 10])
    print findMin([1, 0, 1, 1, 1])
    print findMin([1, 1, 1, 0, 1])
