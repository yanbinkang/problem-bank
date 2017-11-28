def count_bst_nodes(tree):
    if tree == None:
        return 0
    return count_bst_nodes(tree.left_child) + 1 + count_bst_nodes(tree.right_child)
