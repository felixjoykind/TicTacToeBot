#wtf i'm doing
from colorama import init
from colorama import Back, Fore, Style
import os

init()
# Game Board
board = ["-", "-", "-",
		 "-", "-", "-",
		 "-", "-", "-"]

#clear console function
clear = lambda: os.system('cls')
#If game still going
game_still_going = True

#Winner
winner = None

#Whos turn
current_player = 'X'

def display_board():
	print()
	print( board[0] + " | " + board[1] + " | " + board[2] + "		1 | 2 | 3")
	print( board[3] + " | " + board[4] + " | " + board[5] + "		4 | 5 | 6")
	print( board[6] + " | " + board[7] + " | " + board[8] + "		7 | 8 | 9")


def play_game():
	while game_still_going:
		#clearing the console
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
	if winner == 'X' or winner == 'O':
		#clearing the console
		clear()
		#displaying the board
		display_board()
		print(Back.YELLOW)
		print( f"{winner} won." )
		print(Back.BLACK)
	elif winner == None:
		#clearing the console
		clear()
		#displaying the board
		display_board()
		print(Back.YELLOW)
		print( "Tie." )
		print(Back.BLACK)

def handle_turn(player):

	print()
	#displaying whos turn it is
	print(Back.GREEN)
	print( f"{player}'s turn." )
	print(Back.BLACK)
	print()
	#getting position
	position = input( "Choose the position 1-9: " )

	#while position isn't valid
	while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		#clearing console
		clear()
		#displaying the board
		display_board()
		print(Back.GREEN)
		print( f"{current_player}'s turn." )
		print(Back.RED)
		position = input( "[!]Invalid input. Choose the position 1-9: " )
		print(Back.BLACK)

	position = int(position) - 1

	#Placing player
	if board[position] == '-':
		board[position] = player
		display_board()
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
		current_player = 'O'
	else:
		current_player = 'X'

def check_if_game_over():
	#checking if someone won
	check_if_winner()
	#checking if ts's a tie
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
		return board[0]
	elif row2:
		return board[3]
	elif row3:
		return board[6]
	return

def check_columns():
	global game_still_going

	#check columns for havong same values
	column1 = board[0] == board[3] == board[6] != '-'
	column2 = board[1] == board[4] == board[7] != '-'
	column3 = board[2] == board[5] == board[8] != '-'

	#if
	if column1 or column2 or column3:
		game_still_going = False

	#returning the winner
	if column1:
		return board[0]
	elif column2:
		return board[1]
	elif column3:
		return board[2]
	return

def check_diagonals():
	global game_still_going

	#check diagonals for havong same values
	diagonal1 = board[0] == board[4] == board[8] != '-'
	diagonal2 = board[6] == board[4] == board[2] != '-'

	#if
	if diagonal1 or diagonal2:
		game_still_going = False

	#returning the winner
	if diagonal1:
		return board[0]
	elif diagonal2:
		return board[6]
	return

play_game()