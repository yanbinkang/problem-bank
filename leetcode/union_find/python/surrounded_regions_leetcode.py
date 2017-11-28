"""
https://leetcode.com/problems/surrounded-regions/#/description

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

solution: The idea comes from the observation that if a region is NOT captured, it is connected to the boundary (edge of the board). So if we connect all the 'O' nodes on the boundary to a dummy node, and then connect each internal 'O' node to its neighbour 'O' nodes, then we can tell directly whether a 'O' node is captured by checking whether it is connected to the dummy node.
"""
from disjoint_set import *
def solve(board):
    ds = DisjointSet()
    dummy_node = ds.make_set(-1)

    # make set for all 'O' nodes
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                ds.make_set((i, j))

    for i in range(len(board)):
        for j in range(len(board[0])):
            # connect all boundary nodes to dummy node
            if (i == 0 or i == len(board) - 1 or\
                j == 0 or j == len(board[0]) - 1) and\
                board[i][j] == 'O':
                    ds.union((i, j), -1)
            elif board[i][j] == 'O':
                cell = (i, j)

                # up
                if i > 0 and board[i - 1][j] == 'O':
                    ds.union(cell, (i-1, j))

                # down
                if i < len(board) - 1 and board[i + 1][j] == 'O':
                    ds.union(cell, (i + 1, j))

                # left
                if j > 0 and board[i][j - 1] == 'O':
                    ds.union(cell, (i, j - 1))

                # right
                if j < len(board[0]) - 1 and board[i][j + 1] == 'O':
                    ds.union(cell, (i, j + 1))

    dummy_set_rep = ds.find_set(-1)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                set_rep = ds.find_set((i, j))

                if dummy_set_rep != set_rep:
                    board[i][j] = 'X'


if __name__ == '__main__':
    board1 = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    print 'before board1 is %s' % board1
    print('\n')
    solve(board1)
    print('after board1 is %s') % board1

    print('\n')
    board2 = [['O', 'O', 'O'],
              ['O', 'O', 'O'],
              ['O', 'O', 'O']]

    print 'before board2 is %s' % board2
    print('\n')
    solve(board2)
    print('after board2 is %s') % board2

    print('\n')
    board3 = [['O', 'X', 'X', 'O', 'X'],
              ['X', 'O', 'O', 'X', 'O'],
              ['X', 'O', 'X', 'O', 'X'],
              ['O', 'X', 'O', 'O', 'O'],
              ['X', 'X', 'O', 'X', 'O']]

    print 'before board3 is %s' % board3
    print('\n')
    solve(board3)
    print('after board3 is %s') % board3
