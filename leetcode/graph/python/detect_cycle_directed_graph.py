from graph import *
"""
Detect cycle in directed graph.

watch: https://youtu.be/rKQaZuoUR4M?list=PLrmLmBdmIlpu2f2g8ltqaaCZiq6GJvl1j

WHITE : Vertex is not processed yet.  Initially
        all vertices are WHITE.

GRAY : Vertex is being processed (DFS for this
       vertex has started, but not finished which means
       that all descendants (ind DFS tree) of this vertex
       are not processed yet (or this vertex is in function
       call stack)

BLACK : Vertex and all its descendants are
        processed.

While doing DFS, if we encounter an edge from current
vertex to a GRAY vertex, then this edge is back edge
and hence there is a cycle.

O(V + E) time, O(V) space
"""
def has_cycle(graph):
    white_set = set()
    gray_set = set()
    black_set = set()

    for vertex in graph:
        white_set.add(vertex)

    while len(white_set) > 0:
        current = next(iter(white_set))

        if dfs(current, white_set, gray_set, black_set):
            return True

    return False

def dfs(current, white_set, gray_set, black_set):
    move_vertex(current, white_set, gray_set)

    for neighbor in current.get_connections():
        # if in black set means already explored so continue
        if neighbor in black_set:
            continue

        # if in gray set then cycle found.
        if neighbor in gray_set:
            return True

        if dfs(neighbor,  white_set, gray_set, black_set):
            return True

    # move vertex from gray set to black set when done exploring
    move_vertex(current, gray_set, black_set)
    return False

def move_vertex(vertex, source_set, destination_set):
    source_set.remove(vertex)
    destination_set.add(vertex)

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(4, 1)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)

    print has_cycle(graph)
