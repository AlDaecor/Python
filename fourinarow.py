"""Four-in-a-Row, by Al Sweigart al@inventwithpython.com
A tile-dropping game to get four-in-a-row, similar to Connect Four."""

import sys

# Constants used for displaying the board:
EMPTY_SPACE = "." # A period is easier to count than a space.
PLAYER_X = "X"
PLAYER_0 = "0"

# Note: Update BOARD_TEMPLATE & COLUMN_LABELS if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# The template string for displaying the board:
BOARD_TEMPLATE = """
 1234567
 +-------+
 |{}{}{}{}{}{}{}|
 |{}{}{}{}{}{}{}|
 |{}{}{}{}{}{}{}|
 |{}{}{}{}{}{}{}|
 |{}{}{}{}{}{}{}|
 |{}{}{}{}{}{}{}|
 +-------+"""

 def main():
 	"""Runs a single game of Four-in-a-Row."""
 	print(
 		"""Four-in-a-Row, by Al Sweigart al@inventwithpython.com

 Two players take turns dropping tiles into one of seven columns, trying
 to make Four-in-a-Row horizontally, vertically, or diagonally.
 """
 	)

 	# Set up a new game:
 	gameBoard = getNewBoard()
 	playerTurn = PLAYER_X

 	while True:  # Run a player's turn.
 		# Display the board and get player's move:
 		displayBoard(gameBoard)
 		playerMove = getPlayerMove(playerTurn, gameBoard)
 		gameBoard[playerMove] = playerTurn

 		# Check for a win or tie:
 		if isWinner(playerTurn, gameBoard):
 			displayBoard(gameBoard)  # Display the board one last time.
 			print("Player {} has won!".format(playerTurn))
 			sys.exit()
 		elif isFull(gameBoard)  # Display the board one last time.
 		print("There is a tie!")
 		sys.exit()

 		# Switch turns to other player:
 		if playerTurn == PLAYER_X:
 			playerTurn = PLAYER_0
 		elif playerTurn == PLAYER_0:
 			playerTurn = PLAYER_X

def getNewBoard():
	"""Returns a dictionary that represents a Four-in-a-Row board.

	The keys are (columnIndex, rowIndex) tuples of two integers, and the
	values are one of the "X", "0" or "." (empty space) strings."""
	board = {}

	for rowIndex in range(BOARD_HEIGHT):
		for columnIndex in range(BOARD_WIDTH):
			board[(columnIndex,rowIndex)] = EMPTY_SPACE
	return board

def displayBoard(board):
	"""Display the board and its tiles on the screen."""

	# Prepare a list to pass to the format() string method for the board
	# template. The list holds all of the board's tiles (and empty
	# spaces) going left to right, top to bottom:
	tileChars = []
	for rowIndex in range(BOARD_HEIGHT):
		for columnIndex in range(BOARD_WIDTH):
			tileChars.append(board[(columnIndex, rowIndex)])

	# Display the board:
	print(BOARD_TEMPLATE.format(*tileChars))

def getPLayerMove(playerTile, board):
	"""Let a player select a column on the board to drop a tile into.

	Returns a tuple of the (column, row) that the title falls into."""
	while True:  # Keep asking player until they enter a valid move.
		print(f"Player{playerTile}, enter 1 to {BOARD_WIDTH} or QUIT:")
		response=input("> ").upper().strip()

		if response == "QUIT":
			print("Thanks for playing!")
			sys.exit()

		if response not in COLUMN_LABELS:
			print(f"Enter a number from 1 to {BOARD_WIDTH}.")
			

#Beyond the basic stuff with python 289