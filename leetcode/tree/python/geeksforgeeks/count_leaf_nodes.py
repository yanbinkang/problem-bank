"""
http://www.geeksforgeeks.org/write-a-c-program-to-get-count-of-leaf-nodes-in-a-binary-tree/
"""
from binary_tree import *
def count_leaf(root):
    if root is None: 0

    count = [0]

    count_leaf_rec(root, count)

    return count[0]

def count_leaf_rec(root, count):
    if root is None: return

    if root.left is None and root.right is None:
        count[0] += 1

    count_leaf_rec(root.left, count)
    count_leaf_rec(root.right, count)

"""
getLeafCount(node)
1) If node is NULL then return 0.
2) Else If left and right child nodes are NULL return 1.
3) Else recursively calculate leaf count of the tree using below formula.
    Leaf count of a tree = Leaf count of left subtree +
                                 Leaf count of right subtree

Time and Space Complexity: O(n)
"""

def get_leaf_count(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    else:
        return get_leaf_count(root.left) + get_leaf_count(root.right)

if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)

    print count_leaf(t)
    print('\n')
    print get_leaf_count(t)
