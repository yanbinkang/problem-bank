# O(n) time O(n) space
def spiral_printing_two_stack(root):
    if root == None:
        return

    stack_1 = []
    stack_2 = []

    stack_1.append(root)

    while stack_1 != [] or stack_2 != []:
        while stack_1 != []:
            root = stack_1.pop()
            print root.key
            if root.get_left_child():
                stack_2.append(root.left_child)
            if root.get_right_child():
                stack_2.append(root.right_child)

        while stack_2 != []:
            root = stack_2.pop()
            print root.key
            if root.get_right_child():
                stack_1.append(root.right_child)
            if root.get_left_child():
                stack_1.append(root.left_child)
