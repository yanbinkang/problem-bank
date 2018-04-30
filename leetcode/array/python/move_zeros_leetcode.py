"""
https://leetcode.com/problems/move-zeroes/?tab=Description

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.
"""
def move_zeros(nums):
    # NOTE: array.remove(x) Removes the first occurrence of x from the array
    for i in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)

"""
Scan the array, maintain an index position insert_pos starting at 0. If element is not 0 move element to nums[insert_pos]. Increment insert_pos for next operation.

After moving all non zero's to the front, we have to set the remaining elements to zero. insert_pos will be at position where we have to insert the first zero. while insert_pos < len(nums) set nums[insert_pos] = 0 and increment insert_pos.
"""
def move_zeros_1(nums):
    if not nums or len(nums) == 0: return

    insert_pos = 0

    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    move_zeros_1(nums) # [1, 3, 12, 0, 0]
    print move_zeros_1(nums).__doc__ # [1, 3, 12, 0, 0]
    print nums
