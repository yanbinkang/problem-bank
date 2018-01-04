"""
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

https://discuss.leetcode.com/topic/21559/python-solutions-dfs-stack-bfs-queue-dfs-recursively
"""
from binary_tree import *
def binary_tree_paths(root):
    res = []

    if root:
        tree_paths(root, "", res)

    return res

def tree_paths(root, string, collection):
    if root.left == None and root.right == None:
        collection.append(string + str(root.val))

    if root.left:
        tree_paths(root.left, string + str(root.val) + "->", collection)
    if root.right:
        tree_paths(root.right, string + str(root.val) + "->", collection)

def binary_tree_paths_iterative(root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, string = stack.pop()
        if not node.left and not node.right:
            res.append(string + str(node.val))
        if node.right:
            stack.append((node.right, string + str(node.val) + "->"))
        if node.left:
            stack.append((node.left, string + str(node.val) + "->"))
    return res

if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.left.insert_right(5)

    print(binary_tree_paths(tree))
    print('\n')
    print binary_tree_paths_iterative(tree)
