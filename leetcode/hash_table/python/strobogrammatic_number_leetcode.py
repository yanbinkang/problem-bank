"""
https://leetcode.com/problems/strobogrammatic-number/

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

https://discuss.leetcode.com/topic/21773/python-solution-with-dictionary
"""
def is_strobogrammatic(num):
    dic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in dic or dic[num[left]] != num[right]:
            return False

        left += 1
        right -= 1

    return True

# https://discuss.leetcode.com/topic/38099/simple-python-solution/2
def is_strobogrammatic_2(nums):
    maps = {('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')}
    i,j = 0, len(num) - 1
    while i <= j:
        if (num[i], num[j]) not in maps:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    print is_strobogrammatic('818')
    print is_strobogrammatic('69')
    print is_strobogrammatic('6889')
    print is_strobogrammatic('1234')

