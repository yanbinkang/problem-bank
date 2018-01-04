from binary_tree import *
"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

Solution: morris algorithm for tree traversal

O(n)
"""
def flatten(root):
    if root == None:
        return None

    current = root

    while current:
        if current.left:
            predecessor = current.left

            while predecessor.right:
                predecessor = predecessor.right

            predecessor.right = current.right
            current.right = current.left
            current.left = None

        current = current.right


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(5)

    tree.left.insert_left(3)
    tree.left.insert_right(4)

    tree.right.insert_right(6)

    flatten(tree)

    while tree:
        print(str(tree.val) + "\n")
        tree = tree.right
