from disjoint_set import *
from graph import *

"""
O(E + V) space.O(ElogE + E) time.

Note: ElogE is how long it takes for sorting edges. E is disjoing set time.

problems: https://www.hackerearth.com/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/1/?sort_by=partially%20solved&p_level=

ALGORITHM:

NOTE: USE DISJOINT SETS
0) Create a result list to store the fianl results

1) Sort edges in non-decreasing order (ASC)

2) Make set out of all the edges

3) Pick one edge at a time and check both vertices on that edge to see if they belong to the same disjoing set

4) If they belong to the same ignore this edge(continue)

5) I they don't, union these vertices on that edge and append the edge to the result list

6) Return the result list
"""
def minimum_spanning_tree(graph):
    disjoint_set = DisjointSet()

    # very important
    sorted_edges = sorted(graph.get_all_edges(), key=lambda x:x[0].get_weight(x[1]))
    print [(from_vert.id, to_vert.id) for from_vert, to_vert in sorted_edges]

    # [(1, 3), (2, 5), (2, 4), (4, 7), (6, 5), (2, 6), (6, 4), (1, 2), (3, 4), (3, 7)]

    for vertex in graph:
        disjoint_set.make_set(vertex.id)

    result_edge = []

    for from_vert, to_vert in sorted_edges:
        root1 = disjoint_set.find_set(from_vert.id)
        root2 = disjoint_set.find_set(to_vert.id)

        if root1 == root2:
            continue
        else:
            result_edge.append([from_vert, to_vert])
            disjoint_set.union(from_vert.id, to_vert.id)

    return result_edge

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(1,3,1)
    graph.add_edge(1,2,4)
    graph.add_edge(2,4,2)
    graph.add_edge(2,5,1)
    graph.add_edge(2,6,3)
    graph.add_edge(3,4,5)
    graph.add_edge(3,7,8)
    graph.add_edge(4,7,2)
    graph.add_edge(6,5,2)
    graph.add_edge(6,4,3)

    result = minimum_spanning_tree(graph)
    for from_vert, to_vert in result:
        print([from_vert.id, to_vert.id])
