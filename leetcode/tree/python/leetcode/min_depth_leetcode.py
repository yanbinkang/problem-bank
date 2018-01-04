from binary_tree import *

"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

def min_depth(root):
    if root == None: return 0

    if root.left and root.right:
        return 1 + min(min_depth(root.left), min_depth(root.right))
    else:
        return 1 + max(min_depth(root.left), min_depth(root.right))


"""
The idea is to traverse the given Binary Tree. For every node, check if it is a leaf node. If yes, then return 1. If not leaf node then if left subtree is NULL, then recur for right subtree. And if right subtree is NULL, then recur for left subtree. If both left and right subtrees are not NULL, then take the minimum of two heights.
The above method may end up with complete traversal of Binary Tree even when the topmost leaf is close to root.
 solution: http://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
 """
def min_depth_rec(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return min_depth_rec(root.right) + 1

    if root.right is None:
        return min_depth_rec(root.left) + 1

    return min(min_depth_rec(root.left), min_depth_rec(root.right)) + 1

"""
A better solution is to do level order traversal. While doing traversal returns depth of the first encountered leaf node.

http://www.geeksforgeeks.org/find-minimum-depth-of-a-binary-tree/
"""
def min_depth_level_order_helper(root):
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

    print min_depth_level_order_helper(tree)
    print("\n")
    print min_depth(tree)
    print("\n")
    print min_depth_rec(tree)


