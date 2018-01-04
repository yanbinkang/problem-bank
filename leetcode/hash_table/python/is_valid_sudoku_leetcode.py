"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

This is similar to sudoku solver but not backtracking question. Move to
Hash Table category

https://leetcode.com/problems/valid-sudoku/

https://discuss.leetcode.com/topic/23811/clean-and-easy82ms-python

solution: Uses a set. store (row, current), (current, col) and sub-boxes and check for duplicates.

- (row, current) stores the value in each row. So if there is a duplicate we can tell easily. Eg. (0, '1') means row 0 has a value of '1' stored in a cell; (0, '8') means row 0 has a value of '8' stored in a cell.

- The same goes for the columns: (current, col) stores the value in each column. Eg. ('1', 6) means '1' is stored in column 6. So onces we encounter this same combination we know there's a duplicate '1' in column 6.

For sub-boxes: in a nxn box there'll be 4 sub-boxes represented as:
first box values (0, 0, current), second box is (0, 1, current).
third box is (1, 0, current), fourth box (1, 1, current).

Example of 4 sub-boxes in 4x4 box:

[['.', '.',    '.', '.'],
 ['.', '.',    '.', '.'],

 ['.', '.',    '.', '.'],
 ['.', '.',    '.', '.']]

- The top left sub-box represents (0, 0, current), meaning the first sub-boxes has value represented by current

- The top right sub-box represents (0, 1, current), meaning the second sub-boxes has value represented by current

- The bottom left sub-box represents (1, 0, current), meaning the third sub-boxes has value represented by current

- The bottom right sub-box represents (1, 1, current), meaning the fourth sub-boxes has value represented by current

"""
def is_valid_sudoku(board): # 9 x 9 board
    if not board or len(board) == 0: return

    store = set()

    for row in range(9):
        for col in range(9):
            if board[row][col] != '.':
                current = board[row][col]
                if (row, current) in store or\
                   (current, col) in store or\
                   (row/3, col/3, current) in store: # store sub-boxes
                        return False

                store.add((row, current))
                store.add((current, col))
                store.add((row/3, col/3, current))

    return True

# solution for smaller data set of 4x4 box
def is_valid_sudoku_4_by_4(board):
    if not board or len(board) == 0: return

    store = set()

    for row in range(4):
        for col in range(4):
            if board[row][col] != '.':
                current = board[row][col]

                if (row, current) in store or\
                   (current, col) in store or\
                   (row/2, col/2, current) in store:
                        return False

                store.add((row, current))
                store.add((current, col))
                store.add((row/2, col/2, current))

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

    board_1[0] = list('1234')
    board_1[1] = list('4321')
    board_1[2] = list('.132')
    board_1[3] = list('24..')


    print is_valid_sudoku(board)
    print('\n')
    print is_valid_sudoku_4_by_4(board_1)
