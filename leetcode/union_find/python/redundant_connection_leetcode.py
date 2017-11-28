"""
https://leetcode.com/problems/redundant-connection/description/

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: Original tree will be like this:
  1
 / \
2 - 3


Example 2:
Input: [[1,2], [1,3], [3,1]]
Output: [3,1]
Explanation: Original tree will be like this:
  1
 / \\
2   3


Note:
    * The size of the input 2D-array will be between 1 and 1000.
    * Every integer represented in the 2D-array will be between 1 and 2000.

Algo: we basically want to find all the edges that form a cycle and return the last one.

Very similar to finding a cycle in an undirected graph.
"""
from disjoint_set import *

def findRedundantConnection(edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    ds = DisjointSet()
    result = []

    for u, v in edges:
        ds.make_set(u)
        ds.make_set(v)

    for u, v in edges:
        parent1 = ds.find_set(u)
        parent2 = ds.find_set(v)

        if parent1 == parent2: # cycle, add to result
            result.append([u, v])
        else:
            ds.union(u, v)

    return result[-1]

if __name__ == '__main__':
    print findRedundantConnection([[1,2], [1,3], [3,1]])
    print findRedundantConnection([[1,2], [1,3], [2,3]])
    print findRedundantConnection([[2,3],[5,2],[1,5],[4,2],[4,1]])
    print findRedundantConnection([[2,3],[5,3],[2,1],[5,4],[3,2]])
    print findRedundantConnection([[2,1],[3,1],[4,2],[1,4]])
