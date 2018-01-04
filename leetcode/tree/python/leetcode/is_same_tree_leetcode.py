"""
https://leetcode.com/problems/same-tree/#/description

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

from binary_tree import *

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False

    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# https://discuss.leetcode.com/topic/7513/my-non-recursive-metho
def is_same_tree_iterative(p, q):
    stack = [(p, q)]

    while stack:
        node1, node2 = stack.pop()

        if node1 is None and node1 is None:
            continue

        if node1 is None and node2 is not None:
            return False

        if node1.val == node2.val:
            stack.append( (node1.left, node2.left) )
            stack.append( (node1.right, node2.right) )
        else:
            return False

    return True



if __name__ == '__main__':
    t1 = BinaryTree(1)
    t1.insert_left(2)
    t1.insert_right(3)

    t2 = BinaryTree(1)
    t2.insert_left(2)
    t2.insert_right(3)

    t3 = BinaryTree(4)
    t3.insert_left(5)
    t3.insert_right(3)

    print(is_same_tree(t1, t2))
    print("\n")
    print(is_same_tree(t1, t3))
    print("\n")
    print is_same_tree_iterative(t1, t2)
    print('\n')
    print is_same_tree_iterative(t1, t3)
