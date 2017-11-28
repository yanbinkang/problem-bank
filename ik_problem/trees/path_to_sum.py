from binary_tree import BinaryTree
"""
question: Paths that sum to constant K
Problem
You have been given a Binary tree with integer (positive/negative) values Print all paths that  sum to a constant K. Paths start at root and end at leaves.
eg.
k = 6
               1
              / \
             2   3
            / \   \
           4   5  -6
          /   / \   \
        -1   1   2   8
"""
def path_to_sum(root, target_sum, res=[]):
    if root == None:
        return

    res.append(root.key)

    if root.left_child == None and root.right_child == None:
        if root.key == target_sum:
            for elem in res:
                print elem
            print "\n"
    else:
        path_to_sum(root.left_child, target_sum - root.key, res)
        path_to_sum(root.right_child, target_sum - root.key, res)

    res.pop()


def build_tree_1():
    tree = BinaryTree(1)

    tree.insert_left(2)
    tree.insert_right(3)

    tree.get_left_child().insert_right(5)
    tree.get_left_child().get_right_child().insert_left(1)
    tree.get_left_child().get_right_child().insert_right(2)
    tree.get_left_child().insert_left(4)
    tree.get_left_child().insert_left(-1)

    tree.get_right_child().insert_right(-6)
    tree.get_right_child().insert_right(8)

    return tree

tree_1 = build_tree_1()

path_to_sum(tree_1, 6)
