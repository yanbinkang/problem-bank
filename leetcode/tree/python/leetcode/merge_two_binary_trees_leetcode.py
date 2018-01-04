"""
https://leetcode.com/problems/merge-two-binary-trees/#/description

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
        Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7

Output:
Merged tree:
         3
        / \
       4   5
      / \   \
     5   4   7

solution: https://discuss.leetcode.com/topic/92105/java-solution-6-lines-tree-traversal
"""
from binary_tree import *
def merge_trees(t1, t2):

    if t1 is None and t2 is None: return

    val = (t1.val if t1 else 0) + (t2.val if t2 else 0)

    root = BinaryTree(val)

    root.left = merge_trees( t1.left if t1 else None, t2.left if t2 else None )
    root.right = merge_trees( t1.right if t1 else None, t2.right if t2 else None )

    return root

if __name__ == '__main__':
    t1 = BinaryTree(1)
    t1.insert_left(3)
    t1.insert_right(2)
    t1.left.insert_left(5)

    t2 = BinaryTree(2)
    t2.insert_left(1)
    t2.insert_right(3)
    t2.left.insert_right(4)
    t2.right.insert_right(7)

    res = merge_trees(t1, t2)

    # test level order traversal
    queue = [res]

    data = []

    while queue:
        collection = []
        for _ in range(len(queue)):
            node = queue.pop()
            collection.append(node.val)

            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

        data.append(collection)

    print data




