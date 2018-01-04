"""
http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/

1. Initialize current as root
2. While current is not NULL
   If current does not have left child
      a) Print current's data
      b) Go to the right, i.e., current = current->right
   Else
      a) Make current as right child of the rightmost
         node in current's left subtree
      b) Go to this left child, i.e., current = current->left
"""
def morris_traversal(root):
    current = root

    while current:
        if current.left is None:
            print current.val
            current = current.right
        else:
            predecessor = current.left

            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if predecessor.right is None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                print predecessor.val
                current = current.right
