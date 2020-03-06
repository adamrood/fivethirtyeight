# Riddler Express 03/06/20
# A local cafe has board games on a shelf, designed to keep kids (and some adults) 
# entertained while they wait on their food. One of the games is a tic-tac-toe board, 
# which comes with nine pieces that you and your opponent can place: five Xs and four Os.

# When I took my two-year-old with me, he wasn’t particularly interested in the game 
# itself, but rather in the placement of the pieces.

# If he randomly places all nine pieces in the nine slots on the tic-tac-toe 
# board (with one piece in each slot), what’s the probability that X wins? That is, 
# what’s the probability that there will be at least one occurrence of three Xs in a 
# row at the same time there are no occurrences of three Os in a row?

import numpy as np

xo = [1,1,1,1,1,0,0,0,0]
n_games = 10000
get_avg = []
for y in range(10):
    wins = 0
    for x in range(n_games):
        b = np.random.choice(xo, 9, replace = False).reshape(3,3)
        if (b[0][0] == 1 and b[0][1] == 1 and b [0][2] == 1) \
        or (b[1][0] == 1 and b[1][1] == 1 and b [1][2] == 1) \
        or (b[2][0] == 1 and b[2][1] == 1 and b [2][2] == 1) \
        or (b[0][0] == 1 and b[1][0] == 1 and b [2][0] == 1) \
        or (b[0][1] == 1 and b[1][1] == 1 and b [2][1] == 1) \
        or (b[0][2] == 1 and b[1][2] == 1 and b [2][2] == 1) \
        or (b[0][0] == 1 and b[1][1] == 1 and b [2][2] == 1) \
        or (b[0][2] == 1 and b[1][1] == 1 and b [2][0] == 1):
            wins += 1
    get_avg.append(wins/n_games)

print(np.mean(get_avg))
