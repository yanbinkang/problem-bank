"""
https://leetcode.com/problems/remove-element/?tab=Description

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""
def remove_element(nums, val):
    for i in range(nums.count(val)):
        nums.remove(val)

    return len(nums)

"""
It scans numbers from the left to the right, one by one.

Once it finds a number that equals to elem, it swaps current element with the last element in the array and then dispose the last.

https://discuss.leetcode.com/topic/1228/my-solution-for-your-reference/3
"""
def remove_element_1(nums, val):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1

    return n

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    print remove_element(nums, 3)
    print nums
    print remove_element_1([3, 2, 2, 3], 3)

