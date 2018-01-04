""" Given a binary tree, find size of largest binary search subtree in this binary tree.

Approach
--------

Traverse tree in post order fashion. Left and right nodes return 4 piece of information to root which isBST, size of max
BST, min and max in those subtree.

If both left and right subtree are BST and this node data is greater than max of left and less than min of right then it
returns to above level left size + right size + 1 and new min will be min of left side and new max will be max of right
side.

Video link
----------
* https://youtu.be/4fiDs7CCxkc

References
----------
* http://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/
* https://leetcode.com/problems/largest-bst-subtree/
* http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

O(n) time
"""

from binary_tree import BinaryTree

def largest_bst_subtree(root):
    m = largest(root)
    return m.size

def largest(root):
    if root is None:
        return MinMax()

    left_min_max = largest(root.left)
    right_min_max = largest(root.right)

    m = MinMax()

    if (
        (left_min_max.isBST == False or right_min_max.isBST == False) or \
        (left_min_max.max > root.val or right_min_max.min <= root.val)
        ):
        m.isBST = False
        m.size = max(left_min_max.size , right_min_max.size)
        return m

    m.isBST = True
    m.size = left_min_max.size + right_min_max.size + 1
    m.min = left_min_max.min if root.left is not None else root.val
    m.max = right_min_max.max if root.right is not None else root.val
    return m

class MinMax:
    def __init__(self):
        self.min = float("inf")
        self.max = float("-inf")
        self.isBST = True
        self.size = 0

if __name__ == '__main__':
    tree = BinaryTree(25)
    tree.insert_left(18)
    tree.insert_right(50)

    tree.left.insert_left(19)
    tree.left.insert_right(20)
    tree.right.insert_left(35)
    tree.right.insert_right(60)

    tree.left.left.insert_right(15)
    tree.left.right.insert_left(18)
    tree.left.right.insert_right(25)
    tree.right.left.insert_left(20)
    tree.right.left.insert_right(40)
    tree.right.right.insert_left(55)
    tree.right.right.insert_right(70)

    tree.right.left.left.insert_right(25)

    print largest_bst_subtree(tree)
