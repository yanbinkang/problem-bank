from binary_tree import *

"""
https://leetcode.com/problems/delete-node-in-a-bst/

https://discuss.leetcode.com/topic/65792/recursive-easy-to-understand-java-solution
Steps:

1) Recursively find the node that has the same value as the key, while setting the left/right nodes equal to the returned subtree
2) Once the node is found, have to handle the below 4 cases
    - node doesn't have left or right - return null
    - node only has left subtree- return the left subtree
    - node only has right subtree- return the right subtree
    - node has both left and right - find the minimum value in the right subtree, set that value to the currently found node, then recursively delete the minimum value in the right subtree

"""

def delete_node(root, key):
    if root == None:
        return None

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left

        min_node = find_min(root.right)
        root.val = min_node.val
        root.right = delete_node(root.right, root.val)

    return root

def find_min(node):
    while node.left:
        node = node.left

    return node
