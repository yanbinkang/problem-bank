"""
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5

Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
    * Then length of the input array is in range [1, 10,000].
    * The input array may contain duplicates, so ascending order here means <=.

ref: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/#approach-3-using-sorting-accepted

Time: O(nlogn) for because of sorting
Space: O(n)

Algo: Another very simple idea is as follows. We can sort a copy of the given array nums, say given by nums_sorted. Then, if we compare the elements of nums and nums_sorted, we can determine the leftmost and rightmost elements which mismatch. The subarray lying between them is, then, the required shorted unsorted subarray
"""
def findUnsortedSubarray(nums):
    sorted_nums = sorted(nums)

    start, end = float('inf'), 0

    for i in range(len(sorted_nums)):
        if sorted_nums[i] != nums[i]:
            start = min(start, i)
            end = max(end, i)

    return end - start + 1 if end - start >=0 else 0


if __name__ == '__main__':
    print findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
