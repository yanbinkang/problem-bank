from binary_tree import *
"""
Recursive: For given node we check whether its left child is a leaf. If it is the case, we add its value to answer, otherwise recursively call method on left child. For right child we call method only if it has at least one non null child.
"""

def sum_of_left_leaves_recur(root):
    ans = 0

    if root == None:
        return ans

    if root.left:
        if root.left.left == None and root.left.right == None: #leaf
            ans += root.left.val
        else:
            ans += sum_of_left_leaves_recur(root.left)

    ans += sum_of_left_leaves_recur(root.right) # go right

    return ans


"""
Iterative method. Here for each node in the tree we check whether its left child is a leaf. If it is true, we add its value to answer, otherwise add left child to the stack to process it later. For right child we add it to stack only if it is not a leaf.
"""
def sum_of_left_leaves_iterative(root):
    if not root: return 0

    ans = 0

    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        if node.left:
            if node.left.left == None and node.left.right == None:
                ans += node.left.val
            else:
                stack.append(node.left)

        if node.right:
            if node.right.left != None or node.right.right != None:
                stack.append(node.right)

    return ans

# https://discuss.leetcode.com/topic/60415/java-solution-with-stack/2
def sum_of_left_leaves_iterative_1(root):
    res = 0

    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            if node.left and node.left.left is None and \
                node.left.right is None:
                    res += node.left.val
            stack.append(node.left)
            stack.append(node.right)

    return res




if __name__ == '__main__':
    t = BinaryTree(3)
    t.insert_left(9)
    t.insert_right(20)
    t.right.insert_left(15)
    t.right.insert_right(7)

    print(sum_of_left_leaves_recur(t))

    print("\n")

    print(sum_of_left_leaves_iterative(t))

    print("\n")

    print sum_of_left_leaves_iterative_1(t)
