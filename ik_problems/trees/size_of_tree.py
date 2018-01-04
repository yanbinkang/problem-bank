# return number of nodes in a tree
def size(root):
    if root == None:
        return 0

    left_size = size(root.left_child)
    right_size = size(root.right_child)

    return left_size + right_size + 1
