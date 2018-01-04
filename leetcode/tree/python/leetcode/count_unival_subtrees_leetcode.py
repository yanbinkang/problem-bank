from binary_tree import *

"""
https://leetcode.com/problems/count-univalue-subtrees/

http://www.geeksforgeeks.org/find-count-of-singly-subtrees/
"""
def count_unival_subtrees(root):
    count = [0]

    count_single_rec(root, count)

    return count[0]

def count_single_rec(root, count):
    if root is None:
        return True

    left = count_single_rec(root.left, count)
    right = count_single_rec(root.right, count)

    if left == False or right == False:
        return False

    if root.left and root.left.val != root.val:
        return False

    if root.right and root.right.val != root.val:
        return False

    count[0] += 1
    return True

if __name__ == '__main__':
    tree = BinaryTree(5)
    tree.insert_left(1)
    tree.insert_right(5)

    tree.left.insert_left(5)
    tree.left.insert_right(5)
    tree.right.insert_right(5)

    print(count_unival_subtrees(tree))
