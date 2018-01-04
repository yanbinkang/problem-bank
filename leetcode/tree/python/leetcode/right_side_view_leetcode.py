from binary_tree import *
"""
https://leetcode.com/problems/binary-tree-right-side-view/

https://discuss.leetcode.com/topic/11768/my-simple-accepted-solution-java/19

http://www.programcreek.com/2014/04/leetcode-binary-tree-right-side-view-java/
"""

def right_side_view_rec(root):
    result = []

    right_view(root, result, 0)

    return result

def right_view(root, result, current_depth):
    if root == None:
        return

    if current_depth == len(result):
        result.append(root.val)

    right_view(root.right, result, current_depth + 1)
    right_view(root.left, result, current_depth + 1)

"""
use level order traversal but only add to result if node is last element in current level

read more here: https://discuss.leetcode.com/topic/11315/reverse-level-order-traversal-java
"""
def right_side_view_with_queue(root):
    result = []

    queue = []
    queue.append(root)

    while queue:
        size = len(queue)

        for i in range(size):
            top = queue.pop()

            if i == (size - 1): # last element in current level
                result.append(top.val)

            if top.left:
                queue.insert(0, top.left)

            if top.right:
                queue.insert(0, top.right)

    return result


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)
    tree.left.insert_right(5)

    print(right_side_view_rec(tree))

    """
                    1
                  /   \
                 2     3
                  \
                   5
    """

    tree_1 = BinaryTree(1)
    tree_1.insert_left(2)
    tree_1.insert_right(3)
    tree_1.left.insert_right(5)
    tree_1.right.insert_right(4)

    print(right_side_view_with_queue(tree_1))

    """
                    1
                  /   \
                 2     3
                  \     \
                   5     4
    """
