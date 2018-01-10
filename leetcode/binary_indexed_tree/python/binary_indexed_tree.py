"""
Write a program to implement fenwick or binary indexed tree

A Fenwick tree or binary indexed tree is a data structure providing efficient methods
for calculation and manipulation of the prefix sums of a table of values.

Space complexity for fenwick tree is O(n)
Time complexity to create fenwick tree is O(nlogn)
Time complexity to update value is O(logn)
Time complexity to get prefix sum is O(logn)

References
http://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/
https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/
http://en.wikipedia.org/wiki/Fenwick_tree
"""
class FenTree(object):
    def __init__(self, array):
        self.array = [0] * len(array)
        self.tree = [0] * (len(array) + 1)

        for i in range(len(array)):
            self.update(i, array[i])

    def __str__(self):
        return "ARRAY => \t" + str(self.array) +\
         '\n' + "Binary Indexed Tree => \t" + str(self.tree)

    def __repr__(self):
        return self.__str__()

    """
    0) Find binary representation of index
    1) 2's complement (flip all the bits and add 1)
    2) AND it with original number
    3) Subtract from original number

    O(1) operation
    """
    def get_parent(self, child):
        return (child - (child & -child))


    """
    0) Find binary representation of index
    1) 2's complement (flip all the bits and add 1)
    2) AND it with original number
    3) Add to original number

    O(1) operation
    """
    def get_next(self, index):
        return (index + (index & -index))

    def update(self, index, item):
        current = self.array[index]
        self.array[index] = item

        item -= current

        index += 1

        while index < len(self.tree):
            self.tree[index] += item
            index = self.get_next(index)

    def prefix_sum(self, index):
        index += 1

        total = 0

        while index > 0:
            total += self.tree[index]
            index = self.get_parent(index)

        return total

    def range_sum(self, x, y):
        return (self.prefix_sum(max(x, y)) -\
                 self.prefix_sum( min(x, y) - 1 )
                )

if __name__ == '__main__':
    tree = FenTree([-2 ,0 , 3, -5, 2, -1])
    print tree

    print('\n')

    tree.update(4, 8) # replaces 2 with 8 in the list given to the fenwick tree

    print tree

    print('\n')
    print 'range sum of 1 to 5 is', tree.range_sum(1, 5) #returns 0+3-5+8-1
    print 'prefix sum of 5 is', tree.prefix_sum(5) #returns -2+0+3-5+8-1
