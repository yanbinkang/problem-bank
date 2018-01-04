"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/


Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7

Output: [3, 14.5, 11]

Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:

    - The range of node's value is in the range of 32-bit signed integer.
"""
from binary_tree import *
def average_of_levels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    queue, result = [root], []

    while queue:
        total = 0
        count = 0
        for _ in range(len(queue)):
            node = queue.pop()

            total += node.val
            count += 1

            if node.left:
                queue.insert(0, node.left)

            if node.right:
                queue.insert(0, node.right)

        result.append(total * 1.0 / count)

    return result

# ref: https://leetcode.com/articles/average-of-levels/#approach-2-breadth-first-search-accepted
def averageOfLevels(root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    queue, result = [root], []

    while queue:
        count, total = 0, 0
        temp = []

        while queue:
            node = queue.pop()

            total += node.val
            count += 1

            if node.left:
                temp.append(node.left)

            if node.right:
                temp.append(node.right)

        result.append(total * 1.0 / count)
        queue = temp

    return result

if __name__ == '__main__':
    t = BinaryTree(3)
    t.insert_left(9)
    t.insert_right(20)
    t.right.insert_left(15)
    t.right.insert_right(7)

    print average_of_levels(t)
