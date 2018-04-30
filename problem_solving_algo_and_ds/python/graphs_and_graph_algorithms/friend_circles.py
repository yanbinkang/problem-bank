import os, sys
sys.path.insert(0, os.path.abspath(".."))
from graphs_and_graph_algorithms.graph import Graph

"""
ref: https://www.hackerrank.com/contests/juniper-hackathon/challenges/friend-circles
"""
def friend_circle_strongly_connected_components(graph):
    stack = []
    visited = set()

    for a_vert in graph:
        if a_vert in visited:
            continue
        dfs_visit(a_vert, visited, stack)

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


    return len(res)

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
    matrix = [['Y', 'Y', 'N', 'N'],
              ['Y', 'Y', 'Y', 'N'],
              ['N', 'Y', 'Y', 'N'],
              ['N', 'N', 'N', 'Y']]

    mat_2 = [['Y', 'N', 'N', 'N', 'N'],
             ['N', 'Y', 'N', 'N', 'N'],
             ['N', 'N', 'Y', 'N', 'N'],
             ['N', 'N', 'N', 'Y', 'N'],
             ['N', 'N', 'N', 'N', 'Y']]

    matrix3 =  [['Y', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N'],
                ['N', 'Y', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'Y'],
                ['N', 'N', 'Y', 'N', 'Y', 'N', 'N', 'N', 'N', 'N'],
                ['N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N'],
                ['N', 'N', 'Y', 'N', 'Y', 'N', 'N', 'N', 'N', 'N'],
                ['N', 'Y', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N'],
                ['Y', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N'],
                ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N'],
                ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N'],
                ['N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y']]

    g = Graph()
    n = len(matrix)
    i = 0
    while i < n:
        j = 0
        while j < n:
            if matrix[i][j] == 'Y':
                g.add_edge(i, j, 'Y')
            j += 1
        i += 1

    print friend_circle_strongly_connected_components(g)
    print('\n')

    g1 = Graph()
    m = len(mat_2)
    x = 0
    while x < m:
        y = 0
        while y < m:
            if mat_2[x][y] == 'Y':
                g1.add_edge(x, y, 'Y')
            y += 1
        x += 1

    print friend_circle_strongly_connected_components(g1)
    print('\n')

    g2 = Graph()
    m = len(matrix3)
    x = 0
    while x < m:
        y = 0
        while y < m:
            if matrix3[x][y] == 'Y':
                g2.add_edge(x, y, 'Y')
            y += 1
        x += 1
    print friend_circle_strongly_connected_components(g2)
