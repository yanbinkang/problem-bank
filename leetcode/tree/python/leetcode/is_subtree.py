from binary_tree import *
"""
this function will return true if s is a subtree of t
O(mn) time worse case where m and n are number of nodes in given two trees

see this for O(n): http://www.geeksforgeeks.org/check-binary-tree-subtree-another-binary-tree-set-2/
"""
def is_subtree(t, s):
    if s is None:
        return True

    if t is None:
        return True

    if is_same_tree(t, s):
        return True

    return is_same_tree(t.left, s) or is_same_tree(t.right, s)

# utility function to check whether trees with roots as root1 and root2 are identical or not
def is_same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return (root1.val == root2.val and is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right))
