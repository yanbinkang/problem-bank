from binary_tree import *

def same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False

    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)



if __name__ == '__main__':
    t1 = BinaryTree(1)
    t1.insert_left(2)
    t1.insert_right(3)

    t2 = BinaryTree(1)
    t2.insert_left(2)
    t2.insert_right(3)

    t3 = BinaryTree(4)
    t3.insert_left(5)
    t3.insert_right(3)

    print(same_tree(t1, t2))
    print("\n")
    print(same_tree(t1, t3))
