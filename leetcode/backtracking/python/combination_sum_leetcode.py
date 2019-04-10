"""
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


def combination_sum(candidates, target):
    result = []

    helper(candidates, target, 0, result, [])

    return result


def helper(candidates, target, start, result, temp_list):
    if target < 0: return

    if target == 0:
        result.append([] + temp_list)
    else:
        for i in range(start, len(candidates)):
            temp_list.append(candidates[i])
            helper(
                candidates, target - candidates[i], i, result, temp_list
            )  # not i + 1 cos the same repeated number can be chosen unlimited times
            temp_list.pop()


if __name__ == '__main__':
    print(combination_sum([2, 3, 6, 7], 7))
    print(combination_sum([1, 2, 3], 4))
