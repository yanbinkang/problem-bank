import unittest
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from data_structures import stack, queue

class TestStack(unittest.TestCase):
    """
    Test stack implementation
    """
    def test_stack(self):
        self.stack = stack.Stack()
        self.stack.push(7)
        self.stack.push(23)
        self.stack.push(4)
        self.stack.push(9)

        self.assertEqual(self.stack.pop(), 9)
        self.assertFalse(self.stack.isEmpty())
        self.assertEqual(self.stack.size(), 3)
        self.assertEqual(self.stack.peek(), 4)

class TestQueue(unittest.TestCase):
    """
    Test queue implementation
    """
    def test_queue(self):
        self.queue = queue.Queue()
        self.queue.enqueue(13)
        self.queue.enqueue(57)
        self.queue.enqueue(-1)
        self.queue.enqueue(45)

        self.assertEqual(self.queue.dequeue(), 13)
        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.dequeue(), 57)
        self.assertEqual(self.queue.dequeue(), -1)
        self.assertEqual(self.queue.dequeue(), 45)
        self.assertEqual(self.queue.is_empty(), True)

if __name__ == '__main__':
    unittest.main()
