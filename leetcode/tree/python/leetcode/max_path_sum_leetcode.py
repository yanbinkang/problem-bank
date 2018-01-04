from binary_tree import BinaryTree

"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

https://discuss.leetcode.com/topic/4407/accepted-short-solution-in-java
"""

def max_path_sum(root):
    max_value = [float('-inf')]

    max_path_down(root, max_value)
    return max_value[0]

def max_path_down(root, max_value):
    if root is None: return 0

    left = max(0, max_path_down(root.left, max_value))
    right = max(0, max_path_down(root.right, max_value))
    max_value[0] = max(max_value[0], left + right + root.val)

    return max(left, right) + root.val


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)

    print max_path_sum(tree)
