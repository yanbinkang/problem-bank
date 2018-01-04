"""
http://www.geeksforgeeks.org/merge-two-binary-trees-node-sum/

Given two binary trees. We need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the non-null node will be used as the node of new tree.

Example:

Input:
     Tree 1            Tree 2
       2                 3
      / \               / \
     1   4             6   1
    /                   \   \
   5                     2   7

Output: Merged tree:
         5
        / \
       7   5
      / \   \
     5   2   7

look at: https://leetcode.com/problems/merge-two-binary-trees/#/description
"""

