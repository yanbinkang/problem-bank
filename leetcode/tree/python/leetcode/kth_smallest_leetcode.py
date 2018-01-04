from binary_tree import *

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

def kth_smallest(root, k):
    if root is None:
        return None

    result = []

    in_order(root, result)

    return result[k - 1]

def in_order(root, result):
    if root:
        in_order(root.left, result)
        result.append(root.val)
        in_order(root.right, result)
