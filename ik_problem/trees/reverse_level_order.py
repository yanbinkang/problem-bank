# O(n) time O(n) space
def reverse_level_order(root):
    queue = []
    stack = []

    queue.insert(0, root)

    while queue != []:
        current_node = queue.pop()

        if current_node.get_right_child():
            queue.insert(0, current_node.right_child)
        if current_node.get_left_child():
            queue.insert(0, current_node.left_child)

        stack.append(current_node)

    while stack != []:
        current_node = stack.pop()
        print current_node.key
