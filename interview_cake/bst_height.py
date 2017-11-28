def get_height_bst(tree):
    return max_height(tree)

def max_height(root):
    if root == None:
        return 0
    else:
        return 1 + max(max_height(root.left_child), max_height(root.right_child))
