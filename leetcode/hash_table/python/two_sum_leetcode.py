"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


https://discuss.leetcode.com/topic/23004/here-is-a-python-solution-in-o-n-time/16

idea: store target - num as key and num's index as value in dictionary. As soon as an element in nums becomes available in the dictionary, return the value for that num's key and the nums index in an array.

Note: Use a set of you dont need the indexes or key/value pair.
"""
def two_sum(nums, target):
    hash_map = {}

    for i, num in enumerate(nums):
        if num in hash_map:
            return [hash_map[num], i]
        else:
            hash_map[target - num] = i

if __name__ == '__main__':
    print two_sum([2, 7, 11, 15], 9)
    print two_sum([0, 4, 3, 0], 0)
    print two_sum([-1,-2,-3,-4,-5], -8)
