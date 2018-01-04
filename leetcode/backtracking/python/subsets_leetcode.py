"""
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

O(2^n) time and space. Because all possible combinations of array with 3 elements is 2^3 or 8. For n elements is 2^n
"""

def subsets(nums):
    result = []

    if not nums:
        return result

    sorted_nums = sorted(nums) # its fine if you don't sort nums as well

    helper(sorted_nums, result, 0, [])
    return result

def helper(nums, result, start, temp_list):
    result.append([] + temp_list)

    for i in range(start, len(nums)):
        temp_list.append(nums[i])
        helper(nums, result, i + 1, temp_list)
        temp_list.pop()


if __name__ == '__main__':
    print subsets([1, 2, 3])
    print subsets('word')
    print subsets('albert')

