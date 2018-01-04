"""
Deep Copy of a Tree
Problem
We're given a special binary tree. We need to clone that tree.
"""

What makes the tree special, is that on each node, it can have an extra pointer (over and above left and right pointers), which points to another node anywhere in the tree.

def deep_clone(root):
    if root == None:
        return None

    if root != None:
        newNode = Node(root.key)

    newNode.left = deep_copy(root.left)
    newNode.right = deep_copy(root.right)

"""

        Answer
Ignore the special pointer for now. Just make copy like usual. Either in the process of, or with another pass, make a lookup table of "Node in existing tree" ==> "Node in new tree". Then take yet another pass and set all special pointers.
"""
