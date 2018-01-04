from binary_tree import *
"""
This solution uses to stacks. But you could also use one stack and a result list to keep track of result.
"""
def post_order_traversal_iterative(root):
    s1 = []
    s2 = []

    s1.append(root)

    while s1:
        node = s1.pop()
        s2.insert(0, node.val)

        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)

    return s2

def post_order_traversal(root):
    result = []
    if root == None:
        result

    traversal(root, result)

    return result

def traversal(root, result):
    if root:
        traversal(root.left, result)
        traversal(root.right, result)
        result.append(root.val)


if __name__ == '__main__':
    tree = BinaryTree(7)

    tree.insert_left(10)
    tree.insert_right(2)

    tree.left.insert_left(4)
    tree.left.insert_right(3)
    tree.left.right.insert_right(1)

    tree.right.insert_left(8)
    tree.right.left.insert_left(11)

    print(post_order_traversal(tree))
    print("\n")
    print(post_order_traversal_iterative(tree))
