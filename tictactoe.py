# The game of tic tac toe, played by computer based on #1 of 4 strategies in order:
# 1. Check if already 2 of three cells in a winning position is attained, then fill the 3rd pos
# 2. TODO: Check if a cell is vulnerable (i.e. the opponent would win if gets the cell as empty in next turn)
# 3. TODO: Check if there exists an empty cell that gives 2 winning options. This will guarrantee win in next turn by rule 1.
# 4. TODO: Check if a cell can be filled that draws the game

import random

def create_board():
    board = ['_' for i in range(9)]
    return board

def show_board(board):
    for i in range(0,9,3):
    	print board[i], board[i+1], board[i+2]

win_states = {
	0: [(1,2), (3,6), (4,8)],
	1: [(0,2), (4,7)],
	2: [(0,1), (5,8), (4,6)],
	3: [(4,5), (0,6)],
	4: [(3,5), (1,7), (0,8), (2,6)],
	5: [(3,4), (2,8)],
	6: [(7,8), (0,3), (2,4)],
	7: [(6,8), (1,4)],
	8: [(6,7), (2,5),(0,4)]
}

# set[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

# returns list of board indices which are empty
def empties(board):
	emp = []
	for i in range(9):
		if board[i] == '_':
			emp.append(i)
	return emp


def make_move(board, label):
	cells = []
	empty_cells = empties(board)
	for i in range(9):
		if board[i] == label:
			cells.append(i)
	for c in empty_cells:
		ps = win_states[c]
		for p in ps:
			if p[0] in cells and p[1] in cells:
				return c
	return empty_cells[random.randint(0, len(empty_cells)-1)]

def check_row(board):
	for i in range(0,9,3):
		if board[i]==board[i+1] and board[i+1]==board[i+2]:
			return board[i]
	return '_'

def check_col(board):
	for i in range(3):
		if board[i]==board[i+3] and board[i+3]==board[i+6]:
			return board[i]
	return '_'

def check_diag(board):
	if board[0]==board[4] and board[4]==board[8]:
		return board[4]
	elif board[2]==board[4] and board[4]==board[6]:
		return board[4]
	return '_'


def check_state(board):
	if check_row(board) != '_':
		return check_row(board)
	elif check_col(board) != '_':
		return check_col(board)
	elif check_diag(board) != '_':
		return check_diag(board)
	else:
		return '_'


def play_game(board):
	first = 'X'
	second = 'O'
	board[random.randint(0,8)] = first
	winner = '_'
	emp = empties(board)
	for i in range(4):
		board[make_move(board, second)] = second
		winner = check_state(board)
		if winner != '_':
			break
		board[make_move(board, first)] = first
		winner = check_state(board)
		if winner != '_':
			break
	return winner


def main():
    board = create_board()
    winner = play_game(board)
    show_board(board)
    print winner, "wins"


if __name__ == '__main__':
    main()
