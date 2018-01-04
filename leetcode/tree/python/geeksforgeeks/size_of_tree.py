"""
http://www.geeksforgeeks.org/write-a-c-program-to-calculate-size-of-a-tree/

Size of a tree is the number of elements present in the tree.

Algorithm:

size(tree)
1. If tree is empty then return 0
2. Else
     (a) Get the size of left subtree recursively  i.e., call
          size( tree->left-subtree)
     (a) Get the size of right subtree recursively  i.e., call
          size( tree->right-subtree)
     (c) Calculate size of the tree as following:
            tree_size  =  size(left-subtree) + size(right-
                               subtree) + 1
     (d) Return tree_size
"""
from binary_tree import *
def size(tree):
    if tree is None:
        return 0

    left = size(tree.left)
    right = size(tree.right)

    return 1 + left + right

if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)

    print "Size of the tree is %d" % (size(t))
