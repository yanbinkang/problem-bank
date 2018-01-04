"""
http://www.geeksforgeeks.org/print-nodes-at-k-distance-from-root/

Given a root of a tree, and an integer k. Print all the nodes which are at k distance from root.

For example, in the below tree, 4, 5 & 8 are at distance 2 from root.
            1
          /   \
        2      3
      /  \    /
    4     5  8
"""
from binary_tree import *
def print_k_distance(root, k): # level order traversal
    if root is None: return

    queue = [root]

    while queue:
        if k == 0:
            print ' '.join([str(node.val) for node in reversed(queue)])
            return

        for _ in range(len(queue)):
            node = queue.pop()

            if node.left:
                queue.insert(0, node.left)

            if node.right:
                queue.insert(0, node.right)

        k -= 1

def print_k_distance_rec(root, k):
    if root is None: return

    if k == 0:
        print root.val,

    print_k_distance_rec(root.left, k - 1)
    print_k_distance_rec(root.right, k- 1)


if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)
    t.right.insert_left(8)

    print_k_distance(t, 2)
    print('\n')
    print_k_distance_rec(t, 2)
