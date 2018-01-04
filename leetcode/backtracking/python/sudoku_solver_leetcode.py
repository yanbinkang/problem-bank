"""
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'

You may assume that there will be only one unique solution.

https://discuss.leetcode.com/topic/11327/straight-forward-java-solution-using-backtracking/18

O(9 ^ m) m represents the number of blanks to be filled in since each blank can have 9 choices. (Exponential)
"""
def solve_sudoku(board):
    if not board or len(board) == 0:
        return

    solve(board)

def solve(board):
    for i in range(len(board)): # row
        for j in range(len(board[0])): # col
            if board[i][j] == '.':
                for c in '123456789':
                    if is_valid(board, i, j, c):
                        board[i][j] = c # put c in this cell

                        if solve(board):
                            return True # if its the solution return true
                        else:
                            board[i][j] = '.' # else go back
                return False # 1..9 cannot be placed on board
    return True # entire board is filled

def is_valid(board, row, col, c):
    for i in range(9):
        if board[i][col] == c:
            return False

        if board[row][i] == c:
            return False

    # this is also correct but results in longer runtime
    # for j in range(9):
    #     if board[row][j] == c:
    #         return False

    # check sub-box
    for i in range(3):
        for j in range(3):
            if board[3 * (row / 3) + i][3 * (col / 3) + j] == c:
                return False

    return True

# solution for 4 x 4 board. Use for testing
def solve_sudoku_4_by_4(board):
    if not board or len(board) == 0:
        return

    solve_4_by_4(board)

def solve_4_by_4(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                for c in '1234':
                    if is_valid_4_by_4(board, i, j, c):
                        board[i][j] = c

                        if solve_4_by_4(board):
                            return True
                        else:
                            board[i][j] = '.'
                return False # 1, 2, 3, 4 cannot be placed on board
    return True # entire board is filled

def is_valid_4_by_4(board, row, col, c):
    for i in range(4):
        if board[i][col] == c:
            return False

        if board[row][i] == c:
            return False

    for i in range(2):
        for j in range(2):
            if board[2 * (row / 2) + i][2 * (col / 2 ) + j] == c:
                return False
    return True


if __name__ == '__main__':
    board = [['.' for i in range(9)] for j in range(9)]

    board[0] = list('53..7....')
    board[1] = list('6..195...')
    board[2] = list('.98....6.')
    board[3] = list('8...6...3')
    board[4] = list('4..8.3..1')
    board[5] = list('7...2...6')
    board[6] = list('.6....28.')
    board[7] = list('...419..5')
    board[8] = list('....8..79')

    board_1 = [[None for i in range(4)] for j in range(4)]

    board_1[0] = list('1.3.')
    board_1[1] = list('..21')
    board_1[2] = list('.1.2')
    board_1[3] = list('24..')

    solve_sudoku(board)

    # print board
    print '9 x 9 board solution'
    print '\n'
    for i in range(len(board)):
        for j in range(len(board)):
            print board[i][j],

        print '\n'

    print '\n'

    solve_sudoku_4_by_4(board_1)

    print '4 x 4 board solution'
    print '\n'
    for i in range(len(board_1)):
        for j in range(len(board_1)):
            print board_1[i][j],

        print '\n'
