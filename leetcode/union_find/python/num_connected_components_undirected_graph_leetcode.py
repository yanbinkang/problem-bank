"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/#/description

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

     0          3
     |          |
     1 --- 2    4

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4
     |           |
     1 --- 2 --- 3

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Space: O(n) where n is number of elements in the set

Time: For m operations and total n elements time complexity is O(m*f(n)) where f(n) is very slowly growing function. For most cases f(n) <= 4 so effectively total time will be O(m). Proof in Coreman book.

Algorithm:

1) if we have n = 5 with nodes startign from 0, the max node will be 5. So make set out of all nodes range(5) => [0, 1, 2, 3, 4]

2) Union all edges for from_vert, to_vert in each edge.

3) return the number of sets i.e ds.num_sets
"""
from disjoint_set import *

def count_components(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    ds = DisjointSet()

    for i in range(n):
        ds.make_set(i)

    for i, j in edges:
        ds.union(i, j)

    return ds.num_sets

if __name__ == '__main__':
    print count_components(5, [[0, 1], [1, 2], [3, 4]]) #2
    print('\n')
    print count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) #1
