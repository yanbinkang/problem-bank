class BinaryTree:
    def __init__(self, data):
        self.key = data
        self.left_child = None
        self.right_child = None

    def insert_left(self, key):
        if self.left_child == None:
            self.left_child = BinaryTree(key)
        else:
            temp = BinaryTree(key)
            temp.left_child = self.left_child
            self.left_child = temp

    def insert_right(self, key):
        if self.right_child == None:
            self.right_child = BinaryTree(key)
        else:
            temp = BinaryTree(key)
            temp.right_child = self.right_child
            self.right_child = temp

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.right_child:
                for elem in self.right_child:
                    yield elem


if __name__ == '__main__':
    """
    Build this tree:

              20

             /  \
            8    22
           / \     \
          4   12    23
         /
        3
    """
    tree = BinaryTree(20)
    tree.insert_left(8)
    tree.insert_right(22)

    tree.left_child.left_child = BinaryTree(4)
    tree.left_child.right_child = BinaryTree(12)
    tree.left_child.left_child.left_child = BinaryTree(3)

    tree.right_child.right_child = BinaryTree(23)

    a = iter(tree)

    print a.next()
    print a.next()
    print a.next()
    print a.next()
    print a.next()
    print a.next()
    print a.next()
