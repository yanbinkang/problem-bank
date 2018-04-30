"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].


Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.


Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

ref: https://discuss.leetcode.com/topic/102997/python-dp-with-explanation
"""
def findNumberOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lis = [[1, 1]] * (len(nums)) # lis[i] = length of lis till i, number of lis till i
    longest = 1

    for i in range(1, len(nums)):
        count, current_longest = 0, 1
        for j in range(i):
            if nums[i] > nums[j]:
                current_longest = max(current_longest, lis[j][0] + 1)

        for j in range(i):
            if lis[j][0] + 1 == current_longest and nums[i] > nums[j]:
                count += lis[j][1]

        lis[i] = [current_longest, max(count, lis[i][1])]
        longest = max(current_longest, longest)

    return sum(item[1] for item in lis if item[0] == longest)
