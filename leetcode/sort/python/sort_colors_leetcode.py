"""
https://leetcode.com/problems/sort-colors/description/

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

"""
ref: https://discuss.leetcode.com/topic/5422/share-my-at-most-two-pass-constant-space-10-line-solution

The idea is to sweep all 0s to the left and all 2s to the right, then all 1s are left in the middle.
"""
def sort_colors_1(nums):
    second = len(nums) - 1
    zero = 0

    for i in range(len(nums)):
        """
        because we want the 2's at the end we don't care if we find 2 and i == second (i.e at the very end of the list), that's why we care about cases where we've found 2 and i < second

        The while loop says: while i < second or if i != second, if there is a 2 move it to the right
        """
        while nums[i] == 2 and i < second:
            temp = nums[i]
            nums[i] = nums[second]
            nums[second] = temp

            second -= 1

        """
        because we want 0's at the front we don't care if we find 0 and i == zero (eg. when i, zero = 0, 0). that's why we care about cases where we've found 0 and i > zero

        Thwe while loop says, while i is greater than zero, if theres a zero, move if to the left
        Eg. [0, 1, 0]
        """
        while nums[i] == 0 and i > zero:
            temp = nums[i]
            nums[i] = nums[zero]
            nums[zero] = temp

            zero += 1

# ref: https://discuss.leetcode.com/topic/26181/ac-python-in-place-one-pass-solution-o-n-time-o-1-space-no-swap-no-count
def sort_colors(nums):
    i = j = 0

    for k in range(len(nums)):
        temp = nums[k]
        nums[k] = 2

        if temp < 2:
            nums[j] = 1
            j += 1

        if temp == 0:
            nums[i] = 0
            i += 1

# my solution
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    red_count = nums.count(0)
    white_count = nums.count(1)
    blue_count = nums.count(2)

    k = 0

    for i in range(red_count):
        nums[k] = 0
        k += 1

    for i in range(white_count):
        nums[k] = 1
        k += 1

    for i in range(blue_count):
        nums[k] = 2
        k += 1

if __name__ == '__main__':
    sort_colors([1, 0, 0, 1, 1, 2, 0, 1])
