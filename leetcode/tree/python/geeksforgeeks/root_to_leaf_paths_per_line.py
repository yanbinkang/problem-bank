"""
http://www.geeksforgeeks.org/given-a-binary-tree-print-out-all-of-its-root-to-leaf-paths-one-per-line/
"""
from binary_tree import *
def print_paths(root):
    if root is None:
        return

    result = []

    print_paths_recur(root, result)


def print_paths_recur(root, result):
    if root is None: return

    result.append(root.val)

    if root.left is None and root.right is None:
        print result
    else:
        print_paths_recur(root.left, result)
        print_paths_recur(root.right, result)

    result.pop()

def print_paths_iterative(root):
    stack = [(root, [])]
    result = []

    while stack:
        node, temp_list = stack.pop()

        if node.left is None and node.right is None:
            result.append(temp_list + [node.val])

        if node.right:
            stack.append((node.right, temp_list + [node.val]))
        if node.left:
            stack.append((node.left, temp_list + [node.val]))

    return result



if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)

    print_paths(t)
    print print_paths_iterative(t)
