from binary_tree import *

"""
Iterative method is quite straightforward: use BFS and update maximum level by level until reaching the bottom level. One detail is to use another stack count to store the length of the sequence ending at current node.

https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
https://discuss.leetcode.com/category/376/binary-tree-longest-consecutive-sequence
"""

def longest_consecutive(root):
    if root == None:
        return 0

    count_stack = [1]
    stack = [root]

    maximum = 1

    while stack:
        node = stack.pop()
        count_val = count_stack.pop()

        maximum = max(count_val, maximum)

        if node.left:
            stack.append(node.left)
            if node.left.val - node.val == 1:
                count_stack.append(count_val + 1)
            else:
                count_stack.append(1)


        if node.right:
            stack.append(node.right)
            if node.right.val - node.val == 1:
                count_stack.append(count_val + 1)
            else:
                count_stack.append(1)

    return maximum

if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_right(3)
    tree.right.insert_left(2)
    tree.right.insert_right(4)
    tree.right.right.insert_right(5)

    tree1 = BinaryTree(2)
    tree1.insert_right(3)
    tree1.right.insert_left(2)
    tree1.right.left.insert_left(1)

    tree2 = BinaryTree(1)
    tree2.insert_left(2)
    tree2.insert_right(2)

    print(longest_consecutive(tree))
    print("\n")
    print(longest_consecutive(tree1))
    print("\n")
    print(longest_consecutive(tree2))
