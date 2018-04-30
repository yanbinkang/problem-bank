"""
https://leetcode.com/problems/4sum/

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
def four_sum(nums, target):
    result = []
    nums = sorted(nums)

    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1

        target = -nums[i]

        while j < k:
            if nums[j] + nums[k] == target:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            elif nums[j] + nums[k] > target:
                k -= 1
            else:
                j += 1

    return result

if __name__ == '__main__':
    print four_sum([1, 0, -1, 0, -2, 2], 0)
