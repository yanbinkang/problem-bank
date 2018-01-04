"""
https://leetcode.com/problems/most-frequent-subtree-sum/

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.

https://discuss.leetcode.com/topic/77769/python-easy-understand-solution
"""
from binary_tree import *
def find_frequent_tree_sum(root):
    if not root: return []

    hash_map = {}

    helper(root, hash_map)

    most_frequent = max(hash_map.values())

    return [i for i in hash_map.keys() if hash_map[i] == most_frequent]

def helper(root, hash_map):
    if root == None:
        return 0
    else:
        val = helper(root.left, hash_map) + helper(root.right, hash_map) + root.val
        hash_map[val] = hash_map.get(val, 0) + 1
        return val


if __name__ == '__main__':
    tree = BinaryTree(5)
    tree.insert_left(2)
    tree.insert_right(-3)

    print find_frequent_tree_sum(tree)
