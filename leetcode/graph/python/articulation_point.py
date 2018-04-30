"""
Find articulation points in connected undirected graph.
Articulation points are vertices such that removing any one of them disconnects the graph.

We need to do DFS of this graph and keep visitedTime and lowTime for each vertex.
lowTime is keeps track of back edges.

If any one of following condition meets then vertex is articulation point.

1) If vertex is root of DFS and has atlesat 2 independent children.(By independent it means they are
not connected to each other except via this vertex). This condition is needed because if we
started from corner vertex it will meet condition 2 but still is not an articulation point. To filter
out those vertices we need this condition.

2) It is not root of DFS and if visitedTime of vertex <= lowTime of any adjacent vertex then its articulation point.

Time complexity is O(E + V)
Space complexity is O(V)

References:
https://en.wikipedia.org/wiki/Biconnected_component
http://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
"""
from graph import *
class ArticulationPoint(object):
    def __init__(self):
        self.time = 0

    def find_articulation_point(self, graph):
        visited = set()
        articulation_points = []
        vertex = next(iter(graph.get_vertices()))

        start_vertex = graph.get_vertex(vertex)

        visited_time = {}
        low_time = {}
        parent = {}

        self.dfs(visited, articulation_points, start_vertex, visited_time, low_time, parent)

        return articulation_points

    def dfs(self, visited, articulation_points, vertex, visited_time, low_time, parent):
            visited.add(vertex)
            visited_time[vertex] = self.time
            low_time[vertex] = self.time
            self.time += 1
            child_count = 0
            is_articulation_point = False

            for nbr in vertex.get_connections():
                # if nbr is same as parent then just ignore this vertex.
                if nbr == parent.get(vertex):
                    continue

                if nbr not in visited:
                    parent[nbr] = vertex
                    child_count += 1
                    self.dfs(visited, articulation_points, nbr, visited_time, low_time, parent)

                    if visited_time.get(vertex) <= low_time.get(nbr):
                        is_articulation_point = True
                    else:
                        low_time[vertex] = min(low_time[vertex], low_time[nbr])

                else:
                    low_time[vertex] = min(low_time[vertex], visited_time[nbr])

            if parent.get(vertex) is None and child_count >= 2 or\
                parent.get(vertex) is not None and is_articulation_point:
                    articulation_points.append(vertex)

if __name__ == '__main__':
    graph = Graph()
    # graph.add_edge(1, 2)
    # graph.add_edge(2, 3)
    # graph.add_edge(1, 3)
    # graph.add_edge(1, 4)
    # graph.add_edge(4, 5)
    # graph.add_edge(5, 6)
    # graph.add_edge(6, 7)
    # graph.add_edge(7, 5)
    # graph.add_edge(6, 8)

    graph.add_edge('a', 'b')
    graph.add_edge('b', 'a')
    graph.add_edge('a', 'c')
    graph.add_edge('c', 'a')
    graph.add_edge('b', 'c')
    graph.add_edge('c', 'b')
    graph.add_edge('c', 'd')
    graph.add_edge('d', 'c')

    ap = ArticulationPoint()

    a_points = ap.find_articulation_point(graph)

    for point in a_points:
        print point
        print('\n')
