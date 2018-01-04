"""
http://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/

Algorithm:

 maxDepth()
1. If tree is empty then return 0
2. Else
     (a) Get the max depth of left subtree recursively  i.e.,
          call maxDepth( tree->left-subtree)
     (a) Get the max depth of right subtree recursively  i.e.,
          call maxDepth( tree->right-subtree)
     (c) Get the max of max depths of left and right
          subtrees and add 1 to it for the current node.
         max_depth = max(max dept of left subtree,
                             max depth of right subtree)
                             + 1
     (d) Return max_depth

Time Complexity: O(n)
"""
from binary_tree import *
def max_depth(node):
    if node is None:
        return 0

    return 1 + max(max_depth(node.left), max_depth(node.right))

def max_depth_1(node):
    if node is None:
        return 0
    else:
        l_depth = max_depth(node.left)
        r_depth = max_depth(node.right)

        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1

if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)

    print max_depth(t)
