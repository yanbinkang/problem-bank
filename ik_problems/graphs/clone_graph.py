from graph import Graph, Vertex

def clone(start):
    hash_map = {}
    queue = []

    queue.insert(0, start)

    vert = Vertex(start.id)
    hash_map[start] = vert

    while len(queue) > 0:
        current_vert = queue.pop()
        for nbr in current_vert.get_connections():
            x = hash_map.get(nbr)

            if x == None:
                p = Vertex(nbr.id)
                hash_map[current_vert].add_neighbor(p)
                hash_map[nbr] = p
                queue.insert(0, nbr)
            else:
                hash_map[current_vert].add_neighbor(hash_map[nbr])

    return vert


if __name__ == '__main__':
    # g = Graph()
    # g.add_edge(1, 2)
    # g.add_edge(1, 3)
    # g.add_edge(3, 4)
    # g.add_edge(4, 5)
    # g.add_edge(2, 5)
    # g.add_edge(5, 3)

    g = Graph()
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(2, 2)

    # for vert in g:
    #     print vert

    res = clone(g.get_vertex(1))

    # print start vertex and it's connections
    print res

    # print all other connections
    for nbr in res.get_connections():
        print nbr
