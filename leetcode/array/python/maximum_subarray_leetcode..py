"""
https://leetcode.com/problems/maximum-subarray/#/description

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2 , 1, -3, 4, -1, 2, 1, -5, 4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

explanation: you keep one value, max_ending_here: the cumulative sum up to current element starting from somewhere in the past.

Algo:
At each new element, you could either add the new element to the existing sum or start calculating the sum from the current element (wipe out previous results)

At each new element if the current element is greater than the cumulative sum from the past plus the current element, we know the current element is the max_ending_here; else max_ending_here will be the cumulative sum + current element.

Example 1: [-2 , 1]. when you add -2 + 1 the result is not greater than 1. So 1 becomes max_ending_here. Start calculating cumulative sum from 1.

Example 2: [-2 , 1, -3, 4]. When you add -2 + 1 + (-3) + 4, the result is not greater than 4 so 4 becomes max_ending_here. Start calculating cumulative sum from 4.

All the while keep updating the max_so_far using max(max_so_far, max_ending_here).

Finally return max_so_far

ref: https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""


def max_subarray(nums):
    max_ending_here = nums[0]
    max_so_far = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == '__main__':
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
'''
num = 1
max_ending_here = max(1, -2+1) = 1
max_so_far = max(-2, 1) = 1

num=-3
max_ending_here = max(-3, 1+-3) = -2
max_so_far = max(1, -2) = 1

num=4
max_ending_here = max(4, -2+4) = 4
max_so_far = max(1, 4) = 4

num = -1
max_ending_here = max(-1, 4+-1) = 3
max_so_far = max(3, 4) = 4

num = 2
max_ending_here = max(2, 3+2) = 5
max_so_far = max(4, 5) = 5

num = 1
max_ending_here = max(1, 5 + 1) = 6
max_so_far = max(5, 6) = 6

num = -5
max_ending_here = max(-5, 6 + -5) = 1
max_so_far = max(6, 1) = 6

num = 4
max_ending_here = max(4, 1 + 5) = 5
max_so_far = max(6, 5) = 6

return 6
'''
