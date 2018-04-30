from graph import *
"""
Use set and stack. Idea is to start from any vertex and put it in the visited set (if it's not already in the visited set). Then explore its neighbors. Put each neighbor in the visited set.

when a neighbor has no futher neighbors to explore (i.e its been totally explored - it's has no more neighbors or all it's neighbors are in the visited set) you put it in the stack. Do this till all vertexes are in the visited set. Finally reverse the stack and return it as the finaly result.
"""
def topological_sort(graph):
    stack = []
    visited = set()

    for vertex in graph:
        if vertex in visited:
            continue

        top_sort_util(vertex, stack, visited)

    return stack

def top_sort_util(vertex, stack, visited):
    visited.add(vertex)

    for neighbor in vertex.get_connections():
        if neighbor in visited:
            continue
        top_sort_util(neighbor, stack, visited)

    stack.append(vertex)

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(1, 3)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)
    graph.add_edge(5, 6)
    graph.add_edge(6, 3)
    graph.add_edge(3, 8)
    graph.add_edge(8, 11)

    res = topological_sort(graph)

    print [vertex.get_id() for vertex in res][::-1]

