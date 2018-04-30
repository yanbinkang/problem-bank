import os, sys
sys.path.insert(0, os.path.abspath(".."))
from graphs_and_graph_algorithms.graph import Graph, Vertex
from graphs_and_graph_algorithms.priority_queue import PriorityQueue

def dijkstra(a_graph, start):
    pq = PriorityQueue()
    start.set_distance(0)
    pq.build_heap([(v.get_distance(), v) for v in a_graph])
    while not pq.is_empty():
        current_vert = pq.del_min()
        for next_vert in current_vert.get_connections():
            new_dist = current_vert.get_distance() + current_vert.get_weight(next_vert)
            if new_dist < next_vert.get_distance():
                next_vert.set_distance(new_dist)
                next_vert.set_pred(current_vert)
                pq.decrease_key(next_vert, new_dist)
