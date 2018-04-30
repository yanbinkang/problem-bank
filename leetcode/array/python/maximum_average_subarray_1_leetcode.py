"""
https://leetcode.com/problems/maximum-average-subarray-i/

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
    1. 1 <= k <= n <= 30,000.
    2. Elements of the given array will be in the range [-10,000, 10,000].

ref: https://leetcode.com/articles/maximum-average-subarray/#approach-2-cumulative-sum-accepted

O(n) time and space
"""
def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    """
    n = len(nums)

    for i in range(1, n):
        nums[i] = nums[i] + nums[i - 1]

    avg_so_far = nums[k - 1] * 1.0 / k

    for i in range(k, len(nums)):
        avg_so_far = max(avg_so_far, ((nums[i] - nums[i - k]) * 1.0) / k)

    return avg_so_far

if __name__ == '__main__':
    print findMaxAverage([1, 12, -5, -6, 50, 3], 4)
