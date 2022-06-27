#! python
#John Best
"""tictactoe

this is a multi-line comment too
"""

theBoard = {'topL': ' ', 'topM': ' ', 'topR': ' ',
			'midL': ' ', 'midM': ' ', 'midR': ' ',
			'lowL': ' ', 'lowM': ' ', 'lowR': ' ',}

def printBoard(board):
	print(board['topL'] + '|' + board['topM'] + '|' + board['topR'])
	print('-+-+-')
	print(board['midL'] + '|' + board['midM'] + '|' + board['midR'])
	print('-+-+-')
	print(board['lowL'] + '|' + board['lowM'] + '|' + board['lowR'])
	

turn = 'X'

for i in range(9):
	printBoard(theBoard)
	print(turn + '\'s turn' )
	move = input()
	theBoard[move] = turn

	print('move is ' + move)
	print('turn is ' + turn)


	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'


printBoard(theBoard)