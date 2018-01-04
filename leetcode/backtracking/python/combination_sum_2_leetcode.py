"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

https://discuss.leetcode.com/topic/46161/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning/2
"""
def combination_sum_2(candidates, target):
    result = []
    if not candidates or not target:
        return result

    sorted_candidates = sorted(candidates)

    helper(sorted_candidates, target, result, 0, [])

    return result

def helper(candidates, target, result, start, temp_list):
    if target < 0:
        return
    elif target == 0:
        result.append([] + temp_list)
    else:
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            temp_list.append(candidates[i])
            helper(candidates, target - candidates[i], result, i + 1, temp_list)
            temp_list.pop()

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print combination_sum_2(candidates, target)
