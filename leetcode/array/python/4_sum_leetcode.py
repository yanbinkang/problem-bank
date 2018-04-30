"""
https://leetcode.com/problems/4sum/description/

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

ref: https://discuss.leetcode.com/topic/12368/clean-accepted-java-o-n-3-solution-based-on-3sum/12

O(n^3) time
"""
def four_sum(nums, target):
    result = []
    if len(nums) < 4: return result

    nums.sort()

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]: continue # ignore duplicates

        # first candidate too large, search finished
        if nums[i] * 4 > target: break # too big

        if nums[i] + 3 * nums[-1] < target: continue # too small
        # first candidate too small


        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]: continue # ignore duplicates

            # second candidate too large
            if nums[j] * 3 > target - nums[i]: break # too big

            # second candidate too small
            # too small
            if nums[j] + 2 * nums[-1] < target - nums[i]:
                continue

            low, high = j + 1, len(nums) - 1

            while low < high:
                s = nums[i] + nums[j] + nums[low] + nums[high]

                if s < target:
                    low += 1
                elif s > target:
                    high -= 1
                else:
                    result.append([nums[i], nums[j], nums[low], nums[high]])

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1

                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1

    return result

if __name__ == '__main__':
    print four_sum([1, 0, -1, 0, -2, 2], 0)
