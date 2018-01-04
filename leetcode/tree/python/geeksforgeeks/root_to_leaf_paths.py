"""
http://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/

Given a binary tree, print all root-to-leaf paths
"""
from binary_tree import *
def print_paths_recur(root):
    if root is None: return

    dfs(root, '')

def dfs(root, string):
    if root is None: return

    if root.left is None and root.right is None:
        string += str(root.val)

        print string
        print('\n')

    dfs(root.left, string + str(root.val) + ' -> ')
    dfs(root.right,  string + str(root.val) + ' -> ')


def print_paths_iterative(root):
    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()

        if node.left is None and node.right is None:
            print path
            print('\n')

        if node.right:
            stack.append( (node.right, path + ' -> ' + str(node.right.val)) )

        if node.left:
            stack.append( (node.left, path + ' -> ' + str(node.left.val)) )

if __name__ == '__main__':
    t = BinaryTree(10)
    t.insert_left(8)
    t.insert_right(2)
    t.left.insert_left(3)
    t.left.insert_right(5)
    t.right.insert_left(2)

    print_paths_recur(t)
    print('\n')
    print_paths_iterative(t)

