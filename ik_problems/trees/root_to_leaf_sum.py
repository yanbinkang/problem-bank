# Reference http://www.geeksforgeeks.org/root-to-leaf-path-sum-equal-to-a-given-number/
from binary_tree import BinaryTree

def root_to_leaf_sum(root, target_sum, result=[]):
    if root == None:
        return False

    if root.left_child == None and root.right_child == None:
        if root.key == target_sum:
            result.append(root.key)
            return True
        else:
            return False

    if root_to_leaf_sum(root.left_child, target_sum - root.key, result):
        result.append(root.key)
        return True
    if root_to_leaf_sum(root.right_child, target_sum - root.key, result):
        result.append(root.key)
        return True

    return False


def build_tree_1():
    tree = BinaryTree(10)

    tree.insert_left(16)
    tree.insert_right(5)
    tree.get_left_child().insert_right(-3)
    tree.get_right_child().insert_left(6)
    tree.get_right_child().insert_right(11)

    return tree

tree_1 = build_tree_1()
print root_to_leaf_sum(tree_1, 26)
