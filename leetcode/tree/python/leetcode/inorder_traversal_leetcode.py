from binary_tree import *

"""
watch this:
    https://youtu.be/wGXB9OWhPTg

read this:
    https://discuss.leetcode.com/topic/46016/learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-java-solution
"""

# O(n) time O(1) space
def morris_traversal_inorder(root):
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
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right == None: # node is None, go left
                predecessor.right = current
                current = current.left
            else: # left is already visited, go right
                predecessor.right = None
                result.append(current.val) # or print current.val
                current = current.right

    return result

# O(n) time O(n) space
def inorder_traversal_rec(root):
    result = []

    if root == None:
        return result

    traversal(root, result)

    return result

def traversal(root, result):
    if root:
        traversal(root.left, result)
        result.append(root.val)
        traversal(root.right, result)

# O(n) time O(n) space
def inorder_traversal_stack(root):
    result = []

    if root == None:
        return result

    stack = []

    while True:
        if root:
            stack.append(root)
            root = root.left
        else:
            if not stack:
                break
            root = stack.pop()
            result.append(root.val)
            root = root.right

    return result

"""
algorithm: while root is not null and stack is not empty, append root to the stack and keep going left. As soon as you've pushed the last left node, pop from the stack and append to the results stack. Then go right
"""
def inorder_traversal_stack_1(root):
    result = []
    if root is None: return result

    stack = []

    while root or stack:
        # append root node and all left nodes (if any)
        while root:
            stack.append(root)
            root = root.left

        # pop last appended node and apppend to result list
        root = stack.pop()
        result.append(root.val)
        # now go right
        root = root.right

    return result



if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_right(2)
    tree.right.insert_left(3)

    print inorder_traversal_rec(tree)
    print("\n")
    print(inorder_traversal_stack(tree))
    print("\n")
    print (morris_traversal_inorder(tree))
    print("\n")
    print inorder_traversal_stack_1(tree)

