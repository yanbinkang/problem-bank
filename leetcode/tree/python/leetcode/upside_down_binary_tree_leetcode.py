from binary_tree import BinaryTree

"""
https://leetcode.com/problems/binary-tree-upside-down/

solution is similar to iterative Linkedlist reversal

https://discuss.leetcode.com/topic/40924/java-recursive-o-logn-space-and-iterative-solutions-o-1-space-with-explanation-and-figure
"""

def upside_down_binary_tree(root):
    current = root
    next_node = None
    temp = None
    previous = None

    while current:
        next_node = current.left

        current.left = temp
        temp = current.right
        current.right = previous

        previous = current
        current = next_node

    return previous

def test_level_order(root):
    if root is None: return

    q = [root]

    while q:
        for _ in range(len(q)):
            node = q.pop()
            print node.val
            if node.left:
                q.insert(0, node.left)
            if node.right:
                q.insert(0, node.right)

if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_left(2)
    tree.insert_right(3)

    tree.left.insert_left(4)
    tree.left.insert_right(5)

    test_level_order(tree)
    print('\n')
    res = upside_down_binary_tree(tree)

    test_level_order(res)
