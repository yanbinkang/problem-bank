from binary_tree import *

# https://youtu.be/wGXB9OWhPTg
# O(n) time O(1) space
def morris_traversal_preorder(root):
    result = []

    if root == None:
        return result

    current = root

    while current:
        if current.left == None:
            result.append(current.val) # or print current.val
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right != None and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right == None:
                predecessor.right = current
                result.append(current.val) # or print current.val
                current = current.left
            else:
                predecessor.right = None
                current = current.right

    return result

# O(n) time O(n) space
def preorder_traversal_rec(root):
    result = []

    if root == None:
        return result

    traversal(root, result)

    return result

def traversal(root, result):
    if root == None:
        return

    if root:
        result.append(root.val)
        traversal(root.left, result)
        traversal(root.right, result)

# O(n) time O(n) space
def preorder_traversal_stack(root):
    result = []

    if root == None:
        return result

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()

        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_right(2)
    tree.right.insert_left(3)

    print preorder_traversal_rec(tree)
    print("\n")
    print preorder_traversal_stack(tree)
    print("\n")
    print(morris_traversal_preorder(tree))

