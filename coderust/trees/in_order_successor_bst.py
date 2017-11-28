def inorder_succ_bst(tree):
    if tree == None:
        return None

    succ = None
    if tree.has_right_child():
        succ = tree.right_child.find_min()
    elif tree.parent:
        if tree.is_left_child():
            succ = tree.parent
        else:
            tree.parent.right_child = None
            succ = tree.parent.inorder_succ_bst()
            tree.parent.right_child = tree
    return succ

def find_min(tree):
    current = tree
    while tree.has_left_child():
        current = current.left_child
    return current
