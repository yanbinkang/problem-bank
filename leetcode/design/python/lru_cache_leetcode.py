"""
https://leetcode.com/problems/lru-cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

https://discuss.leetcode.com/topic/24757/python-concise-solution-with-comments-using-ordereddict

Algorithm using python's OrderedDict:

- Use collections.OrderedDict(). Read about this!

get: if the key we want is not in the cache, we return -1. If key is in cache, we pop that key at whatever position its in and save the value. Then we put the value with its associated key at the back of the cache. Finally we return the value (Reason: this is the recently used item and must be as far away from the front of the cache as possible.)

put: If the key is already in the cache, we pop it out [ pop(key) ]. We're going to insert it anyway, we just cannot insert when that key already exists in the cache. If the key doesn't exist in the cache, we reduce the capacity if its greater the zero. If the cache is zero, it means the cache is full and we need to remove the key/value pair at the front of the cache [ popitem(last=False) ].

Finally insert the key, value pair.

Algorithm using python's Deque:

- Use collections.deque([])
- Use dict

get: very similar to OrderedDict. we return -1 if key doesn't exist. If the key exists, we remove from deque, and add the the back of the deque.

Finally add the key value pair to the dictionary

put: if key in cache remove from deque. If the length of the dictionary is equal to the capacity, pop from the front of the deque and save the value. Pop the value from the dictionary.

Finally add the key to the back of the deque and add the key/value pair to the dictionary.
"""
import collections


class LRUCache(object):

    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.dic:
            return -1

        v = self.dic.pop(key)   # remove key from dic
        self.dic[key] = v       # set the key as the newest one at the back
        return v                # return v

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)  # FIFO or remove from front
        self.dic[key] = value  # set the key as the newest one at the back


"""
LRUCache solution using dictionary and deque
"""


class LRUCache(object):
    def __init__(self, capacity):
        self.deque = collections.deque([])
        self.dic = {}
        self.capacity = capacity

    def get(self, key):
        if key not in self.dic:
            return -1

        self.deque.remove(key)
        self.deque.append(key)
        return self.dic[key]

    def put(self, key, value):
        if key in self.dic:
            # remove for now. we'll put at the back of deque later
            self.deque.remove(key)
        elif len(self.dic) == self.capacity:
            # remove and return the Least Recently Used element
            lru_item = self.deque.popleft()
            # remove lru_item and its associated value from dictionary as well
            self.dic.pop(lru_item)
        self.deque.append(key)
        self.dic[key] = value


if __name__ == '__main__':
    cache = LRUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print cache.dic
    # print cache.dic
    # print cache.get(1)        # returns 1
    # # print cache.dic
    # cache.put(3, 3)           # evicts key 2
    # # print cache.dic
    # print cache.get(2)        # returns -1
    # cache.put(4, 4)           # evicts key 1
    # # print cache.dic
    # print cache.get(1)        # returns -1 (not found)
    # print cache.get(3)        # returns 3
    # # print cache.dic
    # print cache.get(4)        # returns 4
    # print cache.dic
