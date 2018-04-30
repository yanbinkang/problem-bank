from sys import maxint
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.dist = maxint
        self.pred = None
        self.disc = 0
        self.fin = 0

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def get_color(self):
        return self.color

    def get_distance(self):
        return self.dist

    def get_pred(self):
        return self.pred

    def get_discovery(self):
        return self.disc

    def get_finish(self):
        return self.fin

    def set_discovery(self, dtime):
        self.disc = dtime

    def set_finish(self, ftime):
        self.fin = ftime

    def set_color(self, color):
        self.color = color

    def set_distance(self, dist):
        self.dist = dist

    def set_pred(self, p):
        self.pred = p

class Graph(object):
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vert_list:
            nv = self.add_vertex(from_vertex)
        if to_vertex not in self.vert_list:
            nv = self.add_vertex(to_vertex)
        self.vert_list[from_vertex].add_neighbor(self.vert_list[to_vertex], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


# g = Graph()
# for i in range(6):
#     g.add_vertex(i)

# # print g.vert_list
# g.add_edge(0, 1, 5)
# g.add_edge(0, 5, 2)
# g.add_edge(1, 2, 4)
# g.add_edge(2, 3, 9)
# g.add_edge(3, 5, 3)
# g.add_edge(3, 4, 7)
# g.add_edge(4, 0, 1)
# g.add_edge(5, 2, 1)
# g.add_edge(5, 4, 8)
# for v in g:
#     for w in v.get_connections():
#         print("( %s, %s )" % (v.get_id(), w.get_id()))
