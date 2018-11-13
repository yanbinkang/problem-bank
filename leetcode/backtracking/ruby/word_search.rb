=begin
https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
=end
def exist(board, word)
  return false if board.nil?

  board.length.times do |i| # row
    board[0].length.times do |j| # col
      return true if helper(i, j, board, word)
    end
  end

  false
end

def helper(i, j, board, word)
  return true if word.length.zero?

  if i < 0 || i > board.length - 1 ||
     j < 0 || j > board[0].length - 1 ||
     word[0] != board[i][j]
    return false
  end

  temp = board[i][j] # first character is found, check rest
  board[i][j] = '#' # avoid visit again

  # search down and up, then right and left
  result = helper(i + 1, j, board, word[1...word.length]) ||
           helper(i - 1, j, board, word[1...word.length]) ||
           helper(i, j + 1, board, word[1...word.length]) ||
           helper(i, j - 1, board, word[1...word.length])

  board[i][j] = temp

  result
end

if $PROGRAM_NAME == __FILE__
  board =
  [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
  ]

  puts exist(board, 'ABCCED')
  puts exist(board, 'SEE')
  puts exist(board, 'ABCB')
end
