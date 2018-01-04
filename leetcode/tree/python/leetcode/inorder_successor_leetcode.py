from binary_tree import *

"""
https://leetcode.com/problems/inorder-successor-in-bst/

https://discuss.leetcode.com/topic/25076/share-my-java-recursive-solution/14
"""

def inorder_successor(root, p):
    if root is None:
        return None

    if p.val >= root.val:
        return inorder_successor(root.right, p)
    else:
        left = inorder_successor(root.left, p)

        return left if left else root.val


if __name__ == '__main__':
    tree = BinaryTree(17)
    tree.insert_left(5)
    tree.insert_right(35)

    tree.left.insert_left(2)
    tree.left.insert_right(11)

    tree.left.right.insert_left(9)
    tree.left.right.insert_right(16)

    tree.left.right.left.insert_left(7)

    tree.left.right.left.left.insert_right(8)

    p = tree.left

    print(inorder_successor(tree, p))
