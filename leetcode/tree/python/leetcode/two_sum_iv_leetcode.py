"""
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

algorithm: similar to 'two sum imput array sorted'.

1. Do inorder traversal of binary tree and store the results in an array.

2. Use two pointer approach to find to find target sum since array is sorted.

Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def findTarget(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: bool
    """
    result = []
    inorder(root, result)

    left, right = 0, len(result) - 1

    while left < right:
        total = result[left] + result[right]

        if total == k:
            return True
        elif total < k:
            left += 1
        elif total > k:
            right -= 1

    return False

    def inorder(root, result):
        if root:
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)
