from binary_tree import *
def pre_order(root):
    stack = [root]

    visited = set()

    visited.add(root)

    while stack:
        node = stack.pop()
        print node.val

        if node.right:
            if node.right and node.right not in visited:
                stack.append(node.right)
                visited.add(node.right)

        if node.left:
            if node.left and node.left not in visited:
                stack.append(node.left)
                visited.add(node.left)


if __name__ == '__main__':
    # tree = BinaryTree(10)
    # tree.insert_left(2)
    # tree.insert_right(5)
    # tree.left.insert_left(6)
    # tree.right.insert_left(8)
    # tree.right.insert_right(3)

    # pre_order(tree)

    root = BinaryTree(100)
    root.insert_left(50)
    root.insert_right(200)
    root.left.insert_right(25)
    root.right.insert_left(125)
    root.right.insert_right(350)
