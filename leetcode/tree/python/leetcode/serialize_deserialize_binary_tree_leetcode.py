from binary_tree import BinaryTree

"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

solution: recursive using preorder O(n)
https://discuss.leetcode.com/topic/28041/recursive-preorder-python-and-c-o-n
"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        self._preorder(root, result)
        return ' '.join(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        result = iter(data.split())
        return self._build_tree(result)


    def _preorder(self, root, result):
        if root:
            result.append(str(root.val))
            self._preorder(root.left, result)
            self._preorder(root.right, result)
        else:
            result.append('#')

    def _build_tree(self, result):
        val = next(result)
        if val == '#': return None
        node = BinaryTree(int(val))
        node.left = self._build_tree(result)
        node.right = self._build_tree(result)

        return node

if __name__ == '__main__':
    root = BinaryTree(1)
    root.insert_left(2)
    root.insert_right(3)

    root.right.insert_left(4)
    root.right.insert_right(5)


    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    codec.deserialize(codec.serialize(root))

