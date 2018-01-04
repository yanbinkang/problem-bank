from binary_tree import *

"""
https://leetcode.com/problems/closest-binary-search-tree-value/

https://discuss.leetcode.com/topic/22590/4-7-lines-recursive-iterative-ruby-c-java-python

https://discuss.leetcode.com/topic/37526/clean-python-code
"""

def closest_value(root, target):
    path = []

    while root:
        path.append(root.val)
        root = root.left if target < root.val else root.right

    return min(path[::-1], key=lambda x: abs(target - x))

def closest_value_2(root, target):
    closest = root.val

    while root:
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        root = root.left if target < root.val else root.right

    return closest

if __name__ == '__main__':
    tree =  BinaryTree(17)
    tree.insert_left(5)
    tree.insert_right(35)

    tree.left.insert_left(2)

    tree.right.insert_left(29)

    print closest_value(tree, 1)
    """
                            17
                          /    \
                         5      35
                       /        /
                      2        29
    """
