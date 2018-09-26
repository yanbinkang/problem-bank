=begin
https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

  1. Each row must contain the digits 1-9 without repetition.
  2. Each column must contain the digits 1-9 without repetition.
  3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:

  * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
  * Only the filled cells need to be validated according to the mentioned rules.
  * The given board contain only digits 1-9 and the character '.'.
  * The given board size is always 9x9.


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

- The top left sub-box represents (0, 0, current), meaning the first sub-box contains a value represented by current

- The top right sub-box represents (0, 1, current), meaning the second sub-boxes has value represented by current

- The bottom left sub-box represents (1, 0, current), meaning the third sub-box contains a value represented by current

- The bottom right sub-box represents (1, 1, current), meaning the fourth sub-box contains a value represented by current
=end
require 'set'
def is_valid_sudoku(board)
  return if board.nil? || board.length == 0

  store = Set.new

  9.times do |row|
    9.times do |col|
      if board[row][col] != '.'
        current = board[row][col]

        if store.include?([row, current]) ||
            store.include?([current, col]) ||
            store.include?([row/3, col/3, current])
          return false
        end

        store.add([row, current])
        store.add([current, col])
        store.add([row/3, col/3, current])
      end
    end
  end

  return true
end

if __FILE__ == $0
  board = Array.new(9) { Array.new(9, '.') }

  board[0] = '53..7....'.split('')
  board[1] = '6..195...'.split('')
  board[2] = '.98....6.'.split('')
  board[3] = '8...6...3'.split('')
  board[4] = '4..8.3..1'.split('')
  board[5] = '7...2...6'.split('')
  board[6] = '.6....28.'.split('')
  board[7] = '...419..5'.split('')
  board[8] = '....8..79'.split('')

  puts is_valid_sudoku(board)
end
