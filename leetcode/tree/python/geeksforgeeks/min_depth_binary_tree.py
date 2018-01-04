"""
A better solution is to do level order traversal. While doing traversal returns depth of the first encountered leaf node.

http://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
"""
from binary_tree import *
def min_depth(root):
    q = []
    depth = 0
    if root == None:
        return depth
    q.append(root)

    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.pop()

            if node.left is None and node.right is None:
                return depth

            if node.left:
                q.insert(0, node.left)
            if node.right:
                q.insert(0, node.right)


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.left.insert_left(4)
    tree.left.insert_right(5)

    print min_depth(tree)
