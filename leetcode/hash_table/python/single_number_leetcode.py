"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
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
