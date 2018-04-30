import os, sys
sys.path.insert(0, os.path.abspath(".."))
from graphs_and_graph_algorithms.graph import Graph

"""
ref: https://www.youtube.com/watch?v=RpgcYiky7uw
ref: http://interactivepython.org/runestone/static/pythonds/Graphs/StronglyConnectedComponents.html

Algorithm (Kosaraju's):
1) create an order of vertices by finish time in decreasing order
2) reverse the graph
3) do a dfs on reversed graph by finish time of vertex in decreasing order
4) each forest computed in 3 is a strongly connected component
"""
def strongly_connected_components(graph):
    stack = []
    visited = set()

    for a_vertex in graph:
        if a_vertex in visited:
            continue
        dfs_visit(a_vertex, visited, stack)

    reverse_graph = transpose(graph)

    visited.clear()
    res = []

    while stack != []:
        vert = reverse_graph.get_vertex(stack.pop().get_id())

        if vert in visited:
            continue

        _set = set()
        dfs_visit_reverse_graph(vert, visited, _set)
        res.append(_set)

    return res

def dfs_visit(start_vert, visited, stack):
    visited.add(start_vert)

    for next_vert in start_vert.get_connections():
        if next_vert in visited:
            continue
        dfs_visit(next_vert, visited, stack)
    stack.append(start_vert)

def dfs_visit_reverse_graph(start_vert, visited, _set):
    visited.add(start_vert)
    _set.add(start_vert.get_id())

    for next_vert in start_vert.get_connections():
        if next_vert in visited:
            continue
        dfs_visit_reverse_graph(next_vert, visited, _set)

def transpose(graph):
    reverse_graph = Graph()
    for v in graph:
        for nbr in v.get_connections():
            reverse_graph.add_edge(nbr.get_id(), v.get_id())

    return reverse_graph

if __name__ == '__main__':
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'e')
    g.add_edge('e', 'd')
    g.add_edge('d', 'b')
    g.add_edge('e', 'a')
    g.add_edge('d', 'g')
    g.add_edge('g', 'e')
    g.add_edge('b', 'c')
    g.add_edge('c', 'c')
    g.add_edge('c', 'f')
    g.add_edge('f', 'h')
    g.add_edge('h', 'i')
    g.add_edge('i', 'f')

    res = strongly_connected_components(g)

    print res
