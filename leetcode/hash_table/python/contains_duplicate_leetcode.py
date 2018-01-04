"""
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

https://discuss.leetcode.com/topic/14730/possible-solutions

O(n) time and space
"""
def contains_duplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    hash_map = {}

    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    for key, value in hash_map.items():
        if value > 1:
            return True

    return False

def contains_duplicate_alt(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        else:
            num_set.add(num)

    return False
