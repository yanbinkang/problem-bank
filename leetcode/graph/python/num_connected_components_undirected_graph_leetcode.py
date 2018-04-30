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
"""
from graph import *
def count_components(n, edges):
    components = 0
    g = Graph()

    for from_vertex, to_vertex in edges:
        g.add_edge(from_vertex, to_vertex)
        g.add_edge(to_vertex, from_vertex)

    visited = set()
    stack = []

    for vertex in g:
        if vertex not in visited:
            dfs(vertex, stack, visited)
            components += 1

    return components

def dfs(vertex, stack, visited):
    visited.add(vertex)
    stack.append(vertex)

    while stack:
        current = stack.pop()

        for nbr in current.get_connections():
            if nbr not in visited:
                visited.add(nbr)
                stack.append(nbr)

def count_components_1(n, edges):
    graph = {x: [] for x in range(n)}

    visited = set()

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    components = 0

    for i in range(n):
        if i not in visited:
            _dsf(i, visited, graph)
            components += 1

    return components

def _dsf(node, visited, graph):
    visited.add(node)

    for nbr in graph[node]:
        if nbr not in visited:
            _dsf(nbr, visited, graph)

def count_components_2(n, edges):
    graph = {x: [] for x in range(n)}

    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    queue = []
    visited = set()

    components = 0

    for i in range(n):
        if i not in visited:
            bfs(i, queue, visited, graph)
            components += 1

    return components

def bfs(node, queue, visited, graph):
    visited.add(node)
    queue.append(node)

    while queue:
        current = queue.pop()

        for nbr in graph[current]:
            if nbr not in visited:
                visited.add(nbr)
                queue.insert(0, nbr)


if __name__ == '__main__':
    print count_components(5, [[0, 1], [1, 2], [3, 4]]) #2
    print('\n')
    print count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) #1
    print('\n')
    print count_components_1(5, [[0, 1], [1, 2], [3, 4]]) #2
    print('\n')
    print count_components_1(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) #1
    print('\n')
    print count_components_2(5, [[0, 1], [1, 2], [3, 4]]) #2
    print('\n')
    print count_components_2(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) #1


