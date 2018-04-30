"""
https://leetcode.com/problems/largest-number/#/description

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""
def largest_number(nums):
    nums = map(str, nums)
    nums.sort(cmp=lambda x, y: cmp(y + x, x + y))

    return str(int(''.join(nums)))
    # return ''.join(nums).lstrip('0') or '0'

if __name__ == '__main__':
    print largest_number([3, 30, 34, 5, 9]) # 9534330
