import numpy as np

xo = [1,1,1,1,1,0,0,0,0]
n_games = 10000
get_avg = []
for y in range(10):
    wins = 0
    for x in range(n_games):
        ttt_board = np.random.choice(xo, 9, replace = False).reshape(3,3)
        if (ttt_board[0][0] == 1 and ttt_board[0][1] == 1 and ttt_board [0][2] == 1) \
        or (ttt_board[1][0] == 1 and ttt_board[1][1] == 1 and ttt_board [1][2] == 1) \
        or (ttt_board[2][0] == 1 and ttt_board[2][1] == 1 and ttt_board [2][2] == 1) \
        or (ttt_board[0][0] == 1 and ttt_board[1][0] == 1 and ttt_board [2][0] == 1) \
        or (ttt_board[0][1] == 1 and ttt_board[1][1] == 1 and ttt_board [2][1] == 1) \
        or (ttt_board[0][2] == 1 and ttt_board[1][2] == 1 and ttt_board [2][2] == 1) \
        or (ttt_board[0][0] == 1 and ttt_board[1][1] == 1 and ttt_board [2][2] == 1) \
        or (ttt_board[0][2] == 1 and ttt_board[1][1] == 1 and ttt_board [2][0] == 1):
            wins += 1
    get_avg.append(wins/n_games)

print(np.mean(get_avg))