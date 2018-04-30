"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/?tab=Description

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

https://discuss.leetcode.com/topic/17252/5-lines-c-java-nicer-loops
"""

# keep a counter, move unique elements to left. return counter
def remove_duplicates(nums):
    i = 0

    for num in nums:
        if i == 0 or num > nums[i - 1]:
            nums[i] = num
            i += 1

    return i

"""
ref: https://leetcode.com/articles/remove-duplicates-sorted-array/#approach-1-two-pointers-accepted

Keep two pointers i and j: i and j are slow and fast runners respectively.

i starts at 0 and j at 1

If nums[i] != nums[j] it means we're not looking at duplicates, we increment i and set nums[i] = nums[j]

Finally return i + 1, since at the end i will be at the zero-indexed index so we add 1 to get the new length.

O(n) time O(1) space.
"""
def remove_duplicates_1(nums):
    if len(nums) == 0: return 0
    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1



if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2, 3]
    print remove_duplicates(nums)
    print('\n')
    print remove_duplicates([1, 2])
