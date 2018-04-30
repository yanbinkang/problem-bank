import unittest

import os, sys
sys.path.insert(0, os.path.abspath(".."))
from trees_and_tree_algorithms import binary_search_tree



class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = binary_search_tree.BinarySearchTree()

    def test_get_put(self):
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')

        assert self.bst.get(50) == 'a'
        assert self.bst.get(45) == 'f'
        assert self.bst.get(85) == 'd'
        assert self.bst.get(10) == 'b'
        assert self.bst.root.key == 50
        assert self.bst.root.left_child.key == 10
        assert self.bst.root.right_child.key == 70

    def test_put_oper(self):
        self.bst[25] = 'g'
        assert self.bst[25] == 'g'

    def test_find_succ(self):
        x = binary_search_tree.BinarySearchTree()
        x.put(10, 'a')
        x.put(15, 'b')
        x.put(6, 'c')
        x.put(2, 'd')
        x.put(8, 'e')
        x.put(9, 'f')
        assert x.root.left_child.left_child.find_successor().key == 6
        assert x.root.left_child.right_child.find_successor().key == 9
        assert x.root.left_child.right_child.right_child.find_successor().key == 10

    def test_size(self):
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        assert self.bst.length() == 7

    def test_delete(self):
        self.bst.put(50, 'a')
        self.bst.put(10, 'b')
        self.bst.put(70, 'c')
        self.bst.put(30, 'd')
        self.bst.put(85, 'd')
        self.bst.put(15, 'e')
        self.bst.put(45, 'f')
        self.bst.put(5, 'g')

        assert(10 in self.bst) == True
        self.bst.delete(10)
        
        assert(10 in self.bst) == False
        assert self.bst.root.left_child.key == 15
        assert self.bst.root.left_child.parent == self.bst.root
        assert self.bst.root.left_child.right_child.parent == self.bst.root.left_child
        assert self.bst.get(30) == 'd'
        self.bst.delete(15)

        assert self.bst.root.left_child.key == 30
        assert self.bst.root.left_child.right_child.key == 45
        assert self.bst.root.left_child.right_child.parent == self.bst.root.left_child



if __name__ == '__main__':
    unittest.main()
