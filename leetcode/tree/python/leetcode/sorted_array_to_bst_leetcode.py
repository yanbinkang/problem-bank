from binary_tree import *

def sorted_array_to_bst(root, a_list):
    first = 0
    last = len(a_list) - 1
    mid = len(a_list) // 2

    if first > last:
        return

    root = BinaryTree(a_list[mid])

    root.left = sorted_array_to_bst(a_list[:mid])
    root.right = sorted_array_to_bst(a_list[mid+1:])

    return root
