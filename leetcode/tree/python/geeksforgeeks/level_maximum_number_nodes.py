"""
http://www.geeksforgeeks.org/level-maximum-number-nodes/

Find the level in a binary tree which has maximum number of nodes. The root is at level 0.

Examples:

Input :
       2
    /     \
   1        3
 /   \       \
4     6        8
     /
    5

Output : 2

        2
     /     \
    1        3
  /   \       \
 4    6        8        [Level with maximum nodes = 3]
     /
    5
"""
from binary_tree import *
def max_level_node(root):
    queue = []
    queue.append(root)

    d = {}

    level = 0

    while queue:
        d[level] = len(queue)

        for i in range(len(queue)):
            node = queue.pop()

            if node.left:
                queue.insert(0, node.left)

            if node.right:
                queue.insert(0, node.right)

        level += 1

    sorted_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)

    return sorted_dict[0][0]

if __name__ == '__main__':
    tree = BinaryTree(2)

    tree.insert_left(1)
    tree.insert_right(3)

    tree.left.insert_left(4)
    tree.left.insert_right(6)
    tree.right.insert_right(8)

    tree.left.right.insert_left(6)

    print max_level_node(tree)
