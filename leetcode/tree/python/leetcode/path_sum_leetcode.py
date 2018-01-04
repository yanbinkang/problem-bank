"""
https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
from binary_tree import *
def has_path_sum(root, sum):
    if root == None:
        return False

    if root.left == None and root.right == None:
        return root.val == sum

    return has_path_sum(root.left, sum - root.val) or has_path_sum(root.right, sum - root.val)


def has_path_sum_iterative(root, sum):
    done = False

    if not root: return done

    stack = [(root, sum)]


    while stack and not done:
        node, sum = stack.pop()

        if node.left is None and node.right is None:
            done = node.val == sum

            if done: return done

        if node.right:
            stack.append( (node.right, sum - node.val) )

        if node.left:
            stack.append( (node.left, sum - node.val) )

    return False

if __name__ == '__main__':
    t = BinaryTree(5)
    t.insert_left(4)
    t.insert_right(8)
    t.left.insert_left(11)
    t.left.left.insert_left(7)
    t.left.left.insert_right(2)

    t.right.insert_left(13)
    t.right.insert_right(4)
    t.right.right.insert_right(1)

    print has_path_sum(t, 22)
    print has_path_sum_iterative(t, 22)

    t2 = BinaryTree(1)
    t2.insert_right(2)

    print has_path_sum(t2, 3)
    print has_path_sum_iterative(t2, 3)


