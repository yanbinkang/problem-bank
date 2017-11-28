# from binary_tree import *

# def build_tree_1():
#     tree = BinaryTree(100)

#     tree.insert_left(50)
#     tree.insert_right(200)
#     tree.get_left_child().insert_left(25)
#     tree.get_left_child().insert_right(75)
#     tree.get_right_child().insert_left(125)
#     tree.get_right_child().insert_right(350)
#     return tree

# t = build_tree_1()

# def nth_highest_node_in_bst(root, n):
#     count += 1
#     if root.right_child:
#         nth_highest_node_in_bst(root.right_child, n)
#     if count == n:
#         print root.key
#     if root.left_child:
#         nth_highest_node_in_bst(root.left_child, n)

# print nth_highest_node_in_bst(t, 1)
