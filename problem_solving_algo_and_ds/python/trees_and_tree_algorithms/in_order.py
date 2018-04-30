def in_order(tree):
    if tree != None:
        in_order(tree.get_left_child())
        print(tree.get_root_val())
        in_order(tree.get_right_child())
