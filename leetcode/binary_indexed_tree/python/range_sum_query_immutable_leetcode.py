"""
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
    1) You may assume that the array does not change.
    2) There are many calls to sumRange function.
"""
from binary_indexed_tree import *
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.itree = FenTree(nums)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.itree.range_sum(i, j)

if __name__ == '__main__':
    tree = NumArray([-2, 0, 3, -5, 2, -1])
    print tree.sumRange(0, 2) # -> 1
    print tree.sumRange(2, 5) # -> -1
    print tree.sumRange(0, 5) # -> -3
