"""
https://leetcode.com/problems/combination-sum/

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.
"""
def combination_sum(candidates, target):
    result = []

    sorted_candidates = sorted(candidates)

    helper(sorted_candidates, target, 0, result, [])

    return result

def helper(candidates, target, start, result, temp_list):
    if target < 0:
        return
    elif target == 0:
        result.append([] + temp_list)
    else:
        for i in range(start, len(candidates)):
            temp_list.append(candidates[i])
            helper(candidates, target - candidates[i], i, result, temp_list) # not i + 1 cos of repeated number
            temp_list.pop()


if __name__ == '__main__':
    print combination_sum([2, 3, 6, 7], 7)
    print combination_sum([1, 2, 3], 4)


