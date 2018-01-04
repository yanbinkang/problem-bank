"""
https://leetcode.com/problems/subtree-of-another-tree/#/description

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:
   4
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.

Example 2:

Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:
   4
  / \
 1   2

Return false.
"""
from binary_tree import *
def isSubtree(s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    if s is None:
        return False

    if is_same_tree(s, t):
        return True

    return isSubtree(s.left, t) or isSubtree(s.right, t)

def is_same_tree(s, t):
    if s is None and t is None:
        return True

    if s is None or t is None:
        return False

    return s.val == t.val and is_same_tree(s.left, t.left) and\
                        is_same_tree(s.right, t.right)

if __name__ == '__main__':
    """
          Tree 1 (t)

            26
          /   \
        10     3
      /    \     \
    4       6      3
     \
      30


      Tree 2 (s)

        10
      /    \
    4       6
     \
      30
    """


    s = BinaryTree(10)
    s.insert_left(4)
    s.insert_right(6)
    s.left.insert_right(30)

    t = BinaryTree(26)
    t.insert_left(10)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(6)
    t.left.left.insert_right(30)
    t.right.insert_right(3)

    print isSubtree(t, s)
