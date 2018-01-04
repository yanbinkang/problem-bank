def predecessor(root, p):
    if root == None:
        return None

    if root.val >= p.val:
        return predecessor(root.left, p)
    else:
        right = predecessor(root.right, p)

        return right if right else root
