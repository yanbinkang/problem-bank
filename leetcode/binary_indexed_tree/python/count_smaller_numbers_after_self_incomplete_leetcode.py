"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/#/description

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Return the array [2, 1, 1, 0].
"""
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i):
        # i += 1
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def total(self, i):
        # i += 1
        r = 0

        while i > 0:
            r += self.sums[i]
            i -= i & -i

        return r

def count_smaller(nums):
    d = { value: index for index, value in enumerate(sorted(set(nums))) }

    tree, result = BinaryIndexedTree(len(d)), []

    for i in reversed(range(len(nums))):
        result.append(tree.total( d[nums[i]] ))
        tree.update( d[nums[i]] + 1 )

    return result[::-1]


if __name__ == '__main__':
    print count_smaller([5, 2, 6, 1])

