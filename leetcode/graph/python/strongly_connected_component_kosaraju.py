from graph import *
"""
Given a directed graph, find all strongly connected components in this graph.
We are going to use Kosaraju's algorithm to find strongly connected component.

Algorithm
Create a order of vertices by finish time in decreasing order.
Reverse the graph
Do a DFS on reverse graph by finish time of vertex and created strongly connected
components.

Runtime complexity - O(V + E)
Space complexity - O(V)

References
https://en.wikipedia.org/wiki/Strongly_connected_component
http://www.geeksforgeeks.org/strongly-connected-components/
https://youtu.be/RpgcYiky7uw?list=PLrmLmBdmIlpu2f2g8ltqaaCZiq6GJvl1j
"""
def strongly_connected_components(graph):
    stack = []
    visited = set()

    for vertex in graph:
        if vertex in visited:
            continue

        dfs_visit(vertex, visited, stack)

    reversed_graph = reverse_graph(graph)

    visited.clear()
    result = [] # store strongly connected components

    while stack:
        item = stack.pop()

        vert = reversed_graph.get_vertex(item.get_id())

        if vert in visited:
            continue

        connected_components = set()

        dfs_visit_reversed_graph(vert, visited, connected_components)
        result.append(connected_components)

    return result

def dfs_visit(vertex, visited, stack):
    visited.add(vertex)

    for neighbor in vertex.get_connections():
        if neighbor in visited:
            continue

        dfs_visit(neighbor, visited, stack)
    stack.append(vertex)

def dfs_visit_reversed_graph(vertex, visited, connected_components):
    visited.add(vertex)
    connected_components.add(vertex.get_id())


    for neighbor in vertex.get_connections():
        if neighbor in visited:
            continue

        dfs_visit_reversed_graph(neighbor, visited, connected_components)

def reverse_graph(graph):
    reversed_graph = Graph()
    for vertex in graph:
        for nbr in vertex.get_connections():
            reversed_graph.add_edge(nbr.get_id(), vertex.get_id())

    return reversed_graph

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 3)
    graph.add_edge(5, 6)

    scc = strongly_connected_components(graph)

    print scc

