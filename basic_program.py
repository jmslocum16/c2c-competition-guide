"""

Your program must implement the run() function to play the game.

The input to the run function is a 2d list representing the current state of the game.
The return value should be an integer represening the the column index you wish to play your piece, where 0 <= moveColumn < 7. You must play in a column that is not currently "full", meaning if the column already has 6 pieces in it, you cannot play there. There is guaranteed to be at least one valid column to play in.

The board variable is a list of lists. Each item in the first list represents a column in the board (starting from the left and going to the right). It is guaranteed that len(board) == 7.
Each column list represents all pieces in that column, starting from the bottom, and it is guaranteed that len(column_list) <= 6
Your program should assume that you are the Black player (pieces represented with 'B'), and your opponent is the Red player (pieces represented with 'R')

The following board:

|R| | | | | | |
|B| | |B| | | |
|B|R| |R|R|B|R|

Would be represented with the following 2d list:

[
  ['B', 'B', 'R'],
  ['R'],
  [],
  ['R'],
  ['R', 'B'],
  ['B'],
  ['R']
]

When you submit your program, it will be judged by:
 - Checking that it is a valid python program that has a run() function
 - That it can play a game against itself to completion (win/lose/draw) without performing any invalid moves, throwing any errors, or taking more than 5 seconds per move
   - an "invalid move" is defined as returning a non-int object from the run() function, returning an invalid column (not 0 through 6), or returning a column that already has 6 pieces

During the actual competition, similar rules will apply, with the exception that if your program makes an invalid move, throws an error, or takes more than 5 seconds,
your turn will be skipped, and you will not play a piece that turn.

"""

# Play in the first column, always.
# Note that this submission will fail, as it cannot actually complete a game against itself without making an invalid move.
def run(board):
    return 0
