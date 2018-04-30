def post_order_eval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    res_1 = None
    res_2 = None
    if tree:
        res_1 = post_order_eval(tree.get_left_child())
        res_2 = post_order_eval(tree.get_right_child())
        if res_1 and res_2:
            return opers[tree.get_root_val()](res_1, res_2)
        else:
            return tree.get_root_val()
