"""
https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/tutorial/

Given a weighted undirected graph. Find the sum of weights of edges of a Minimum Spanning Tree.
"""
from disjoint_set import *

def find_sum_of_weights(n, input):
    result = []
    ds = DisjointSet()

    sorted_edges = sorted(input, key=lambda x:x[2])

    for i in range(1, n + 1):
        ds.make_set(i)

    for from_vert, to_vert, weight in sorted_edges:
        root1 = ds.find_set(from_vert)
        root2 = ds.find_set(to_vert)

        if root1 == root2:
            continue
        else:
            result.append([from_vert, to_vert, weight])
            ds.union(from_vert, to_vert)

    return sum([z for x, y, z in result])

if __name__ == '__main__':
    print find_sum_of_weights(4, [[1, 2, 7], [1, 4, 6], [4, 2, 9], [4, 3, 8], [2, 3, 6]])
