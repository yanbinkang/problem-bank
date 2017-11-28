"""
Given 2 BSTs. Find If BST2 is subtree of BST1.

          20

         /  \
        8    22
       / \     \
      4   12    23
     /
    3


        8
       / \
      4   12
"""

def is_subtree(tree_1, tree_2):
    if tree_2 == None:
        return True

    if tree_1 == None:
        return False

    if is_same_tree(tree_1, tree_2):
        return True

    # taking advantage of bst property
    # if tree_1.key > tree_2.key it means tree_2 will be in subtree of tree_1. opposite is true
    if tree_1.key > tree_2.key:
        return is_subtree(tree_1.left_child, tree_2)

    return is_subtree(tree_1.right_child, tree_2)


def is_same_tree(root_1, root_2):
    if root_2 == None:
        return True

    if root_1 == None and root_2 != None:
        return False

    return root_1.key == root_2.key and is_same_tree(root_1.left_child, root_2.left_child) \
        and is_same_tree(root_1.right_child, root_2.right_child)

