import unittest

import os, sys
sys.path.insert(0, os.path.abspath(".."))
from trees_and_tree_algorithms import avl_tree


class AVLTreeTests(unittest.TestCase):
    def setUp(self):
        self.avl_tree = avl_tree.AVLTree()

    def test_auto_1(self):
        self.avl_tree.put(30, 'a')
        self.avl_tree.put(50, 'b')
        self.avl_tree.put(40, 'c')
        assert self.avl_tree.root.key == 40

    def test_auto_2(self):
        self.avl_tree.put(50, 'a')
        self.avl_tree.put(30, 'b')
        self.avl_tree.put(40, 'c')
        assert self.avl_tree.root.key == 40

    def test_auto_3(self):
        self.avl_tree.put(50, 'a')
        self.avl_tree.put(30, 'b')
        self.avl_tree.put(70, 'c')
        self.avl_tree.put(80, 'c')
        self.avl_tree.put(60, 'd')
        self.avl_tree.put(90, 'e')
        assert self.avl_tree.root.key == 70

    def test_auto_4(self):
        self.avl_tree.put(40, 'a')
        self.avl_tree.put(30, 'b')
        self.avl_tree.put(50, 'c')
        self.avl_tree.put(10, 'd')
        self.avl_tree.put(35, 'e')
        self.avl_tree.put(37, 'f')
        assert self.avl_tree.root.key == 35
        assert self.avl_tree.root.left_child.key == 30
        assert self.avl_tree.root.right_child.key == 40
        assert self.avl_tree.root.balance_factor == 0
        assert self.avl_tree.root.left_child.balance_factor == 1
        assert self.avl_tree.root.right_child.balance_factor == 0

    def test_auto_5(self):
        self.avl_tree.put(40, 'a')
        self.avl_tree.put(30, 'b')
        self.avl_tree.put(50, 'c')
        self.avl_tree.put(45, 'd')
        self.avl_tree.put(60, 'e')
        self.avl_tree.put(43, 'f')
        assert self.avl_tree.root.key == 45
        assert self.avl_tree.root.left_child.key == 40
        assert self.avl_tree.root.right_child.key == 50
        assert self.avl_tree.root.balance_factor == 0
        assert self.avl_tree.root.left_child.balance_factor == 0
        assert self.avl_tree.root.right_child.balance_factor == -1


if __name__ == '__main__':
    unittest.main()
