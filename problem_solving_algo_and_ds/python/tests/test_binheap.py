import unittest

import os, sys
sys.path.insert(0, os.path.abspath(".."))
from trees_and_tree_algorithms import binary_heap_min_heap


class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = binary_heap_min_heap.BinaryHeap()
        self.heap.insert(9)
        self.heap.insert(6)
        self.heap.insert(5)
        self.heap.insert(2)
        self.heap.insert(3)

    def test_insert(self):
        assert self.heap.current_size == 5

    def test_del_min(self):
        assert self.heap.del_min() == 2
        assert self.heap.del_min() == 3

    def test_build_heap(self):
        my_heap = binary_heap_min_heap.BinaryHeap()
        my_heap.build_heap([7, 3, 5, -1, 10, 14])
        assert my_heap.current_size == 6
        assert my_heap.del_min() == -1
        assert my_heap.del_min() == 3
        assert my_heap.del_min() == 5
        assert my_heap.del_min() == 7


if __name__ == '__main__':
    unittest.main()
