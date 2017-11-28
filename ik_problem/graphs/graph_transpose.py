from graph import Graph, Vertex

def transpose(graph):
    reverse_graph = Graph()
    for v in graph:
        for nbr in v.get_connections():
            reverse_graph.add_edge(nbr.get_id(), v.get_id())

    return reverse_graph




if __name__ == '__main__':
    g = Graph()
    g.add_edge('a', 'b')
    g.add_edge('a', 'c')
    g.add_edge('b', 'd')
    g.add_edge('d', 'a')

    res = transpose(g)
    for v in res:
        print v
