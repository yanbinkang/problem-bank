from graph import *
"""
O(V + E) time
"""
def dfs(graph):
    visited = set()
    for vertex in graph:
        dfs_util(vertex, visited)

def dfs_util(vertex, visited):
    if vertex in visited:
        return

    visited.add(vertex)

    print vertex.get_id()

    for neighbor in vertex.get_connections():
        dfs_util(neighbor, visited)

"""
O(v) time where v is the vertices in the graph
"""
def bfs(graph):
    visited = set()
    queue = []

    for vertex in graph:
        if vertex not in visited:
            queue.append(vertex)
            visited.add(vertex)

            while queue:
                current = queue.pop()
                print current.get_id()
                for nbr in current.get_connections():
                    if nbr not in visited:
                        queue.insert(0, nbr)
                        visited.add(nbr)

if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 4)

    dfs(g)
    print('\n')
    bfs(g)

