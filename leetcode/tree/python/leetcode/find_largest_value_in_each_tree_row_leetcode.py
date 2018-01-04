"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""
from binary_tree import *
def largest_values(root):
    result = []

    if root is None: return result

    queue = [root]

    while queue:
        _max = float('-inf')
        for i in range(len(queue)):
            node = queue.pop()

            _max = max(_max, node.val)

            if node.left:
                queue.insert(0, node.left)

            if node.right:
                queue.insert(0, node.right)

        result.append(_max)

    return result


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(3)
    tree.insert_right(2)

    tree.left.insert_left(5)
    tree.left.insert_right(3)

    tree.right.insert_right(9)

    print largest_values(tree)
