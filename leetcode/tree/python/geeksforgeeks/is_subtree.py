"""
http://www.geeksforgeeks.org/check-if-a-binary-tree-is-subtree-of-another-binary-tree/

Given two binary trees, check if the first tree is subtree of the second one. A subtree of a tree T is a tree S consisting of a node in T and all of its descendants in T. The subtree corresponding to the root node is the entire tree; the subtree corresponding to any other node is called a proper subtree.

For example, in the following case, tree S is a subtree of tree T.


            Tree 1 (t)

              26
            /   \
          10     3
        /    \     \
      4       6      3
       \
        30


        Tree 2 (s)

          10
        /    \
      4       6
       \
        30


Time Complexity: Time worst case complexity of above solution is O(mn) where m and n are number of nodes in given two trees.

Time complexity: O(m * n) where m and n are number of nodes in the trees
Space complexity: O(n) where n is the number of nodes in t (the larger tree)
"""
from binary_tree import *
def is_subtree(t, s):
    # base case
    if t is None:
        return False

    if is_same_tree(t, s):
        return True

    return is_subtree(t.left, s) or is_subtree(t.right, s)


def is_same_tree(t1, t2):
    if t1 is None and t2 is None: return True

    if t1 is None or t2 is None: return False

    return t1.val == t2.val and\
            is_same_tree(t1.left, t2.left) and\
            is_same_tree(t1.right, t2.right)


if __name__ == '__main__':
    s = BinaryTree(10)
    s.insert_left(4)
    s.insert_right(6)
    s.left.insert_right(30)

    t = BinaryTree(26)
    t.insert_left(10)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(6)
    t.left.left.insert_right(30)
    t.right.insert_right(3)

    print is_subtree(t, s)
