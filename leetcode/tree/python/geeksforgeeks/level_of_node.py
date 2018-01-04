"""
http://www.geeksforgeeks.org/get-level-of-a-node-in-a-binary-tree/

iven a Binary Tree and a key, write a function that returns level of the key.
"""
from binary_tree import *
def level_of_node(root, key):
    if root is None: return

    queue = [root]

    level = 0

    while queue:
        level += 1
        for _ in range(len(queue)):
            node = queue.pop()

            if node.val == key: return level

            if node.left:
                queue.insert(0, node.left)

            if node.right:
                queue.insert(0, node.right)

    return 0

def level_of_node_rec(root, key):
    return helper(root, key, 1)

def helper(root, key, level):
    if root is None: return 0

    if root.val == key:
        return level

    downlevel = helper(root.left, key, level + 1)

    if downlevel:
        return downlevel

    downlevel = helper(root.right, key, level + 1)
    return downlevel





if __name__ == '__main__':
    t = BinaryTree(3)
    t.insert_left(2)
    t.insert_right(5)
    t.left.insert_left(1)
    t.left.insert_right(4)

    print level_of_node(t, 4)
    print('\n')
    print level_of_node_rec(t, 4)
