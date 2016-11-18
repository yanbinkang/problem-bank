from binary_tree import *

def level_order_traversal(root):
    if root is None:
        return None

    q = []
    q.insert(0, root)
    res = []

    while len(q) > 0:
        data = []

        for _ in range(len(q)):
            node = q.pop()
            data.append(node.val)
            if node.left != None:
                q.insert(0, node.left)
            if node.right != None:
                q.insert(0, node.right)

        if data:
            res.append(data)


    return res


if __name__ == '__main__':
    tt = BinaryTree(1)
    tt.insert_left(2)
    tt.insert_right(3)
    tt.left.insert_left(4)
    tt.right.insert_right(5)

    res = level_order_traversal(tt)
    print res

    tree = BinaryTree(3)
    tree.insert_left(9)
    tree.insert_right(20)
    tree.right.insert_left(15)
    tree.right.insert_right(7)

    result = level_order_traversal(tree)
    print(result)


"""
             1
            / \
           2   3
          /     \
         4       5
"""
