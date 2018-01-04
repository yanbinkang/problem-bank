"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/#/description

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

from binary_tree import *

def sum_numbers(root):
    total = 0

    if root == None:
        return total

    res = []

    helper(root, "", res)

    for i in res:
        total += int(i)

    return total

def helper(root, string, collection):
    if root.left == None and root.right == None:
        collection.append(string + str(root.val))

    if root.left:
        helper(root.left, string + str(root.val), collection)

    if root.right:
        helper(root.right, string + str(root.val), collection)

# alternate solution
def sum_numbers_alt(root):
    return _sum(root, 0)

def _sum(root, num):
    if root == None:
        return 0

    if root.left == None and root.right == None:
        return num * 10 + root.val

    return _sum(root.left, num * 10 + root.val) + _sum(root.right, num * 10 + root.val)


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)

    print(sum_numbers(tree))

    print("\n")

    print(sum_numbers_alt(tree))
