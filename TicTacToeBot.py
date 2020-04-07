#wtf i'm doing
from random import randint
from colorama import init
from colorama import Back, Fore, Style
import os

init()

#clear console...
clear = lambda: os.system('cls')

# Game Board
board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]

#If game still going
game_still_going = True

#Winner
winner = None

#Whos turn
current_player = 'X'

#Board
def display_board():
	print()
	print( board[0] + " | " + board[1] + " | " + board[2] + "		1 | 2 | 3")
	print( board[3] + " | " + board[4] + " | " + board[5] + "		4 | 5 | 6")
	print( board[6] + " | " + board[7] + " | " + board[8] + "		7 | 8 | 9")

#game loop
def play_game():
	while game_still_going:
		#clearing console
		clear()
		#displaying the board
		display_board()
		#Giving player a turn
		handle_turn(current_player)

		#Checking for winners
		check_if_game_over()

		#Fliping player
		flip_player()

	#Game has ended
	if winner == 'X':
		#clearing console
		clear()
		display_board()
		#back color
		print( Back.YELLOW )
		print( "X won." )
		print( Back.BLACK )
	elif winner == "Bot":
		#clearing console
		clear()
		display_board()
		#back color
		print( Back.YELLOW )
		print( "Bot win" )
		print( Back.BLACK )
	elif winner == None:
		#clearing console
		clear()
		display_board()
		#back color
		print( Back.YELLOW )
		print( "Tie." )
		print( Back.BLACK )

def handle_turn(player):
	#displaying whos turn it is
	if player == 'X':
		print()
		print( f"{player}'s turn." )
	print()

	if player == "X":
		#getting position
		position = input( "Choose the position 1-9: " )
		#while position isn't valid
		while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			clear()
			display_board()
			print( Back.RED )
			position = input( "[!]Invalid input. Choose the position 1-9: " )
			print( Back.BLACK )

		position = int(position) - 1
	elif player == "Bot":
		position = check_board_bot()

	#Placing player
	if board[position] == '-' and player == "X":
		board[position] = player
		display_board()
	elif board[position] == '-' and player == "Bot":
		if board[position] == '-':
			board[position] = 'O'
			display_board()
		else:
			handle_turn(current_player)
	else:
		#clearing the console
		clear()
		#displaying the board
		display_board()
		print()
		print( 'Place is already taken' )
		handle_turn(current_player)

def flip_player():
	#Switching to other player
	global current_player
	if current_player == 'X':
		current_player = 'Bot'
	else:
		current_player = 'X'

def check_if_game_over():
	#checking if someone won
	check_if_winner()
	#checking if its's a tie
	check_if_tie()

def check_if_winner():
	global winner

	#check rows
	row_winner = check_rows()
	#check columns
	column_winner = check_columns()
	#check diagonals
	diagonal_winner = check_diagonals()

	if row_winner:
		winner = row_winner
	elif column_winner:
		winner = column_winner
	elif diagonal_winner:
		winner = diagonal_winner
	else:
		winner = None

def check_if_tie():
	global game_still_going

	#checking for tie
	if '-' not in board:
		game_still_going = False

	return

def check_rows():
	global game_still_going

	#check rows for havong same values
	row1 = board[0] == board[1] == board[2] != '-'
	row2 = board[3] == board[4] == board[5] != '-'
	row3 = board[6] == board[7] == board[8] != '-'

	#if
	if row1 or row2 or row3:
		game_still_going = False

	#returning the winner
	if row1:
		if board[0] == 'X':
			return board[0]
		else:
			return 'Bot'
	elif row2:
		if board[3] == 'X':
			return board[0]
		else:
			return 'Bot'
	elif row3:
		if board[6] == 'X':
			return board[0]
		else:
			return 'Bot'
	return

def check_columns():
	global game_still_going

	#check columns for having same values
	column1 = board[0] == board[3] == board[6] != '-'
	column2 = board[1] == board[4] == board[7] != '-'
	column3 = board[2] == board[5] == board[8] != '-'

	#if
	if column1 or column2 or column3:
		game_still_going = False

	#returning the winner
	if column1:
		if board[0] == 'X':
			return board[0]
		else:
			return 'Bot'
	elif column2:
		if board[1] == 'X':
			return board[1]
		else:
			return 'Bot'
	elif column3:
		if board[2] == 'X':
			return board[2]
		else:
			return 'Bot'

def check_diagonals():
	global game_still_going

	#check diagonals for having same values
	diagonal1 = board[0] == board[4] == board[8] != '-'
	diagonal2 = board[6] == board[4] == board[2] != '-'

	#if
	if diagonal1 or diagonal2:
		game_still_going = False

	#returning the winner
	if diagonal1:
		if board[0] == 'X':
			return board[0]
		else:
			return 'Bot'
	elif diagonal2:
		if board[6] == 'X':
			return board[6]
		else:
			return 'Bot'
	return

def check_board_bot():
	#check rows for having same values
	row1 = board[0] == board[1] != '-' or board[1] == board[2] != '-' or board[0] == board[2] != '-'
	row2 = board[3] == board[4] != '-' or board[4] == board[5] != '-' or board[3] == board[5] != '-'
	row3 = board[6] == board[7] != '-' or board[7] == board[8] != '-' or board[6] == board[8] != '-'

	#check columns for having same values
	column1 = board[0] == board[3] != '-' or board[3] == board[6] != '-' or board[0] == board[6] != '-'
	column2 = board[1] == board[4] != '-' or board[4] == board[7] != '-' or board[1] == board[7] != '-'
	column3 = board[2] == board[5] != '-' or board[5] == board[8] != '-' or board[2] == board[8] != '-'

	#check diagonals for having same values
	diagonal1 = board[0] == board[4] != '-' or board[4] == board[8] != '-' or board[0] == board[8] != '-'
	diagonal2 = board[6] == board[4] != '-' or board[4] == board[2] != '-' or board[6] == board[2] != '-'

	if row1:
		if board[0] == '-':
			return 0
		elif board[1] == '-':
			return 1
		elif board[2] == '-':
			return 2
	elif row2:
		if board[3] == '-':
			return 3
		elif board[4] == '-':
			return 4
		elif board[5] == '-':
			return 5
	elif row3:
		if board[6] == '-':
			return 6
		elif board[7] == '-':
			return 7
		elif board[8] == '-':
			return 8
	
	if column1:
		if board[0] == '-':
			return 0
		elif board[3] == '-':
			return 3
		elif board[6] == '-':
			return 6
	elif column2:
		if board[1] == '-':
			return 1
		elif board[4] == '-':
			return 4
		elif board[7] == '-':
			return 7
	elif column3:
		if board[2] == '-':
			return 2
		elif board[5] == '-':
			return 5
		elif board[8] == '-':
			return 8
	
	if diagonal1:
		if board[0] == '-':
			return 0
		elif board[4] == '-':
			return 4
		elif board[8] == '-':
			return 8
	elif diagonal2:
		if board[6] == '-':
			return 6
		elif board[4] == '-':
			return 4
		elif board[2] == '-':
			return 2

	return randint(0, 8)

play_game()