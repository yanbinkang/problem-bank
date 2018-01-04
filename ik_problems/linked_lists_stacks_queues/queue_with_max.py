# Implement a queue with max() operation
class MaxQueue:
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

        for elem in self.max_queue:
            if item > elem:
                self.max_queue.remove(elem)
        self.max_queue.insert(0, item)

    def dequeue(self):
        res = self.queue.pop()
        if res == self.max_queue[-1]:
            self.max_queue.pop()
        return res

    def get_max(self):
        return self.max_queue[-1]


queue = MaxQueue()
queue.enqueue(20)
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(31)

print queue.get_max()
