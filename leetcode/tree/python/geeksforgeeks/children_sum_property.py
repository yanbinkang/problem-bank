"""
http://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/

Given a binary tree, write a function that returns true if the tree satisfies below property.

For every node, data value must be equal to sum of data values in left and right children. Consider data value as 0 for NULL children. Below tree is an example
"""
from binary_tree import *
def is_sum_property(node):

    if node is None or (node.left is None and node.right is None):
        return True

    left_data = node.left.val if node.left else 0
    right_data = node.right.val if node.right else 0


    if node.val == left_data + right_data and\
        is_sum_property(node.left) and\
        is_sum_property(node.right):
            return True
    else:
        return False

def is_sum_property_iterative(node):
    queue = [node]

    while queue:
        for _ in range(len(queue)):
            n = queue.pop()

            if n.left or n.right:
                left = n.left.val if n.left else 0
                right = n.right.val if n.right else 0

                if n.val != left + right:
                    return False

            if n.left:
                queue.insert(0, n.left)

            if n.right:
                queue.insert(0, n.right)

    return True

if __name__ == '__main__':
    t = BinaryTree(10)
    t.insert_left(8)
    t.insert_right(2)
    t.left.insert_left(3)
    t.left.insert_right(5)
    t.right.insert_left(2)

    print is_sum_property_iterative(t)
    print('\n')
    print is_sum_property(t)

