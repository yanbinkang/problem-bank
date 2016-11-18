from binary_tree import *

def max_depth(tree):
    if tree is None:
        return 0

    return 1 + max(max_depth(tree.left), max_depth(tree.right))


if __name__ == '__main__':
    tt = BinaryTree(1)
    tt.insert_left(2)
    tt.insert_right(3)
    tt.left.insert_left(4)
    tt.right.insert_right(5)

    res = max_depth(tt)
    print res

"""
             1
            / \
           2   3
          /     \
         4       5
"""

