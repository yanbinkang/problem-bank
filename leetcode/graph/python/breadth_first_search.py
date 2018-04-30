from graph import *

"""
bfs explanation: http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html

Analysis: http://interactivepython.org/runestone/static/pythonds/Graphs/BreadthFirstSearchAnalysis.html

O(v) time where v is the vertices in the graph
"""
def bfs(g, start):
    start.set_distance(0)
    start.set_pred(None)

    vert_queue = []
    vert_queue.append(start)

    while vert_queue:
        current_vert = vert_queue.pop() # dequeue queue

        for nbr in current_vert.get_connections():
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vert.get_distance() + 1)
                nbr.set_pred(current_vert)
                vert_queue.insert(0, nbr) # enqueue queue

        current_vert.set_color('black')

