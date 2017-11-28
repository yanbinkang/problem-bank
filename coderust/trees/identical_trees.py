from binary_tree import *

def build_tree_1():
    tree = BinaryTree(100)

    tree.insert_left(50)
    tree.insert_right(200)
    tree.get_left_child().insert_left(25)
    tree.get_right_child().insert_right(350)
    tree.get_right_child().insert_left(125)
    return tree

def build_tree_2():
    tree = BinaryTree(100)

    tree.insert_left(50)
    tree.insert_right(200)
    tree.get_left_child().insert_left(25)
    tree.get_right_child().insert_right(350)
    tree.get_right_child().insert_left(125)
    return tree

tree_1 = build_tree_1()
tree_2 = build_tree_2()

def is_identical(root_1, root_2):
    if root_1 == None and root_2 == None:
        return True

    if root_1 != None and root_2 != None:
        return (root_1.key == root_2.key and \
            is_identical(root_1.left_child, root_2.left_child) and \
            is_identical(root_1.right_child, root_2.right_child))
    return False

print is_identical(tree_1, tree_2)
