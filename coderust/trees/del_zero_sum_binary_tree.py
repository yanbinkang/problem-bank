from binary_tree import *

def build_tree():
    tree = BinaryTree(7)

    tree.insert_left(5)
    tree.insert_right(6)
    tree.get_left_child().insert_left(-3)
    tree.get_left_child().insert_right(-2)

    return tree

def del_zero_sum_sub_tree(tree):
    current = tree
    while current.left_child != None and current.right_child != None:
        if current.key + current.left_child.key + current.right_child.key == 0:
            current.key = None
            current.left_child = None
            current.right_child = None
        if current.left_child != None:
            current = current.left_child
            del_zero_sum_sub_tree(current)
        if current.right_child != None:
            current = current.right_child
            del_zero_sum_sub_tree(current)

    return current

old_tree = build_tree()
del_zero_sum_sub_tree(old_tree)

print old_tree.left_child.key
