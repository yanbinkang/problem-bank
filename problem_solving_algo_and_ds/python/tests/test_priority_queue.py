import unittest

import os, sys
sys.path.insert(0, os.path.abspath(".."))
from graphs_and_graph_algorithms import priority_queue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.the_heap = priority_queue.PriorityQueue()
        self.the_heap.add((2, 'x'))
        self.the_heap.add((3, 'y'))
        self.the_heap.add((5, 'z'))
        self.the_heap.add((6, 'a'))
        self.the_heap.add((4, 'd'))

    def test_insert(self):
        assert self.the_heap.current_size == 5

    def test_del_min(self):
        assert self.the_heap.del_min() == 'x'
        assert self.the_heap.del_min() == 'y'

    def test_dec_key(self):
        self.the_heap.decrease_key('d', 1)
        assert self.the_heap.del_min() == 'd'

if __name__ == '__main__':
    unittest.main()
