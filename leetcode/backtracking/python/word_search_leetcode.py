"""
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

https://discuss.leetcode.com/topic/22788/python-dfs-solution-with-comments

below uses DFS

Typical dfs+backtracking question. It compare board[row][col] with word[start], if they match, change board[row][col] to '#' to mark it as visited. Then move to the next one (i.e. word[start+1] or word[1:]) and compare it to the current neighbors (doing it by recursion)

my understanding:

At the beginning, check if the current value matches the first char in word(word[0])

If it does:
  mark the value with # to indicate its visisted and check the other directions (down, up, left, right) adjacent/relative to the matching value to see if the value matches the next char in word. Keep doing this until all characters in the word are matched.

board[i][j] = temp, will resture all the marked # values to their original values and return to the previously matched visited value marked with #:

  a) when a search in directions down, up, right, and left have been completed.

  b) when the search is complete i.e the search run and matched all chars in word

  c) along the way a search didn't match, in which case it has to restore the original value so we can search other directions adjacent/relative to the previously visited/marked value

If it doesn't:
  move to the next value in the board and start the process all over

Time complexity: O(mn * 4^k) where k is the length of the string. mn for the loop and for dsf method its 4^k
Space complexity: O(mn)
"""

def exist(board, word):
    if not board: return False

    for i in range(len(board)): #row
        for j in range(len(board[0])): #col
            if helper(i, j, board, word):
                return True

    return False

def helper(i, j, board, word):
    if len(word) == 0:
        return True

    if i < 0 or i > len(board) - 1 or \
       j < 0 or j > len(board[0]) - 1 or \
       word[0] != board[i][j]:
            return False

    temp = board[i][j] # first character is found, check remaining part
    board[i][j] = '#' # avoid visit again

    # search down and up, then right and left
    result = helper(i + 1, j, board, word[1:]) or \
             helper(i - 1, j, board, word[1:]) or \
             helper(i, j + 1, board, word[1:]) or \
             helper(i, j - 1, board, word[1:])

    board[i][j] = temp

    return result


if __name__ == '__main__':
    board = [
              ['A','B','C','E'],
              ['S','F','C','S'],
              ['A','D','E','E']
            ]

    print exist(board, 'ABCCED')
    print '\n'
    print exist(board, 'SEE')
    print '\n'
    print exist(board, 'ABCB')
