"""
http://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/
"""
def max_depth(root):
    if root == None:
        return 0
    else:
        # compute the depth of each subtree
        l_depth = max_depth(root.left_child)
        r_depth = max_depth(root.right_child)

        # return the larger one
        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1

        # above same as
        # return 1 + max(max_depth(root.left_child), max_depth(root.right_child))

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

if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insert_right(3)
    tree.insert_left(2)
    tree.left_child.insert_left(4)
    tree.left_child.insert_right(5)

    print max_depth(tree)
