"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.

1. insert(val): Inserts an item val to the set if not already present.

2. remove(val): Removes an item val from the set if present.

3. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

read this: https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
"""
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = set()


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.store:
            return False
        else:
            self.store.add(val)
            return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.store:
            return False
        else:
            self.store.remove(val)
            return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.sample(self.store, 1)[0]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
