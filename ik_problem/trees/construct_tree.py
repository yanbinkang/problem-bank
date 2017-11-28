"""
http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

                           7
                       /      \
                     10        2
                    /  \       /
                   4    3     8
                         \   /
                          1 11

in:   4, 10, 3, 1, 7, 11, 8, 2
post: 4, 1, 3, 10, 11, 8, 2, 7
4, 1, 3, 10     11, 8, 2

4

4, 1, 3

4, 1



pre: 7, 10, 4, 3, 1, 2, 8, 11
"""
class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

# def build_inorder_postorder(in_ord, post_ord, start, end):
#     post_index = len(post_ord)-1

#     if start > end:
#         return None

#     root = Node(post_ord[post_index])

#     if start == end:
#         return root

#     in_index = in_ord.index(root.data)

#     root.left_child = build_inorder_postorder(in_ord, post_ord[:in_index], start, in_index-1)
#     root.right_child = build_inorder_postorder(in_ord, in_ord[:end+1], in_index+1, end)

#     return root


def build_inorder_preorder(in_ord, pre_ord, in_start, in_end):

    pre_index = 0

    if in_start > in_end:
        return None

    root = Node(pre_ord[pre_index])

    if in_start == in_end:
        return root

    in_index = in_ord.index(root.data)

    root.left_child = build_inorder_preorder(in_ord, pre_ord[pre_index+1:], in_start, in_index-1)
    root.right_child = build_inorder_preorder(in_ord, in_ord[in_index+1:], in_index+1, in_end)

    return root


def in_order(node):
    if node:
        if node.left_child:
            in_order(node.left_child)
        print node.data
        if node.right_child:
            in_order(node.right_child)


if __name__ == '__main__':
    in_ord = [4, 10, 3, 1, 7, 11, 8, 2]
    pre_ord = [7, 10, 4, 3, 1, 2, 8, 11]
    post = [4, 1, 3, 10, 11, 8, 2, 7]

    _in = ['D', 'B', 'E', 'A', 'F', 'C']
    pre = ['A', 'B', 'D', 'E', 'C', 'F']

    # res = build_inorder_preorder(in_ord, pre_ord, 0, len(in_ord)-1)
    res = build_inorder_preorder(_in, pre, 0, len(_in)-1)
    # res = build_inorder_postorder(in_ord, post, 0, len(in_ord)-1)

    in_order(res)
