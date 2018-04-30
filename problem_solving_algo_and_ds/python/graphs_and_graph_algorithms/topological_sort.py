import os, sys
sys.path.insert(0, os.path.abspath(".."))
from graphs_and_graph_algorithms.graph import Graph

"""
ref: http://interactivepython.org/runestone/static/pythonds/Graphs/TopologicalSorting.html
ref: https://www.youtube.com/watch?v=ddTC4Zovtbc
space and time complexity: O(n)
"""

class TopologicalSort(Graph):
    def __init__(self):
        super(TopologicalSort, self).__init__()
        self.time = 0
        self.topological_list = []

    def topological_sort(self):
        for a_vert in self:
            a_vert.set_color('white')
            a_vert.set_pred(-1)
        for a_vert in self:
            if a_vert.get_color() == 'white':
                self.dfs_visit(a_vert)
        return self.topological_list

    def dfs_visit(self, start_vert):
        start_vert.set_color('gray')
        self.time += 1
        start_vert.set_discovery(self.time)

        for next_vert in start_vert.get_connections():
            if next_vert.get_color() == 'white':
                next_vert.set_pred(start_vert)
                self.dfs_visit(next_vert)
        start_vert.set_color('black')
        self.time += 1
        start_vert.set_finish(self.time)
        self.topological_list.insert(0, start_vert.get_id())


if __name__ == '__main__':
    g = TopologicalSort()
    g.add_edge('a', 'c')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('c', 'e')
    g.add_edge('e', 'f')
    g.add_edge('d', 'f')
    g.add_edge('f', 'g')


    print g.topological_sort()
