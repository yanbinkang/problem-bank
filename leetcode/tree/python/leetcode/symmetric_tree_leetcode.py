from binary_tree import *

def symmetric_tree(tree):
    return is_mirror(tree, tree)

def is_mirror(t1, t2):
    if t1 == None and t2 == None:
        return True
    if t1 == None or t2 == None:
        return False

    return (t1.val == t2.val) and is_mirror(t1.right, t2.left) and is_mirror(t1.left, t2.right)

def symmetric_tree_iterative(root):
    if root is None:
        return True

    stack = [(root.left, root.right)]

    while stack:
        left, right = stack.pop()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val == right.val:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        else:
            return False

    return True


if __name__ == '__main__':
    tree1 = BinaryTree(1)
    tree1.insert_left(2)
    tree1.insert_right(2)
    tree1.left.insert_left(3)
    tree1.left.insert_right(4)
    tree1.right.insert_left(4)
    tree1.right.insert_right(3)

    print(symmetric_tree(tree1))

    print("\n")

    tree2 = BinaryTree(1)
    tree2.insert_left(2)
    tree2.insert_right(2)
    tree2.left.insert_right(3)
    tree2.right.insert_right(3)

    print(symmetric_tree(tree2))
    print("\n")
    print symmetric_tree_iterative(tree1)
    print("\n")
    print symmetric_tree_iterative(tree2)

