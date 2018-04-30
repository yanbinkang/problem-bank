def pre_order(tree):
    if tree:
        print(tree.get_root_val())
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())
