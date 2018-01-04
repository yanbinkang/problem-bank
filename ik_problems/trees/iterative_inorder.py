# O(n) time O(n) space
def iterative_inorder(root):
    if root == None:
        return

    stack = []

    while True:
        if root != None:
            stack.append(root)
            root = root.left_child
        else:
            if stack == []:
                break
            root = stack.pop()
            print root.key
            root = root.right_child
