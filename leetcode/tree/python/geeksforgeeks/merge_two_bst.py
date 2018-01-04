"""
http://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/
"""
from binary_tree import *
def merge_trees(t1, t2):
    s1, s2 = [], []

    inorder(t1, s1)
    inorder(t2, s2)

    merged_lists = merge_lists(s1, s2)

    root = helper(merged_lists)

    return root


def helper(sorted_array):
    first, last = 0, len(sorted_array) - 1

    mid = (first + last) // 2

    if first > last:
        return

    root = BinaryTree(sorted_array[mid])

    root.left = helper(sorted_array[:mid])

    root.right = helper(sorted_array[mid+1:])

    return root



def inorder(tree, temp):
    if tree:
        inorder(tree.left, temp)
        temp.append(tree.val)
        inorder(tree.right, temp)

def merge_lists(s1, s2):
    result = [None] * (len(s1) + len(s2))

    i, j, k = 0, 0, 0

    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            result[k] = s1[i]
            i += 1
        else:
            result[k] = s2[j]
            j += 1
        k += 1

    while i < len(s1):
        result[k] = s1[i]
        i += 1
        k += 1

    while j < len(s2):
        result[k] = s2[j]
        j += 1
        k += 1

    return result

"""
        2               5              3
      /   \            / \           /    \
     1     10         3   7         1      7
                                     \    /  \
                                      2  5   10
"""

if __name__ == '__main__':
    t = BinaryTree(2)
    t.insert_left(1)
    t.insert_right(10)

    t2 = BinaryTree(5)
    t2.insert_left(3)
    t2.insert_right(7)

    result = merge_trees(t, t2)

    # queue = [result]

    # data = []

    # while queue:
    #     col = []
    #     for _ in range(len(queue)):
    #         node = queue.pop()

    #         col.append(node.val)

    #         if node.left:
    #             queue.insert(0, node.left)

    #         if node.right:
    #             queue.insert(0, node.right)

    #     data.append(col)

    # print data

    q1, q2 = [], []

    q1.append(result)

    while q1 or q2:
        while q1:
            node = q1.pop()

            if node.left:
                q2.insert(0, node.left)
            if node.right:
                q2.insert(0, node.right)

            print node.val,
        print('\n')

        while q2:
            node1 = q2.pop()

            if node1.left:
                q1.insert(0, node1.left)
            if node1.right:
                q1.insert(0, node1.right)

            print node1.val,
        print('\n')
