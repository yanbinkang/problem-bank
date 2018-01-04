"""
http://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/

Binary Tree where the value of a node is equal to sum of the nodes present in its left subtree and right subtree. An empty tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.

Following is an example of SumTree.

          26
        /   \
      10     3
    /    \     \
  4      6      3

Method1 algo: Get the sum of nodes in left subtree and right subtree. Check if the sum calculated is equal to root's data. Also, recursively check if the left and right subtrees are SumTrees.

Method2 algo: The Method 1 uses helper() to get the sum of nodes in left and right subtrees. The method 2 uses following rules to get the sum directly.

1 - If the node is a leaf node then sum of subtree rooted with this node is equal to value of this node.

1 - If the node is not a leaf node then sum of subtree rooted with this node is twice the value of this node (Assuming that the tree rooted with this node is SumTree)
"""
from binary_tree import *
def is_sumtree_rec(root):
    if root is None or (root.left is None and root.right is None):
        return True

    left = helper(root.left)
    right = helper(root.right)

    return root.val ==  left + right\
        and is_sumtree_rec(root.left)\
        and is_sumtree_rec(root.right)

def helper(root):
    if root is None: return 0

    return root.val + helper(root.left) + helper(root.right)

# FIX ME!
def is_sumtree_rec_2(node):
    # if the node is None or its a leaf then return True
    if node is None or is_leaf(node):
        return True

    if is_sumtree_rec_2(node.left) and is_sumtree_rec_2(node.right):
        # get the sum of nodes in left subtree
        if node.left is None:
            ls = 0
        elif is_leaf(node.left):
            ls = node.left.val
        else:
            ls = 2 * (node.left.data)

        # get the sum of nodes in right subtree
        if node.right is None:
            rs = 0
        elif is_leaf(node.right):
            rs = node.right.val
        else:
            rs = 2 * (node.right.data)


        if node.val == rs + ls:
            return True
        else:
            return False



def is_leaf(node):
    if node is None: return 0

    if node.left is None and node.right is None:
        return 0

    return False


if __name__ == '__main__':
    t = BinaryTree(26)
    t.insert_left(10)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(6)
    t.right.insert_right(3)

    print is_sumtree_rec(t)
    print is_sumtree_rec_2(t)
