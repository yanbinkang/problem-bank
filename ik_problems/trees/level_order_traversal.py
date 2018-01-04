# bfs O(n) time O(n) space
def level_order_traversal(root):
    queue = []

    queue.insert(0, root)

    while queue != []:
        root = queue.pop()

        print root.key

        if root.get_left_child():
            queue.insert(0, root.left_child)
        if root.get_right_child():
            queue.insert(0, root.right_child)
