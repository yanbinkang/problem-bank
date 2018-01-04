from binary_tree import BinaryTree

"""
https://leetcode.com/problems/serialize-and-deserialize-bst/

similar to: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

class Codec:
    def serialize(self, root):
        res = []
        self.preorder(root, res)
        return ' '.join(res)

    def deserialize(self, data):
        preorder = map(int, data.split())
        inorder = sorted(preorder)

        return self.build_tree(preorder, inorder)

    def preorder(self, root, res):
            if root:
                res.append(str(root.val))
                self.preorder(root.left, res)
                self.preorder(root.right, res)

    def build_tree(self, preorder, inorder):
        if inorder:
            root_val = preorder.pop(0)
            root = BinaryTree(root_val)
            index = inorder.index(root_val)

            root.left = self.build_tree(preorder, inorder[:index])
            root.right = self.build_tree(preorder, inorder[index+1:])

            return root

def test_inorder(root):
    """Test traversal """
    if root:
        test_inorder(root.left)
        print(root.val)
        test_inorder(root.right)

if __name__ == '__main__':
    tree = BinaryTree(2)
    tree.insert_left(1)
    tree.insert_right(3)

    codec = Codec()
    res = codec.deserialize(codec.serialize(tree))

    test_inorder(res)
