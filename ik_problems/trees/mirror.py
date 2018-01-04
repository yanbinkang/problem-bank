from binary_tree import BinaryTree
"""
question: http://cslibrary.stanford.edu/110/BinaryTrees.html
change a tree so that the roles of the right pointers are swappped at every node.

       4
      / \
     2   5
    / \
   1   3

       4
      / \
     5   2
        / \
       3   1
"""
def mirror_copy(root):
    if root == None:
        return None

    if root != None:
        new_tree = BinaryTree(root.key)

    if root.left_child and root.right_child:
        new_tree.left_child = mirror_copy(root.right_child)
        new_tree.right_child = mirror_copy(root.left_child)

    return new_tree

def mirror(root):
    if root == None:
        return None

    if root.left_child and root.right_child:
        tmp = root.left_child
        root.left_child = root.right_child
        root.right_child = tmp
        mirror(root.right_child)
        mirror(root.left_child)


    return root

def build_tree_1():
    tree = BinaryTree(4)

    tree.insert_left(2)
    tree.insert_right(5)

    tree.get_left_child().insert_left(1)
    tree.get_left_child().insert_right(3)

    return tree

tree_1 = build_tree_1()

# before
print tree_1.in_order()

# after
print mirror_copy(tree_1).in_order()
print mirror(tree_1).in_order()
