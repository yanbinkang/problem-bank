import os, sys
sys.path.insert(0, os.path.abspath(".."))
from graphs_and_graph_algorithms.graph import Graph

def knight_tour(current_depth, vert_visited_list, vert_to_explore, num_nodes_in_path):
    vert_to_explore.set_color('gray')
    vert_visited_list.append(vert_to_explore)
    if current_depth < num_nodes_in_path:
        nbr_list = list(vert_to_explore.get_connections())
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == 'white':
                done = knight_tour(current_depth+1, vert_visited_list, nbr_list[i], num_nodes_in_path)
            i = i + 1
        if not done: # prepare to backtrack
            vert_visited_list.pop()
            vert_to_explore.set_color('white')
    else:
        done = True
    return done


def order_by_avail(n):
    res_list = []
    for v in n.get_connections():
        if v.get_color() == 'white':
            c = 0
            for w in v.get_connections():
                if w.get_color() == 'white':
                    c = c + 1
            res_list.append((c, v))
    res_list.sort(key=lambda x:x[0])
    return [y[1] for y in res_list]
