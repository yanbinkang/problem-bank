from binary_tree import *

"""
https://leetcode.com/problems/find-leaves-of-binary-tree/

https://discuss.leetcode.com/topic/49200/simple-java-recursive-1ms-solution

This is pretty straight forward but the general idea is to simply prune the leaves at each iteration of the while loop until the root itself is pruned. We can do this using the x = change(x) paradigm for modifying a tree. Whenever we come across a leaf node, we know we must add it to our result but then we prune it by just returning null.
"""
def find_leaves(root):
    result = []

    if root is None:
        return result

    while root:
        leaves = []
        root = remove_leaves(root, leaves)
        result.append(leaves)

    return result

def remove_leaves(root, result):
    if root is None:
        return None

    if root.left == None and root.right == None:
        result.append(root.val)
        return None

    root.left = remove_leaves(root.left, result)
    root.right = remove_leaves(root.right, result)

    return root


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)

    tree.left.insert_left(4)
    tree.left.insert_right(5)

    print find_leaves(tree)

    tree2 = BinaryTree(2)
    tree2.insert_left(1)
    tree2.insert_right(4)
    tree2.left.insert_left(3)
    tree2.right.insert_right(5)

    print('\n')
    print find_leaves(tree2)
