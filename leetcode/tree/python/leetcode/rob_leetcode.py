from binary_tree import *

"""
https://leetcode.com/problems/house-robber-iii/

http://www.geeksforgeeks.org/largest-independent-set-problem/
"""

def rob(root):
    pass


if __name__ == '__main__':
    tree = BinaryTree(3)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.left.insert_right(3)
    tree.right.insert_right(1)

    tree2 = BinaryTree(3)
    tree2.insert_left(4)
    tree2.insert_right(5)

    tree2.left.insert_left(1)
    tree2.left.insert_right(3)
    tree2.right.insert_right(1)

    print rob(tree)
    print("\n")
    print rob(tree2)
