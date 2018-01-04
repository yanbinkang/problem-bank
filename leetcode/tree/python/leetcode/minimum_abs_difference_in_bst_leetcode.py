"""
https://leetcode.com/contest/leetcode-weekly-contest-21/problems/minimum-absolute-difference-in-bst/

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).

Note: There are at least two nodes in this BST.
"""
def getMinimumDifference(root):
    result = []
    inorder(root, result)

    min_diff = float('inf')

    for i in range(1, len(result)):
        min_diff = min(min_diff, abs(result[i] - result[i - 1]))

    return min_diff

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)
