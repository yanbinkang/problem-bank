from binary_tree import *

"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

NOTE TO SELF:
We have to always build the right first, then the left. This is because we're always popping the last element of post_order in each recursive call and calling it root_val.

        If we build left first we'll have to slice in_order[:index] which will give us the first part of the inorder list. At a point the last popped element will not be in the first half of the inorder list:

        Look at the eg. below. If we build the left subtree first:

        First 7 is the root:
            index = 4
            inorder = [4, 10, 3, 1] and is passed as arg to build_tree

        Next, 2 becomes the root but 2 cannot be found in [4, 10, 3, 1].
"""

def build_tree(in_order, post_order):
    if in_order:
        root_val = post_order.pop()
        root = BinaryTree(root_val)

        index = in_order.index(root_val)

        root.right = build_tree(in_order[index+1:], post_order)
        root.left = build_tree(in_order[:index], post_order)

        return root

def level_order_traversal_test(root):
    queue = []

    queue.insert(0, root)

    while queue:
        root = queue.pop()

        print(str(root.val) + "\n")

        if root.left:
            queue.insert(0, root.left)
        if root.right:
            queue.insert(0, root.right)


if __name__ == '__main__':
    in_order = [4, 10, 3, 1, 7, 11, 8, 2]
    post_order = [4, 1, 3, 10, 11, 8, 2, 7]
    res = build_tree(in_order, post_order)

    level_order_traversal_test(res)

