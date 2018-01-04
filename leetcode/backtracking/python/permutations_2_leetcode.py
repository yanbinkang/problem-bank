"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

https://discuss.leetcode.com/topic/46161/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning
"""

def permute_unique(nums):
    result = []
    if not nums: return result

    sorted_nums = sorted(nums)

    used = [None for i in range(len(nums))]

    helper(sorted_nums, result, [], used)

    return result

def helper(nums, result, temp_list, used):
    if len(temp_list) == len(nums):
        result.append([] + temp_list)
    else:
        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            temp_list.append(nums[i])
            helper(nums, result, temp_list, used)
            used[i] = False
            temp_list.pop()

if __name__ == '__main__':
    nums = [1, 1, 2]
    print permute_unique(nums)
