from binary_tree import *

"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

https://discuss.leetcode.com/topic/32531/very-easy-with-recursion-1ms-java-solution/2

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

def min_depth(root):
    if root == None:
        return 0

    if root.left != None and root.right != None:
        return 1 + min(min_depth(root.left), min_depth(root.right))
    else:
        return 1 + max(min_depth(root.left), min_depth(root.right))
