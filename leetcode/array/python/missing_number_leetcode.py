"""
https://leetcode.com/problems/missing-number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

algorithm:

Solution
First, we sum all numbers 0...n. We can do this using the equation:

((n ** 2) + n) / 2

because the numbers in 0...n are a triangular series.

Second, we sum all numbers in our input array,
which should be the same as our other sum but with our missing number ommited.

So the difference between these two sums is the missing number!
Complexity
O(n) time and O(1) additional space.
"""
def missingNumber(self, nums):
    n = len(nums)

    total = (pow(n, 2) + n) / 2

    sum_nums = sum(nums)

    return total - sum_nums
