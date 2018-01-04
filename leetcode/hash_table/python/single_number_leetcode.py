"""
https://leetcode.com/problems/single-number/

Given an array of integers, every element appears twice except for one. Find that single one.
"""
def single_number(nums):
    hash_map = {}

    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    for key, value in hash_map.items():
        if value == 1:
            return key

def single_number_2(nums):
    hash_map = {}

    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    for key, value in hash_map.items():
        if value == 1:
            return key


def single_number_3(nums):
    res = 0

    for num in nums:
        res ^= num

    return res
