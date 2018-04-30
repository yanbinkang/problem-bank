"""
https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest continuous increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.

Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
Note: Length of the array will not exceed 10,000.
"""
def findLengthOfLCIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right, max_length = 0, 0, 1

    if not nums: return 0

    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            right += 1

            # if right - left + 1 > max_length:
            max_length = max(max_length, right - left + 1)
        else:
            left = right = i


    return max_length

def findLengthOfLCIS_DP(nums):
    if not nums: return 0

    dp =  [0] * len(nums)
    max_length = 1
    dp[0] = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1

        max_length = max(max_length, dp[i])

    return max_length

if __name__ == '__main__':
    print findLengthOfLCIS([1,3,5,4,7])
    print('\n')
    print findLengthOfLCIS_DP([1,3,5,4,7])
