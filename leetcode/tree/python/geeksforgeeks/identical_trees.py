"""
http://www.geeksforgeeks.org/write-c-code-to-determine-if-two-trees-are-identical/

Algorithm:

sameTree(tree1, tree2)
1. If both trees are empty then return 1.
2. Else If both trees are non -empty
     (a) Check data of the root nodes (tree1->data ==  tree2->data)
     (b) Check left subtrees recursively  i.e., call sameTree(
          tree1->left_subtree, tree2->left_subtree)
     (c) Check right subtrees recursively  i.e., call sameTree(
          tree1->right_subtree, tree2->right_subtree)
     (d) If a,b and c are true then return 1.
3  Else return 0 (one is empty and other is not)
"""
from binary_tree import *
def identical_trees(a, b):
    if a is None and b is None:
        return True

    return a.val == b.val and\
            identical_trees(a.left, b.left) and\
            identical_trees(a.right, b.right)

    return False

"""
http://www.geeksforgeeks.org/iterative-function-check-two-trees-identical/

Iterative solution

The idea is to use level order traversal. We traverse both trees simultaneously and compare the data whenever we dequeue and item from queue.
"""
def are_identical(a, b):
    if a is None and b is None:
        return True

    if a is None or b is None:
        return False

    q1, q2 = [], []

    q1.append(a)
    q2.append(b)

    while q1 and q2:
        n1 = q1.pop()
        n2 = q2.pop()

        if n1.val != n2.val:
            return False

        if n1.left and n2.left:
            q1.insert(0, n1.left)
            q2.insert(0, n2.left)
        elif n1.left or n2.left:
            return False

        if n1.right and n2.right:
            q1.insert(0, n1.right)
            q2.insert(0, n2.right)
        elif n1.right or n2.right:
            return False

    return True

if __name__ == '__main__':
    t1 = BinaryTree(1)
    t2 = BinaryTree(1)

    t1.insert_left(2)
    t1.insert_right(3)
    t1.left.insert_left(4)
    t1.left.insert_right(5)

    t2.insert_left(2)
    t2.insert_right(3)
    t2.left.insert_left(4)
    t2.left.insert_right(5)

    if identical_trees(t1, t2):
        print 'Both trees are identical'
    else:
        print 'Trees are not identical'

    print are_identical(t1, t2)
