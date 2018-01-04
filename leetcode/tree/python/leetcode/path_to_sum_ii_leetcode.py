"""
https://leetcode.com/problems/path-sum-ii/#/description

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from binary_tree import *

def path_sum(root, sum):
    result = []
    if root == None:
        return result

    helper(root, sum, [], result)

    return result

def helper(root, sum, path, result):
    if root == None:
        return None

    path.append(root.val)

    if root.left == None and root.right == None:
        if root.val == sum:
            result.append([] + path)
    else:
        helper(root.left, sum - root.val, path, result)
        helper(root.right, sum - root.val, path, result)

    path.pop()

def path_sum_iterative(root, sum):
    result = []

    if not root: return result

    stack = [(root, sum, [])]

    while stack:
        node, sum, path = stack.pop()

        if node.left is None and node.right is None:
            if node.val == sum:
                result.append(path + [node.val])

        if node.right:
            stack.append( (node.right, sum - node.val, path + [node.val]) )

        if node.left:
            stack.append( (node.left, sum - node.val, path + [node.val]) )

    return result




if __name__ == '__main__':
    tree = BinaryTree(5)
    tree.insert_left(4)
    tree.insert_right(8)

    tree.left.insert_left(11)
    tree.right.insert_left(13)
    tree.right.insert_right(4)

    tree.left.left.insert_left(7)
    tree.left.left.insert_right(2)
    tree.right.right.insert_left(5)
    tree.right.right.insert_right(1)

    print(path_sum(tree, 22))

    print(path_sum_iterative(tree, 22))
