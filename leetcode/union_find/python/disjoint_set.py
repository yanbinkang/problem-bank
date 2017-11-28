"""
wiki: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

Video link - https://youtu.be/ID00PMy0-vE

Disjoint sets using path compression and union by rank
    Supports 3 operations
    1) makeSet
    2) union
    3) findSet

Space: O(n) where n is number of elements in the set

Time: For m operations and total n elements time complexity is O(m*f(n)) where f(n) is very slowly growing function. For most cases f(n) <= 4 so effectively total time will be O(m). Proof in Coreman book.
"""
class Node(object):
    def __init__(self, data, parent = None, rank = 0):
        self.data = data
        self.parent = parent
        self.rank = rank

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.__str__()


class DisjointSet(object):
    def __init__(self):
        self.map = {}
        self.num_sets = 0

    def make_set(self, data):
        node = Node(data)
        node.parent = node # very important!
        self.map[data] = node
        self.num_sets += 1 # make_set increases the number of disjoint sets by one

    def union(self, data1, data2):
        # gets nodes given data values
        node1 = self.map[data1]
        node2 = self.map[data2]

        # get parents given nodes
        parent1 = self.find_set_util(node1)
        parent2 = self.find_set_util(node2)

        # if they are part of same set do nothing
        if parent1.data == parent2.data:
            return

        # else whoever's rank is higher becomes parent of other
        if parent1.rank >= parent2.rank:
            # increment rank only if both sets have same rank
            if parent1.rank == parent2.rank:
                parent1.rank = parent1.rank + 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2

        self.num_sets -= 1 # union decreases the number of disjoint sets by one

    # Finds the representative of this set
    def find_set(self, data):
        return self.find_set_util(self.map[data]) # pass in the node

    # Find the representative recursively and does path compression as well.
    def find_set_util(self, node):
        parent = node.parent
        if parent == node:
            return parent

        node.parent = self.find_set_util(node.parent) # path compression
        return node.parent

if __name__ == '__main__':
    ds = DisjointSet()
    ds.make_set(1)
    ds.make_set(2)
    ds.make_set(3)
    ds.make_set(4)
    ds.make_set(5)
    ds.make_set(6)
    ds.make_set(7)

    ds.union(1,2)
    ds.union(2,3)
    ds.union(4,5)
    ds.union(6,7)
    ds.union(5,6)
    ds.union(3,7)


    for i in range(1, 8):
        print(ds.find_set(i))
