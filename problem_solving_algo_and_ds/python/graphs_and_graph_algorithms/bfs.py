import os, sys
sys.path.insert(0, os.path.abspath(".."))
from data_structures.queue import Queue
from graphs_and_graph_algorithms.graph import Graph, Vertex

def bfs(g, start):
    start.set_distance(0)
    start.set_pred(None)
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while (vert_queue.size() > 0):
        current_vert = vert_queue.dequeue()
        for nbr in current_vert.get_connections():
            if (nbr.get_color() == 'white'):
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_pred(current_vert)
                vert_queue.enqueue(nbr)
        current_vert.set_color('black')

def traverse(y):
    x = y
    while (x.get_pred()):
        print(x.get_id())
        x = x.get_pred()
    print(x.get_id())

