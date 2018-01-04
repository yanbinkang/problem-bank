"""
http://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/

Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.
"""
from binary_tree import *
def tree_mirror(node):
    if node is None:
        return

    root = BinaryTree(node.val)

    root.left = tree_mirror(node.right)
    root.right = tree_mirror(node.left)

    return root

if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(3)
    t.insert_right(2)
    t.right.insert_left(5)
    t.right.insert_right(4)

    # test
    mirror = tree_mirror(t)

    queue = [mirror]
    result = []

    while queue:
        col = []
        for _ in range(len(queue)):
            node = queue.pop()

            col.append(node.val)

            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

        result.append(col)

    print result

