"""
https://leetcode.com/problems/two-sum-iii-data-structure-design/

Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""

class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memo = []


    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        self.memo.append(number)


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        hash_map = {}

        for num in self.memo:
            if num in hash_map:
                return hash_map[num]
            else:
                hash_map[value - num] = True

        return False



if __name__ == '__main__':
    # Your TwoSum object will be instantiated and called as such:
    obj = TwoSum()
    obj.add(1)
    obj.add(3)
    obj.add(5)
    param_2 = obj.find(4)
    print param_2

    param_3 = obj.find(7)
    print param_3

    param_4 = obj.find(6)
    print param_4

    t = TwoSum()
    t.add(0)
    t.add(0)

    print t.find(0)

