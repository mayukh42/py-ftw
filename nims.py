# nims.py

import random

def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones. The players sit
    in front of a pile of 100 stones. They take turns, each removing 
    between 1 and 5 stones (assuming there are at least 5 stones left in 
    the pile). The person who removes the last stone(s) wins.

    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''
    player = 0
    rounds = 0
    while pile > 0:
        if pile > max_stones:
            pick = random.randint(1, max_stones)
        else:
            pick = pile
        pile -= pick
        print player, "picks", pick, "stones. ", pile, "remaining"
        player = 1 - player
        rounds += 1

    print "Game over"
    return 1 - player, rounds


def main():
    game = play_nims(100, 5)
    print game[0], "wins in", game[1], "rounds"


if __name__ == '__main__':
    main()
