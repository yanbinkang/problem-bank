"""
http://www.geeksforgeeks.org/diameter-of-a-binary-tree/

The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree.

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
from binary_tree import *
def diameter(root):
    result = 0

    if root is None: return result

    cur = height(root.left) + height(root.right)
    left = diameter(root.left)
    right = diameter(root.right)

    return max(cur, max(left, right))

def height(root):
    if root is None: return 0

    return 1 + max(height(root.left), height(root.right))


if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)

    print diameter(t)
