"""
https://leetcode.com/problems/moving-average-from-data-stream/

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
import collections


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        # this makes sure the length of the queue is always 3.
        # So, for  example, when appending the 4th item remove the first element in the queue
        self.queue = collections.deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        # Calculate the average
        return float(sum(self.queue)) / len(self.queue)


if __name__ == "__main__":
    obj = MovingAverage(3)
    obj.next(1)
    obj.next(10)
    obj.next(3)
    obj.next(5)
