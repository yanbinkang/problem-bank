def post_order(tree):
    if tree != None:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_val())
