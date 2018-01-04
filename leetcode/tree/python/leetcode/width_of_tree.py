from binary_tree import *

"""
http://www.geeksforgeeks.org/maximum-width-of-a-binary-tree/

Use queue based level order traversal, keep track of node count at each level in array. return max of nodes in array.
"""

def width_of_tree(tree):
    queue = []
    level_count = []

    queue.append(tree)

    while queue:
        count = 0
        for _ in range(len(queue)):
            root = queue.pop()
            count += 1
            if root.left:
                queue.insert(0, root.left)

            if root.right:
                queue.insert(0, root.right)

        # print(str(count) + "\n")
        level_count.insert(0, count)

    return max(level_count)

if __name__ == '__main__':
    tree = BinaryTree(1)

    tree.insert_left(2)
    tree.insert_right(3)

    tree.left.insert_left(4)
    tree.left.insert_right(5)
    tree.right.insert_right(8)

    tree.right.right.insert_left(8)
    tree.right.right.insert_right(7)

    print(width_of_tree(tree))
