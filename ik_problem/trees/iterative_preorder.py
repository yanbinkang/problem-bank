# O(n) time O(n) space
def iterative_preorder(root):
    if root == None:
        return

    stack = []
    stack.append(root)

    while stack != []:
        root = stack.pop()
        print root.key

        if root.get_right_child():
            stack.append(root.right_child)
        if root.get_left_child():
            stack.append(root.left_child)
