import os, sys
sys.path.insert(0, os.path.abspath(".."))
from graphs_and_graph_algorithms.graph import Graph

def knight_graph(bd_size):
    kt_graph = Graph()
    for row in range(bd_size):
        for col in range(bd_size):
            node_id = pos_to_node_id(row, col, bd_size)
            new_positions = gen_legal_moves(row, col, bd_size)
            for e in new_positions:
                n_id = pos_to_node_id(e[0], e[1], bd_size)
                kt_graph.add_edge(node_id, n_id)
    return kt_graph

def pos_to_node_id(row, column, board_size):
    return (row * board_size) + column

def gen_legal_moves(x, y, bd_size):
    new_moves = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in move_offsets:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coord(new_x, bd_size) and legal_coord(new_y, bd_size):
            new_moves.append(new_x, new_y)
    return new_moves

def legal_coord(x, bd_size):
    if x >= 0 and x < bd_size:
        return True
    else:
        return False
