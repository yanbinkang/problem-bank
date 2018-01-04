from binary_tree import *

"""
https://leetcode.com/problems/unique-binary-search-trees-ii/
https://www.youtube.com/watch?v=dMFXgAhvdYY
"""

def generate_trees(n):
    if n == 0: return []

    return build_tree(1, n)

def build_tree(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left = build_tree(start, i - 1)
        right = build_tree(i + 1, end)

        for l in left:
            for r in right:
                node = BinaryTree(i)
                node.left = l
                node.right = r
                result.append(node)

    return result

if __name__ == '__main__':
    print generate_trees(3)
