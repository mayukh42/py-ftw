#Snakes and Ladders
#The game consists of a 10x10 playing board of squares.
import random
def create_board():
    # This method creates and returns an array representing
    # the playing board. Each cell represents the cell it can "teleport" to.
    # board[13] = 47, means 14th square ends up in square 48.
    # The special squares are as follows...
    # "Ladders": 14->48, 19->60, 55->76, 69->90, 78->97.
    # "Snakes": 99->29. 47->18, 25->7.
    board = range(100)
    board[13] = 47
    board[18] = 59
    board[54] = 75
    board[68] = 89
    board[77] = 96
    board[98] = 28
    board[46] = 17
    board[24] = 6
    return board


def get_step():
    # Select a random number from 1-6 and return that number.
    # This simulates the rolling of a single die.
    return random.randint(1, 6)


def make_move(board, playerPos, step):
    # This method will move a player's piece across the board.
    # The player rolls a dice. The value of that roll is step.
    # The player's current board position is playerPos.
    # If playerPos + step > 99, player does not move.
    newPos = board[playerPos] + step
    if newPos <= 99:
        return board[newPos]
    else:
        return board[playerPos]

def play_game(board):
    playerA = 0
    playerB = 0
    while not (playerA == 99 or playerB == 99):
        playerA = make_move(board, playerA, get_step())
        playerB = make_move(board, playerB, get_step())
        print playerA, playerB
    if playerA == 99:
        print "Player A wins!"
    else:
        print "Player B wins!"

def main():
    play_game(create_board())


if __name__ == '__main__':
    main()
