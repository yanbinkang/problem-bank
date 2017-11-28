# post order traversal without recursion
def iterative_post_order(self):
    s1 = []
    s2 = []
    s1.append(self)
    while s1 != []:
        root = s1.pop()
        s2.append(root)
        if root.get_left_child():
            s1.append(root.get_left_child())
        if root.get_right_child():
            s1.append(root.get_right_child())

    while s2 != []:
        root = s2.pop()
        print root.key
