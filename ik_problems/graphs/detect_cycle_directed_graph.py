from graph import Graph
class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph, self).__init__()

    def is_cyclic(self):
        for a_vertex in self:
            a_vertex.color = 'white'

        for a_vertex in self:
            if a_vertex.color == 'white':
                result = self.is_cyclic_util(a_vertex)
                if result:
                    return True

        return False

    def is_cyclic_util(self, start_vertex):
        if start_vertex.color == 'gray':
            return True

        start_vertex.color = 'gray'

        for next_vertex in start_vertex.get_connections():
            result = self.is_cyclic_util(next_vertex)
            if result:
                return True

        start_vertex.color = 'black'
        return False

if __name__ == '__main__':
    g = DFSGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(2, 5)
    g.add_edge(5, 3)

    print(g.is_cyclic())
