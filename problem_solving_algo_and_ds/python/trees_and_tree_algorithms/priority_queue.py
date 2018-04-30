from binary_heap_min_heap import BinHeap

class PriorityQueue(BinHeap):
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def enqueue(self, item):
        self.insert(item)

    def dequeue(self):
        return self.del_min()

# pq = PriorityQueue()
# pq.enqueue(9)
# pq.enqueue(6)
# pq.enqueue(5)
# pq.enqueue(2)
# pq.enqueue(3)
# print pq.dequeue()
# print pq.heap_list
# print pq.current_size
