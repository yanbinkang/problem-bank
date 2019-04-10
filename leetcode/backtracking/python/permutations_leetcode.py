"""
https://leetcode.com/problems/permutations/

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

read carefully:

https://discuss.leetcode.com/topic/6377/my-ac-simple-iterative-java-python-solution

https://discuss.leetcode.com/topic/46161/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning
"""


def permute(nums):
    results = [[]]

    for num in nums:
        temp = []

        for result in results:
            for i in range(len(result) + 1):
                temp.append(result[:i] + [num] + result[i:])
        results = temp

    return results


def permute_backtracking(nums):
    result = []

    helper(nums, result, [])
    return result


def helper(nums, result, temp_list):
    if len(temp_list) == len(nums):
        result.append([] + temp_list)
    else:
        for i in range(len(nums)):
            if nums[i] in temp_list:
                continue

            temp_list.append(nums[i])
            helper(nums, result, temp_list)
            temp_list.pop()


def permute_backtracking_1(n):
    result = []

    if not n: return result

    test_helper(n, result, [])
    return result


def test_helper(n, result, temp_list):
    if len(temp_list) == n:
        result.append([] + temp_list)
    else:
        for i in range(1, n + 1):
            if i in temp_list:
                continue

            temp_list.append(i)
            test_helper(n, result, temp_list)
            temp_list.pop()


print(permute([1, 2, 3]))
print('\n')
print(permute("abc"))
print('\n')
print(permute_backtracking([1, 2, 3]))
print(permute_backtracking('abc'))
print('\n')
print(permute_backtracking_1(3))
