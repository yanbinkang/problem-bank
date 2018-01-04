"""
An empty tree is height-balanced. A non-empty binary tree T is balanced if:
1) Left subtree of T is balanced
2) Right subtree of T is balanced
3) The difference between heights of left subtree and right subtree is not more than 1.
"""
def height_balanced(root):
    if root is None: return True

    left = height(root.left)
    right = height(root.right)

    return abs(left - right) <= 1 and\
            height_balanced(root.left) and\
            height_balanced(root.right)


def height(root):
    if root is None: return 0

    return 1 + max(height(root.left), height(root.right))
