"""
http://www.geeksforgeeks.org/construct-a-binary-tree-from-postorder-and-inorder/

Given Postorder and Inorder traversals, construct the tree.

Examples:

Input :
in[]   = {2, 1, 3}
post[] = {2, 3, 1}

Output : Root of below tree
      1
    /   \
   2     3


Input :
in[]   = {4, 8, 2, 5, 1, 6, 3, 7}
post[] = {8, 4, 5, 2, 6, 7, 3, 1}

Output : Root of below tree
          1
       /     \
     2        3
   /    \   /   \
  4     5   6    7
    \
      8

NOTE TO SELF:
We have to always build the right first, then the left. This is because we're always popping the last element of post_order in each recursive call and calling it root_val.

        If we build left first we'll have to slice in_order[:index] which will give us the first part of the inorder list. At a point the last popped element from post_order will not be in the first half of the inorder list:
"""
from binary_tree import *
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
