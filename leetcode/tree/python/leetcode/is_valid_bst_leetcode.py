from binary_tree import *

# https://youtu.be/MILxfAbIhrE
def is_valid_bst_rec(root):
    minimum = float("-inf")
    maximum = float("inf")

    return valid_bst(root, minimum, maximum)

def valid_bst(root, minimum, maximum):
    if root == None:
        return True

    # for left maximum is always root.val because nothing in that subtree should be greater than that value. and for right minimum is always root.val because nothing in that subtree should be less than that value.
    if root.val <= minimum or root.val >= maximum:
        return False

    return valid_bst(root.left, minimum, root.val) and valid_bst(root.right, root.val, maximum)

# use inorder traversal and check if result is sorted
def is_valid_bst_inoder_helper(root):
    result = []

    _inorder_traversal(root, result)

    for i in range(1, len(result)):
        if result[i-1] >= result[i]:
            return False

    return True

def _inorder_traversal(root, result):
    if root:
        _inorder_traversal(root.left, result)
        result.append(root.val)
        _inorder_traversal(root.right, result)


if __name__ == '__main__':
    tree = BinaryTree(2)
    tree.insert_left(1)
    tree.insert_right(3)

    print(is_valid_bst_rec(tree))
    print('\n')
    print(is_valid_bst_inoder_helper(tree))

