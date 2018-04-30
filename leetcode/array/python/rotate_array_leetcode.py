"""
https://leetcode.com/problems/rotate-array/#/description

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4]

algorithm:

let a= [1,2,3,4,5,6,7]
k = 3.

1. we have to first reverse the whole array by swapping first element with the last one and so on..
you will get [7, 6, 5, 4, 3, 2, 1]

2. reverse the elements from 0 to k - 1
reverse the elements 7, 6, 5
you will get [5, 6, 7, 4, 3, 2, 1]

3. reverse the elements from k to n - 1
reverse the elements 4,3,2,1
you will get [5, 6, 7, 1, 2, 3, 4]

Note: we do k = k % len(nums) because sometimes, k is larger than the length of array. For example nums = [1, 2, 3, 4, 5], k = 12, this means we only need to rotate the last two numbers. k = k % nums.length = 2

O(n) time, O(1) space
"""
def rotate(nums, k):
    k = k % len(nums)

    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

def reverse(nums, start, end):
    while start <= end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp

        start += 1
        end -= 1

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7]
    print('array before rotation %s') % array
    rotate(array, 3)
    print('array after rotation %s') % array
