from binary_tree import BinaryTree

def same_tree(root_1, root_2):
    if root_1 == None and root_2 == None:
        return True

    if root_1 == None or root_2 == None:
        return False

    return root_1.key == root_2.key and same_tree(root_1.left_child, root_2.left_child) and same_tree(root_1.right_child, root_2.right_child)


def build_tree():
    tree = BinaryTree('a')

    tree.insert_left('b')
    tree.insert_right('c')
    tree.get_left_child().insert_left('d')
    tree.get_left_child().insert_right('e')
    tree.get_right_child().insert_left('f')
    tree.get_right_child().insert_right('g')

    return tree

def build_tree_1():
    tree = BinaryTree(10)

    tree.insert_left(16)
    tree.insert_right(5)
    tree.get_left_child().insert_right(-3)
    tree.get_right_child().insert_left(6)
    tree.get_right_child().insert_right(11)

    return tree

tree = build_tree()
tree_1 = build_tree_1()

print same_tree(tree, tree)
print same_tree(tree, tree_1)
