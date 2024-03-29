=begin
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

  1. A move is guaranteed to be valid and is placed on an empty block.
  2. Once a winning condition is reached, no more moves is allowed.
  3. A player who succeeds in placing n of their marks in a horizontal, vertical,
      or diagonal row wins the game.

  Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|


Follow up:
Could you do better than O(n2) per move() operation?
=end
class TicTacToe
  attr_accessor :rows, :cols, :diagonal, :anti_diagonal

  def initialize(n)
    @rows = [0] * n
    @cols = [0] * n
    @diagonal = 0
    @anti_diagonal = 0
  end

  def move(row, col, player)
    mark = player == 1 ? 1 : -1

    rows[row] += mark
    cols[col] += mark

    diagonal += mark if row == col

    anti_diagonal += mark if col == (cols.length - row - 1)

    size = rows.length

    if rows[row].abs == size ||
       cols[col].abs == size ||
       diagonal.abs == size ||
       anti_diagonal.abs == size
      return player
    end

    0
  end
end

if $PROGRAM_NAME == __FILE__
  game = TicTacToe.new(3)
  game.move(0, 0, 1)
  game.move(0, 2, 2)
  game.move(2, 2, 1)
  game.move(1, 1, 2)
  game.move(2, 0, 1)
  game.move(1, 0, 2)
  game.move(2, 1, 1)
end
