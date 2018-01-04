"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

https://discuss.leetcode.com/topic/8447/simple-solution-using-constant-space

O(n) time O(1) space
"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    if root is None:
        return

    temp_child = TreeLinkNode(0)

    while root:
        current_child = temp_child
        while root:
            if root.left:
                current_child.next = root.left
                current_child = current_child.next
            if root.right:
                current_child.next = root.right
                current_child = current_child.next
            root = root.next

        root = temp_child.next
        temp_child.next = None


if __name__ == '__main__':
    tree = TreeLinkNode(1)
    tree.left = TreeLinkNode(2)
    tree.right = TreeLinkNode(3)

    connect(tree)
