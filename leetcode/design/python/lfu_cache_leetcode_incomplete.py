"""
https://leetcode.com/problems/lfu-cache
"""
import collections

class LFUNode(object):
    def __init__(self, freq):
        self.freq = freq
        self.od = collections.OrderedDict()
        self.prev = None
        self.next = None

class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {} # stores key/node pair
        self.head = LFUNode(0)
        self.tail = LFUNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        if key not in self.map:
            return -1

        node = self.map[key]
        res = node.od[key]
        node.od.pop(key)
        self.move_forward(node, key, res)

        return res

    def pop_item(self):
        node = self.tail

        while len(node.prev.od) == 0:
            # remove the prev node that has no item saved on that
            node.prev = node.prev.prev
            node.prev.next = node

        k, v = node.prev.od.popitem(last=False)
        self.map.pop(k)

    def move_forward(self, node, key, value):
        # add new item
        if node.prev == self.head or node.prev.freq != node.freq + 1:
            prev_node = LFUNode(node.freq + 1)
            prev_node.prev = node.prev
            node.prev = prev_node
            prev_node.prev.next = prev_node
            prev_node.next = node
        else:
            prev_node = node.prev

        prev_node.od[key] = value
        self.map[key] = prev_node

    def set(self, key, value):
        if self.capacity == 0:
            return

        if key in self.map:
            node = self.map[key]
            node.od.pop(key)
            self.move_forward(node, key, value)
        else:
            if self.size == self.capacity:
                self.pop_item()
            else:
                self.size += 1
            self.move_forward(self.tail, key, value)



    def put(self, key, value):
        pass


if __name__ == '__main__':
    # Your LFUCache object will be instantiated and called as such:
    obj = LFUCache(2)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    # cache = LFUCache(3)
    # cache.put(2, 2)
    # cache.put(1, 1)
    # print cache.get(2)
    # print cache.get(1)
    # print cache.get(2)
    # cache.put(3, 3)
    # cache.put(4, 4)
    # print cache.d
    # print cache.counter
    # print cache.get(2)



