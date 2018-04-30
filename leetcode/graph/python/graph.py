from sys import maxint
class Vertex(object):
    def __init__(self, key):
        """
        The discovery time tracks the number of steps in the algorithm before a vertex is first encountered.

        The finish time is the number of steps in the algorithm before a vertex is colored black.
        """
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.dist = maxint
        self.pred = None
        self.disc = 0
        self.fin = 0

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    # def __repr__(self):
    #     return self.__str__()

    # def __eq__(self, other):
    #     return self.id == other.id

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def get_distance(self):
        return self.dist

    def get_color(self):
        return self.color

    def get_pred(self):
        return self.pred

    def get_finish(self):
        return self.fin

    def set_finish(self, finish):
        self.fin = finish

    def set_distance(self, new_distance):
        self.dist = new_distance

    def set_pred(self, new_pred):
        self.pred = new_pred

    def set_color(self, new_color):
        self.color = new_color

class Graph(object):
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0
        self.edges = []

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        return self.vert_list.get(n)

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vert_list:
            nv = self.add_vertex(from_vertex)

        if to_vertex not in self.vert_list:
            nv = self.add_vertex(to_vertex)

        self.vert_list[from_vertex].add_neighbor(self.vert_list[to_vertex], cost)

        self.edges.append( (self.vert_list[from_vertex], self.vert_list[to_vertex]) )

    def get_vertices(self):
        return self.vert_list.keys()

    def get_all_edges(self):
        return self.edges

    def __iter__(self):
        return iter(self.vert_list.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    # print g.vert_list
    print('\n')
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)

    # for vertex in g:
    #     for connection in vertex.get_connections():
    #         print('(%s, %s)' % (vertex.get_id(), connection.get_id()))

    all_edges = g.get_all_edges()

    # print all_edges
    print [(x.id, y.id) for x, y in all_edges]
