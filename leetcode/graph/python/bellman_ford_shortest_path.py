"""
 Write program for Bellman Ford algorithm to find single source shortest path in directed graph.

Bellman ford works with negative edges as well unlike Dijksra's algorithm. If there is negative weight cycle it detects it.

  Time complexity - O(EV)
  Space complexity - O(V)

  References
  https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
  http://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/
"""
from graph import *
class NegativeWeightCycleException(Exception):
    def __init__(self):
        pass

def get_shortest_path(graph, source_vertex):
    distance = {}
    parent = {}

    # set distance of every vertex to be infinity initially
    for vertex in graph:
        distance[vertex] = float('inf')
        parent[vertex] = None

    # set distance of source vertex to be 0
    distance[source_vertex] = 0

    num_vert = graph.num_vertices

    # relax edges repeatedly V - 1 times
    for i in range(num_vert - 1):
        for u, v in graph.get_all_edges():
            """
            relax the edge if we get better distance to v via u then use this distance and set u as parent of v.
            """
            weight = u.get_weight(v)
            u_dist = distance[u]
            v_dist = distance[v]
            if u_dist + weight < v_dist:
                distance[v] = u_dist + weight
                parent[v] = u


    """
    relax all edges again. If we still get lesser distance it means there is negative weight cycle in the graph. Throw exception in that case
    """
    for u, v in graph.get_all_edges():
        if distance[u] + u.get_weight(v) < distance[v]:
            raise NegativeWeightCycleException()


    return distance

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 3, 8)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 5)
    graph.add_edge(1, 2, -3)
    graph.add_edge(2, 4, 4)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 3, 1)


    start_vert_key = next(iter(graph.get_vertices()))

    start_vert = graph.get_vertex(start_vert_key)

    distance = get_shortest_path(graph, start_vert)

    print distance


