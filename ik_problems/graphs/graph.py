from sys import maxsize

class  Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.color = 'white'
        self.dist = maxsize
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

    def set_color(self, color):
        self.color = color

    def set_distance(self, dist):
        self.dist = dist

    def set_pred(self, p):
        self.pred = p

    def set_discovery(self, dtime):
        self.disc = dtime

    def set_finish(self, ftime):
        self.fin = ftime


class Graph(object):
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
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
