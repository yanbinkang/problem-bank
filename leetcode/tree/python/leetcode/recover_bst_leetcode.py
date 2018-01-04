from binary_tree import *

"""
https://leetcode.com/problems/recover-binary-search-tree/

https://discuss.leetcode.com/topic/29161/share-my-solutions-and-detailed-explanation-with-recursive-iterative-in-order-traversal-and-morris-traversal/2

https://discuss.leetcode.com/topic/9305/detail-explain-about-how-morris-traversal-finds-two-incorrect-pointer/2
"""

def recover_tree(root):
    current = root
    previous = None
    first = second = None

    while current:
        # detect incorrect nodes here
        if previous and previous.val >= current.val:
            if first is None:
                first = previous
            second = current

        if current.left == None:
            previous = current
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right == None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                previous = current
                current = current.right

    # swap incorrect nodes here
    temp = first.val
    first.val = second.val
    second.val = temp

def test_inorder(root, res=[]):
    if root:
        test_inorder(root.left, res)
        res.append(root.val)
        test_inorder(root.right, res)

    return res


if __name__ == '__main__':
    tree = BinaryTree(10)
    tree.insert_left(4)
    tree.insert_right(20)

    tree.left.insert_left(7)
    tree.left.insert_right(8)
    tree.right.insert_left(11)
    tree.right.insert_right(22)

    tree2 = BinaryTree(0)
    tree2.insert_left(1)

    print test_inorder(tree, [])
    recover_tree(tree)
    print('\n')
    print test_inorder(tree, [])
    print('\n')
    print test_inorder(tree2, [])
    recover_tree(tree2)
    print test_inorder(tree2, [])


