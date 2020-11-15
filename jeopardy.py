import numpy as np

##riddler express
board = [200, 200, 200, 200, 200, 200, 
         400, 400, 400, 400, 400, 400, 
         600, 600, 600, 600, 600, 600, 
         800, 800, 800, 800, 800, 800,
         1000, 1000, 1000, 1000, 1000, 1000]

won_list = []
for y in range(10**6):
    dd = np.random.choice(len(board))
    total_won = 0
    for x in range(len(board)):
        if x == dd and total_won < 1000:
            total_won += 1000
        elif x == dd and total_won >= 1000:
            total_won += total_won
        else:
            total_won += board[x]
    won_list.append(total_won)

print(np.mean(won_list))

##bonus
won_list = []
for y in range(10**6):
    dd = np.random.choice(len(board))
    board_scramble = np.random.choice(board, size = 30, replace = False)
    total_won = 0
    for x in range(len(board_scramble)):
        if x == dd and total_won < 1000:
            total_won += 1000
        elif x == dd and total_won >= 1000:
            total_won += total_won
        else:
            total_won += board_scramble[x]
    won_list.append(total_won)

print(np.mean(won_list))