"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

ref: https://discuss.leetcode.com/topic/6327/a-very-simple-java-solution-with-only-one-binary-search-algorithm

ref: https://discuss.leetcode.com/topic/16486/9-11-lines-o-log-n

Algo:

The function is a simple binary search, telling me the first index where I could insert a number n into nums to keep it sorted.

Thus, if nums contains target, I can find the first occurrence with search(target). I do that, and if target isn't actually there, then I return [-1, -1]. Otherwise, I ask search(target+1), which tells me the first index where I could insert target+1, which of course is one index behind the last index containing target, so all I have left to do is subtract 1

Question: I always wonder when we set high equal to A.length or A.length-1. Could anyone please provide some explanation? Thank you!

Answer:

I think it's for the case in which there is only one element.
For example, in the test case: search_range([1], 1)

If you use high = A.length - 1; high will be 0 == (1 - 1)
This makes while (low < high) false.
So every time you call first_greater_equal(), it will return 0 directly.

See: "Search insert position" question for further explanation.

Thus, return new int[]{start, Solution.firstGreaterEqual(A, target + 1) - 1};
will return {0, -1}, which is incorrect.
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        first = self.first_target_index(nums, target)

        # nums is empty or index isn't where target is located in nums
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        return [first, self.first_target_index(nums, target + 1) - 1]

    def first_target_index(self, nums, target):
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) / 2

            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


def search_range(nums, target):
    start = first_greater_equal(nums, target)

    if start == len(nums) or nums[start] != target:
        return [-1, -1]

    return [start, first_greater_equal(nums, target + 1) - 1]


def first_greater_equal(nums, target):
    low, high = 0, len(nums)

    while low < high:
        mid = (low + high) / 2

        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low


if __name__ == '__main__':
    print(search_range([5, 7, 7, 8, 8, 10], 8))
    print(search_range([1, 2, 5, 5, 5, 5, 5, 5, 5, 5, 20], 5))
    print(search_range([], 0))
