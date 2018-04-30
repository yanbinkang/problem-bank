"""
https://leetcode.com/problems/majority-element-ii/?tab=Description

Given an integer array of size n, find all elements that appear more than n/3 times. The algorithm should run in linear time and in O(1) space.

https://discuss.leetcode.com/topic/17564/boyer-moore-majority-vote-algorithm-and-my-elaboration
"""
def majority_element(nums):
    if not nums: return []

    count_1, count_2, candidate_1, candidate_2 = 0, 0, 0, 1

    for n in nums:
        if n == candidate_1:
            count_1 += 1
        elif n == candidate_2:
            count_2 += 1
        elif count_1 == 0:
            candidate_1, count_1 = n, 1
        elif count_2 == 0:
            candidate_2, count_2 = n, 1
        else:
            count_1, count_2 = count_1 - 1, count_2 - 1

    return [n for n in (candidate_1, candidate_2) if nums.count(n) > len(nums) // 3]

