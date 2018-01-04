"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
    This problem was inspired by this original tweet by Max Howell:
        Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
"""
from binary_tree import *

def invert_tree(root):
    if root == None:
        return root

    # temp_left = root.left
    left = root.left
    right = root.right

    root.left = invert_tree(right)
    root.right = invert_tree(left)

    return root
