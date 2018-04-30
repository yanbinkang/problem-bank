"""
https://leetcode.com/problems/single-element-in-a-sorted-array

Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.

solution: https://discuss.leetcode.com/topic/87424/java-binary-search-simple-short-7l-and-o-log-n

Algo:

1. Find the middle index, if the middle index is odd, by difinition of the problem, we know that the number before it should be same:

eg: nums = [1, 1, 2, 2, 3, 3]. Here we know the middle index is 3 which is odd. You'll notice that the number before index 3, nums[2] is 2,

    hence nums[2] == nums[3] == 2

This means all the numbers in this half of the array appear twice: [1, 1, 2, 2]

So we reduce the middle number by one so we can comapre the original mid with the number before it:

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] != nums[mid + 1]:
            # some code

If the number before the original mid is not the same as the number before it, we know there should be a single number in the lower half:

        if nums[mid] != nums[mid + 1]:
            end = mid

else, look at the upper half of the orignal mid:

        start = mid + 2
"""
def single_non_duplicate(nums):
    start, end = 0, len(nums) - 1

    while start < end:
        mid = (start + end) / 2

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] != nums[mid + 1]:
            end = mid
        else:
            start = mid + 2

    return nums[start]

if __name__ == '__main__':
    print single_non_duplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
    print single_non_duplicate([3, 3, 7, 7, 10, 11, 11])
