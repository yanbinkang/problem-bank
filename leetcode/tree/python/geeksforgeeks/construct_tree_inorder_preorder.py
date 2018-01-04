"""
http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

Let us consider the below traversals:

Inorder sequence: D B E A F C
Preorder sequence: A B D E C F

"""
from binary_tree import *
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
