
"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
def combinationSum4(nums, target):
    dp = [-1] * (target + 1)
    dp[0] = 1

    return helper(nums, target, dp)


def helper(nums, target, dp):
    if dp[target] != -1:
        return dp[target]

    res = 0
    for i in range(len(nums)):
        if target >= nums[i]:
            res += helper(nums, target - nums[i], dp)

    dp[target] = res
    return res




if __name__ == '__main__':
    print combinationSum4([1, 2, 3], 4)
    print combinationSum4([9], 3)
