"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]

https://discuss.leetcode.com/topic/39196/python-modified-level-order-traversal

idea: initial root is at level = 0. every node's left child is at level - 1, right child is level + 1. Use hash map with levels as key and node.val as values. Sort hasm map keys and return corresponding hash map values.
"""
import collections
from binary_tree import BinaryTree

def vertical_order(root):
    queue = []

    if root is None: return queue

    queue.append([root, 0])

    # output = {}
    dic = collections.defaultdict(list)

    while queue:
        for _ in range(len(queue)):
            node, level = queue.pop()

            dic[level].append(node.val)


            if node.left:
                queue.insert(0, [node.left, level - 1])
            if node.right:
                queue.insert(0, [node.right, level + 1])

    return [dic[key] for key in sorted(dic)]

    # sorted_keys = sorted(dic)
    # vert_order = []

    # for key in sorted_keys:
    #     vert_order.append(dic[key])

    # return vert_order


if __name__ == '__main__':
    tree = BinaryTree(3)
    tree.insert_left(9)
    tree.insert_right(20)

    tree.right.insert_left(15)
    tree.right.insert_right(7)

    print vertical_order(tree)
