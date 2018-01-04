"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

https://discuss.leetcode.com/topic/7798/the-bottom-up-o-n-solution-would-be-better

This is a top down approach.

Solution is to check whether the tree is balanced strictly according to the definition of balanced binary tree: the difference between the heights of the two sub trees are not bigger than 1, and both the left sub tree and right sub tree are also balanced. With the helper function depth(), we could easily write the code.

For the current node root, calling depth() for its left and right children actually has to access all of its children, thus the complexity is O(nlogn).

This approach is O(n^2) because worse case occurs in the case of skewed tree.
"""

def is_balanced(root):
    if root == None:
        return True

    left_height = depth(root.left)
    right_height = depth(root.right)

    return (abs(left_height - right_height)) <= 1 and is_balanced(root.left) and is_balanced(root.right)

def depth(self, root):
    if root == None:
        return 0

    return 1 + max(depth(root.left), depth(root.right))

