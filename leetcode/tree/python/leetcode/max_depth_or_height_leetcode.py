"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

from binary_tree import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def max_depth(tree):
    if tree is None:
        return 0

    return 1 + max(max_depth(tree.left), max_depth(tree.right))


if __name__ == '__main__':
    tt = BinaryTree(1)
    tt.insert_left(2)
    tt.insert_right(3)
    tt.left.insert_left(4)
    tt.right.insert_right(5)

    res = max_depth(tt)
    print res

"""
             1
            / \
           2   3
          /     \
         4       5
"""

