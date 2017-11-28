"""
https://leetcode.com/problems/graph-valid-tree/#/description

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint: According to the definition of tree on Wikipedia: "a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree."

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

algorithm:
similar to cycle in undirected graph algorithm

1. Get all the vertexes and make a set out of each of them
2. For each edge in the graph (i.e from_vert, to_vert) find its parent. If the parents are the same, we have a cycle. Return False

If parents are different (meaning they are not in the same set and adding these two sets will not create a cycle) union these two sets.

If all edges are connected we have exactly one set. Return ds.num_sets == 1

O(v) time and space
"""
from disjoint_set import *
def valid_tree(n, edges):
    ds = DisjointSet()

    for i in range(n):
        ds.make_set(i)

    for from_vert, to_vert in edges:
        parent1 = ds.find_set(from_vert)
        parent2 = ds.find_set(to_vert)

        if parent1 == parent2:
            return False
        ds.union(from_vert, to_vert)

    return ds.num_sets == 1

if __name__ == '__main__':
    print valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print('\n')
    print valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
