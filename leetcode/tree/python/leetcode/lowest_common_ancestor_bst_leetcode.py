from binary_tree import *

"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself)."

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""

# https://youtu.be/TIoCCStdiFo
# other solutions: https://discuss.leetcode.com/topic/18387/3-lines-with-o-1-space-1-liners-alternatives/2

# O(h) time and space where h is the height of the bst
"""
solution: Use BST property - every node on the left side is less than the root node and every node on the right side is greater than the root node, and this is recursively true for every node

1. start from root node. if root node is greater than both nodes whose LCA we're looking for, we go left else go right. As the root is greater than both nodes we're looking for, it means these nodes are smaller than the root, so check the left.

2. If the root node is smaller than both nodes we're looking for, then both these nodes are greater than the root node. So look right.

3. Else we've found the LCA! Fuck yea!


Otherwise that node is the LCA.
"""
def lowest_common_ancestor(root, p, q):
    if root.val > max(p.val, q.val): # root is greater than both p and q
        return lowest_common_ancestor(root.left, p, q)
    elif root.val < min(p.val, q.val): # root is less than both q and q
        return lowest_common_ancestor(root.right, p, q)
    else:
      return root.val
"""
                                             10
                                           /    \
                                        -10     30
                                          \    /  \
                                           8  25   60
                                          / \   \   \
                                         6   9  28   78
"""

if __name__ == '__main__':
    tree = BinaryTree(10)
    tree.insert_left(-10)
    tree.insert_right(30)

    tree.left.insert_right(8)
    tree.left.right.insert_left(6)
    tree.left.right.insert_right(9)

    tree.right.insert_left(25)
    tree.right.insert_right(60)
    tree.right.left.insert_right(28)
    tree.right.right.insert_right(78)

    n1 = tree.right.left.right
    n2 = tree.right.right.right
    # 28, 78 => 30

    print(lowest_common_ancestor(tree, n1, n2))
