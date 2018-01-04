"""
http://www.geeksforgeeks.org/write-a-c-program-to-delete-a-tree/

To delete a tree we must traverse all the nodes of the tree and delete them one by one. So which traversal we should use - Inorder or Preorder or Postorder. Answer is simple - Postorder, because before deleting the parent node we should delete its children nodes first

We can delete tree with other traversals also with extra space complexity but why should we go for other traversals if we have Postorder available which does the work without storing anything in same time complexity.
"""
from binary_tree import *
def delete_tree(node):
    if node is None:
        return

    delete_tree(node.left)
    delete_tree(node.right)

    print 'the deleted node is %d' % node.val
    del node # or node = None


if __name__ == '__main__':
    t = BinaryTree(1)
    t.insert_left(2)
    t.insert_right(3)
    t.left.insert_left(4)
    t.left.insert_right(5)

    print delete_tree(t)
