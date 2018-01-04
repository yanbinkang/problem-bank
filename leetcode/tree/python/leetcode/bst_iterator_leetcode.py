from binary_tree import BinaryTree
"""
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

algorithm: Use morris inorder traversal and keep moving self.root
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.root is not None


    def next(self):
        """
        :rtype: int
        """
        result = 0

        while self.root:
            if self.root.left is None:
                result = self.root.val
                self.root = self.root.right
                break
            else:
                predecessor = self.root.left

                while predecessor.right and predecessor.right != self.root:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = self.root
                    self.root = self.root.left
                else:
                    result = self.root.val
                    predecessor.right = None
                    self.root = self.root.right
                    break

        return result

if __name__ == '__main__':
    tree = BinaryTree(2)
    tree.insert_left(1)
    tree.insert_right(3)



    # Your BSTIterator will be called like this:
    i, v = BSTIterator(tree), []
    while i.hasNext(): v.append(i.next())
    print v
