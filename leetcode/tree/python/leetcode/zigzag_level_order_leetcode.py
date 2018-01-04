from binary_tree import *
"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

this solution is fine. You can also do normal level order with a queue and then reverse the result when level is odd.
O(n) time and space
"""
def zigzag_level_order(root):
    result = []
    if root is None:
        return result

    deque = [root]
    level = 0

    while deque:
        collection = []
        level += 1
        size = len(deque)

        for _ in range(size):
            if level % 2 == 0:
                node = deque.pop()
                if node.right:
                    deque.insert(0, node.right)
                if node.left:
                    deque.insert(0, node.left)
            else:
                node = deque.pop(0)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)

            collection.append(node.val)



        result.append(collection)

    return result

# use two stacks
def zigzag_level_order_two_stack(root):
    result = []
    if root == None: return result

    stack_1 = []
    stack_2 = []

    stack_1.append(root)

    while stack_1 or stack_2:

        collection = []
        while stack_1:
            node = stack_1.pop()
            # print node.val
            collection.append(node.val)
            if node.left:
                stack_2.append(node.left)
            if node.right:
                stack_2.append(node.right)

        result.append(collection)

        collection = []
        while stack_2:
            node = stack_2.pop()
            # print node.val
            collection.append(node.val)
            if node.right:
                stack_1.append(node.right)
            if node.left:
                stack_1.append(node.left)

        if collection:
            result.append(collection)

    return result


if __name__ == '__main__':
    tree = BinaryTree(3)
    tree.insert_left(9)
    tree.insert_right(20)

    tree.right.insert_left(15)
    tree.right.insert_right(7)

    print(zigzag_level_order(tree))

    print("\n")
    print(zigzag_level_order_two_stack(tree))
