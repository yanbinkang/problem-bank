from sys import maxint

def valid_bst_recursive(root, lower_bound = -maxint, upper_bound = maxint):
    if (not root):
        return True

    if (root.value > upper_bound or root.value < lower_bound):
        return False

    return valid_bst_recursive(root.left, lower_bound, root.value) \
        and valid_bst_recursive(root.right, root.value, upper_bound)
