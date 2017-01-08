from binary_tree import *

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

https://youtu.be/13m9ZCB8gjw

O(n)
"""

def lowest_common_ancestor(root, p, q):
    if root == None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q) #find p or q in left subtree
    right = lowest_common_ancestor(root.right, p, q) #find p or q in right subtree

    # three possible return value

    if left is not None and right is not None: return root # p and q can be found on root's left or right subtree. meaning root is LCA

    if left == None and right == None: return None # neither p or q cannot be found. return None

    return left if left else right # return non null node

if __name__ == '__main__':
    """
                                        3
                                      /   \
                                     6     8
                                    /  \    \
                                   2   11    13
                                      /  \   /
                                     9    5  7

lca(8, 7) => 8
lca(8, 11) => 3
    """
    tree = BinaryTree(3)

    tree.insert_left(6)
    tree.insert_right(8)

    tree.left.insert_left(2)
    tree.left.insert_right(11)
    tree.right.insert_right(13)

    tree.left.right.insert_left(9)
    tree.left.right.insert_right(5)
    tree.right.right.insert_left(7)

    p1 = tree.right
    q1 = tree.right.right.left
    res = lowest_common_ancestor(tree, p1, q1)
    print res.val #8

    print('\n')
    p2 = tree.right
    q2 = tree.left.right

    res1 = lowest_common_ancestor(tree, p2, q2)
    print res1.val #3

