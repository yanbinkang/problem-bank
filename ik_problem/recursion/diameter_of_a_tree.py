"""
solution: http://www.geeksforgeeks.org/diameter-of-a-binary-tree/
"""

def diameter(root):
    if root == None:
        return 0

    # get the height of left and right sub-trees
    l_height = height(root.left_child)
    r_height = height(root.right_child)

    # get diameter of left and right sub-trees
    l_diameter = diameter(root.left_child)
    r_diameter = diameter(root.right_child)

    """
    return max of the following three
    1) Diameter of left subtree
    2) Diameter if right subtree
    3) Height of left subtree + height of right subtree + 1
    """
    return max(l_height, r_height + 1, max(l_diameter, r_diameter))


def height(root):
    if root == None:
        return 0

    return 1 + max(height(root.left_child), height(root.right_child))
