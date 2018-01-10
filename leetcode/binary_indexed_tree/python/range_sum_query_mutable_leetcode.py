"""
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:
    1. The array is only modifiable by the update function.

    2. You may assume the number of calls to update and sumRange function is distributed evenly.
"""
from binary_indexed_tree import *
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.itree = FenTree(nums)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.itree.update(i, val)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.itree.range_sum(i, j)

if __name__ == '__main__':
    nums = [1, 3, 5]
    obj = NumArray(nums)
    obj.update(1 ,2)
    print obj.sumRange(0, 2)
