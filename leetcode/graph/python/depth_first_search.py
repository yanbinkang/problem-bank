"""
http://interactivepython.org/runestone/static/pythonds/Graphs/GeneralDepthFirstSearch.html

O(V + E) time
"""
from graph import *
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for a_vertex in self:
            a_vertex.set_color('white')
            a_vertex.set_pred(-1)

        for a_vertex in self:
            if a_vertex.get_color() == 'white':
                self.dfs_visit(a_vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)

        for next_vert in start_vertex.get_connections():
            if next_vert.get_color() == 'white':
                next_vert.set_pred(start_vertex)
                self.dfs_visit(next_vert)

        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish(self.time)
