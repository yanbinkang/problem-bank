def bst_checker(root):
    # start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    stack = Stack([(root, MIN_INT, MAX_INT)])

    # depth-first traversal
    while not stack.is_empty():
        node, lower_bound, upper_bound = stack.pop()

        # if this node is invalid we return false right away
        if (node.value < lower_bound) or (node.value > upper_bound):
            return False

        if node.left:
            stack.push((node.left, lower_bound, node.value))
        if node.right:
            stack.push((node.right, node.value, upper_bound))

    return True
