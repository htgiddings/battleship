from random import randint

#Data definitions
BOARD_SIZE = 5
board = []
tile_state = { 'empty': 'O', 'miss': 'X', 'hit': '*' }

#functions
for x in range(0, BOARD_SIZE):
  board.append([tile_state['empty']] * BOARD_SIZE)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

#start game
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row, ship_col #debug
for turn in range(4):
  print "Turn", turn + 1
  print_board( board )
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    board[guess_row][guess_col] = tile_state['hit']
    print_board( board )
    break
  else:
    if guess_row not in range( BOARD_SIZE ) or \
      guess_col not in range( BOARD_SIZE ):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] != tile_state['empty']:
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = tile_state['miss']
    if turn == 3:
      print "Game Over"
