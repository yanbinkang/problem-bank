"""
https://leetcode.com/problems/find-bottom-left-tree-value/

Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7
Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""
from binary_tree import *
def find_bottom_left_value(root):
    result = None

    queue = [root]

    while queue:
        node_count = 0

        for _ in range(len(queue)):

            node_count += 1
            node = queue.pop()

            if node_count == 1:
                result = node.val

            if node.left:
                queue.insert(0, node.left)
            if node.right:
                queue.insert(0, node.right)

    return result

def find_bottom_left_value_1(root):
  result = None

  queue = [root]

  while queue:
      for i in range(len(queue)):
          node = queue.pop()

          if i == 0:
              result = node.val

          if node.left:
              queue.insert(0, node.left)
          if node.right:
              queue.insert(0, node.right)

  return result

"""
Doing BFS right to left means we can simply return the last node's value and don't have to keep track of the first node in the current tree row.

https://discuss.leetcode.com/topic/78981/right-to-left-bfs-python-java
"""
def find_bottom_left_value_2(root):
    queue = [root]

    while queue:
        root = queue.pop()

        if root.right:
            queue.insert(0, root.right)

        if root.left:
            queue.insert(0, root.left)

    return root.val


if __name__ == '__main__':
    tree = BinaryTree(0)
    tree.insert_left(2)
    tree.insert_right(3)

    tree.left.insert_left(4)
    tree.right.insert_left(5)
    tree.right.insert_right(6)

    tree.right.left.insert_left(7)


    print find_bottom_left_value(tree)
    print('\n')
    print find_bottom_left_value_1(tree)
    print('\n')
    print find_bottom_left_value_2(tree)
