"""
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

https://discuss.leetcode.com/topic/46161/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning
"""

def subsets_with_dup(nums):
    result = []

    if not nums:
        return result

    sorted_nums = sorted(nums)

    helper(sorted_nums, result, 0, [])
    return result

def helper(nums, result, start, temp_list):
    res = sorted([] + temp_list)
    if res not in result:
        result.append(res)

    for i in range(start, len(nums)):
        temp_list.append(nums[i])
        helper(nums, result, i + 1, temp_list)
        temp_list.pop()

def subsets_with_dup_1(nums):
    result = []

    if not nums:
        return result

    sorted_nums = sorted(nums)

    _helper(sorted_nums, result, 0, [])
    return result

def _helper(nums, result, start, temp_list):
    result.append([] + temp_list)

    for i in range(start, len(nums)):
        if i > start and nums[i] == nums[i - 1]:
            continue
        temp_list.append(nums[i])
        _helper(nums, result, i + 1, temp_list)
        temp_list.pop()


if __name__ == '__main__':
    print subsets_with_dup([1, 2, 2])
    print subsets_with_dup_1([1, 3, 3])
    print subsets_with_dup('aabc')

