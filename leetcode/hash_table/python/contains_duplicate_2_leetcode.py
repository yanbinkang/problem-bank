"""
https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

https://discuss.leetcode.com/topic/22444/python-concise-solution-with-dictionary
"""
def contains_nearby_duplicate(nums, k):
    dic = {}

    for i, num in enumerate(nums):
        if num in dic and i - dic[num] <= k:
            return True
        dic[num] = i

    return False

