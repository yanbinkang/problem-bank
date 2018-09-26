class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left == None:
            self.left = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left = self.left
            self.left = t

    def insert_right(self, new_node):
        if self.right == None:
            self.right = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right = self.right
            self.right = t
