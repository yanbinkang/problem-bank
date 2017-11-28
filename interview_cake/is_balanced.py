def is_balanced(tree_root):
    depths = []

    nodes = Stack()
    nodes.push((tree_root, 0))


    while not nodes.is_empty():
        node, depth = nodes.pop()

        if (not node.left) and (not node.right):
            if depth not in depths:
                depths.append(depth)

                if (len(depths) > 2) or \
                    (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False
        else:
            if node.left:
                nodes.push((node.left, depth+1))
            if node.right:
                node.push((node.right, depth+1))
    return True
