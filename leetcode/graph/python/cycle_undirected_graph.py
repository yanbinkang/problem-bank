from graph import *
from disjoint_set import *

"""
1. Maintain a visited set

2. Do dfs for each vertex in the graph with a pointer to the vertex's parent

3. In the dfs, find the neighbors of the vertex. If the parent is present and the vertex's neighbor is same as its parent, continue. This because we're dealing with an undirected graph and edges will move not just in one direction but all directions. We do this because we don't want to visit the parent link again.

If neighbor in visited set return True cos we've found a cycle

Do this for all vertexes in graph

O(v) time and space
"""
def has_cycle_dfs(graph):
    visited = set()

    for vertex in graph:
        if vertex in visited:
            continue

        if has_cycle_dfs_util(vertex, visited, None):
            return True

    return False

def has_cycle_dfs_util(vertex, visited, parent):
    visited.add(vertex)

    for neighbor in vertex.get_connections():
        if parent and neighbor == parent:
            continue

        if neighbor in visited:
            return True

        if has_cycle_dfs_util(neighbor, visited, vertex):
            return True

    return False


"""
1. Get all the vertexes and make a set out of each of them
2. For each edge in the graph (i.e from_vert, to_vert) find its parent. If the parents are the same, we have a cycle.

If parents are different (meaning they are not in the same set. and adding these two sets will not create a cycle) union two sets.

O(v) time and space
"""
def has_cycle_using_disjoint_set(graph):
    ds = DisjointSet()

    for vertex in graph.get_vertices():
        ds.make_set(vertex)

    for from_vert, to_vert in graph.get_all_edges():
        parent1 = ds.find_set(from_vert.id)
        parent2 = ds.find_set(to_vert.id)

        if parent1 == parent2:
            return True
        ds.union(from_vert.id, to_vert.id) # union different parents

    return False

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(0,3)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(5,1)

    has_cycle1 = has_cycle_using_disjoint_set(graph)
    print has_cycle1
    print('\n')
    has_cycle2 = has_cycle_dfs(graph)
    print has_cycle2
