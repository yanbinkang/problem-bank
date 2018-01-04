from binary_tree import *

"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

http://articles.leetcode.com/construct-binary-tree-from-inorder-and-preorder-postorder-traversal

https://discuss.leetcode.com/topic/21287/python-short-recursive-solution/2
https://discuss.leetcode.com/topic/16221/simple-o-n-without-map
"""

def build_tree(pre_order, in_order):
    if in_order:
        root_val = pre_order.pop(0)
        root = BinaryTree(root_val)
        inorder_index = in_order.index(root_val)


        root.left = build_tree(pre_order, in_order[:inorder_index])
        root.right = build_tree(pre_order, in_order[inorder_index+1:])

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
    pre_order = [7, 10, 4, 3, 1, 2, 8, 11]
    in_order = [4, 10, 3, 1, 7, 11, 8, 2]

    res = build_tree(pre_order, in_order)

    level_order_traversal_test(res)
